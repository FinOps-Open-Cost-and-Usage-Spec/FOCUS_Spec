# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import re
import os

from MarkdownPP.Module import Module
from MarkdownPP.Transform import Transform

tocre = re.compile(r"^!TOC(\s+[1-6])*\s*$")
atxre = re.compile(r"^(#+)\s*(.+)$")
setextre = re.compile(r"^(=+|-+)\s*$")
fencedcodere = re.compile(r"^```[ \w]*$")
linkre = re.compile(r"(\[(.*?)\][\(\[].*?[\)\]])")
htmlcommentre = re.compile(r"\s*<!--.*?-->\s*$")


class TableOfContents(Module):
    """
    Module for auto-generating a table of contents based on the Markdown
    headers in the document.  The table of contents is inserted in the document
    wherever a `!TOC` marker is found at the beginning of a line.
    """

    @staticmethod
    def clean_title(title):
        for link in re.findall(linkre, title):
            title = title.replace(link[0], link[1])
        return title
    
    @staticmethod
    def strip_html_comments(title):
        """Strip HTML comments (like <!--SkipTOC-->) from the end of titles."""
        return htmlcommentre.sub('', title).strip()
    
    @staticmethod
    def has_skip_toc(title):
        """Check if title contains <!--SkipTOC--> comment."""
        return '<!--SkipTOC-->' in title
    
    @staticmethod
    def process_header(raw_title, depth, linenum, headers, tocfound, lowestdepth):
        """Process a header and add to headers dict if not marked to skip.
        Returns updated lowestdepth."""
        # Skip headers marked with <!--SkipTOC-->
        if TableOfContents.has_skip_toc(raw_title):
            return lowestdepth  # Skip this header entirely from TOC
        
        title = TableOfContents.strip_html_comments(raw_title)
        headers[linenum] = (depth, title)
        
        if tocfound:
            lowestdepth = min(depth, lowestdepth)
        
        return lowestdepth
    
    @staticmethod
    def add_spacing_for_skip_toc_headers(data, transforms):
        """Add proper spacing before SkipTOC headers to avoid MD022 linting errors."""
        linenum = 0
        for line in data:
            # Check for hash headers with SkipTOC
            match = atxre.search(line)
            if match:
                raw_title = match.group(2).strip()
                if TableOfContents.has_skip_toc(raw_title):
                    # Check if previous line is not empty and add spacing if needed
                    if linenum > 0 and data[linenum - 1].strip() != "":
                        transforms.append(
                            Transform(linenum - 1, "append", "\n")
                        )
            linenum += 1
        return transforms

    def transform(self, data):
        transforms = []

        lowestdepth = 10

        tocfound = False
        toclines = []
        tocdepth = 3
        tocdepths = []
        if tocdepth == 0:
            tocdepth = 6
        tocdata = ""

        headers = {}

        infencedcodeblock = False

        # iterate through the document looking for markers and headers
        linenum = 0
        lastline = ""
        for line in data:
            # Fenced code blocks (Github-flavored markdown)
            match = fencedcodere.search(line)
            if match:
                if infencedcodeblock:
                    infencedcodeblock = False
                else:
                    infencedcodeblock = True

            # !TOC markers
            match = tocre.search(line)
            if match:
                tocfound = True
                tocdepths = re.findall(r'\b[1-6]\b', line)
                if tocdepths:
                    tocdepth = int(tocdepths[0])
                toclines.append(linenum)

            # hash headers
            match = atxre.search(line)
            if match and not infencedcodeblock:
                depth = len(match.group(1))
                raw_title = match.group(2).strip()
                lowestdepth = TableOfContents.process_header(
                    raw_title, depth, linenum, headers, tocfound, lowestdepth
                )

            # underlined headers
            match = setextre.search(line)
            if match and not infencedcodeblock and lastline.strip():
                depth = 1 if match.group(1)[0] == "=" else 2
                raw_title = lastline.strip()
                lowestdepth = TableOfContents.process_header(
                    raw_title, depth, linenum - 1, headers, tocfound, lowestdepth
                )

            lastline = line
            linenum += 1

        # short circuit if no !TOC directive
        if not tocfound:
            return []

        stack = []
        headernum = 0

        lastdepth = 1
        toc_lastdepth = 1
        depthoffset = 1 - lowestdepth

        keys = sorted(headers.keys())

        # Track the hierarchy for full path anchor generation
        hierarchy_stack = []

        # interate through the list of headers, generating the nested table
        # of contents data, and creating the appropriate transforms
        tocdata += f'<ul class="toc tocdepth1">\n'
        current_header_number = -1
        for linenum in keys:
            if linenum < toclines[0]:
                continue

            (depth, title) = headers[linenum]
            depth += depthoffset
            clean_title = re.sub(
                r"([\s,-,\(,\)]+)", "", TableOfContents.clean_title(title)
            ).lower()

            # Adjust hierarchy stack based on current depth
            while len(hierarchy_stack) >= depth:
                hierarchy_stack.pop()
            
            # Add current title to hierarchy
            hierarchy_stack.append(clean_title)
            
            # Generate full path anchor using the hierarchy
            short = ".".join(hierarchy_stack)

            while depth > lastdepth:
                stack.append(headernum)
                headernum = 0
                lastdepth += 1

            while depth < lastdepth:
                headernum = stack.pop()
                lastdepth -= 1

            headernum += 1

            if depth == 1:
                current_header_number += 1
                tocdepth = int(tocdepths[current_header_number]) if current_header_number < len(tocdepths) else 3
                section = "%d. " % headernum
            else:
                section = ".".join([str(x) for x in stack]) + ".%d. " % headernum

            transforms.append(
                Transform(
                    linenum, "swap", data[linenum].replace(title, section + title)
                )
            )
            transforms.append(
                Transform(
                    linenum - 1,
                    "append",
                    '<a class="toc-anchor" name="%s">&nbsp;</a>\n\n' % short,
                )
            )

            if depth > tocdepth:
                continue

            spacing = "  " * depth
            if depth < toc_lastdepth:  # ascending
                i = 0
                while i <= (toc_lastdepth - depth):
                    tocdata += f"{spacing}</ul>\n"
                    i += 1
                tocdata += f'{spacing}<ul class="toc tocdepth{depth}">\n'
            elif depth > toc_lastdepth:  # descending
                tocdata += f'{spacing}<ul class="toc tocdepth{depth}">\n'

            tocdata += f'{spacing}<li class="toc item">'
            tocdata += '<a href="#%s">%s %s</a>' % (
                short,
                section,
                TableOfContents.clean_title(title),
            )
            tocdata += "</li>\n"
            toc_lastdepth = depth
        tocdata += f"</ul>\n"
        # create transforms for the !TOC markers
        for linenum in toclines:
            transforms.append(Transform(linenum, "swap", tocdata))

        # Add proper spacing for SkipTOC headers
        transforms = TableOfContents.add_spacing_for_skip_toc_headers(data, transforms)

        return transforms
