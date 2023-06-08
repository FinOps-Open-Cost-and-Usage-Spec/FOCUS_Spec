# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import re
import os

from MarkdownPP.Module import Module
from MarkdownPP.Transform import Transform

tocre = re.compile(r"^!TOC(\s+[1-6])?\s*$")
atxre = re.compile(r"^(#+)\s*(.+)$")
setextre = re.compile(r"^(=+|-+)\s*$")
fencedcodere = re.compile(r"^```[ \w]*$")
linkre = re.compile(r"(\[(.*?)\][\(\[].*?[\)\]])")


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

    def transform(self, data):
        transforms = []

        lowestdepth = 10

        tocfound = False
        toclines = []
        tocdepth = int(os.environ.get("TOCDEPTH", 0))
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
                depth = match.group(1)
                if depth is not None:
                    depth = int(depth)
                    tocdepth = max(depth, tocdepth)
                toclines.append(linenum)

            # hash headers
            match = atxre.search(line)
            if match and not infencedcodeblock:
                depth = len(match.group(1))
                title = match.group(2).strip()
                headers[linenum] = (depth, title)

                if tocfound:
                    lowestdepth = min(depth, lowestdepth)

            # underlined headers
            match = setextre.search(line)
            if match and not infencedcodeblock and lastline.strip():
                depth = 1 if match.group(1)[0] == "=" else 2
                title = lastline.strip()
                headers[linenum - 1] = (depth, title)

                if tocfound:
                    lowestdepth = min(depth, lowestdepth)

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

        short_titles = []

        # interate through the list of headers, generating the nested table
        # of contents data, and creating the appropriate transforms
        tocdata += f'<ul class="toc tocdepth1">\n'
        for linenum in keys:
            if linenum < toclines[0]:
                continue

            (depth, title) = headers[linenum]
            depth += depthoffset
            short = re.sub(
                r"([\s,-,\(,\)]+)", "", TableOfContents.clean_title(title)
            ).lower()

            if short in short_titles:
                i = 1
                short_i = short
                while short_i in short_titles:
                    short_i = short + "-" + str(i)
                    i += 1
                short = short_i
            short_titles.append(short)

            while depth > lastdepth:
                stack.append(headernum)
                headernum = 0
                lastdepth += 1

            while depth < lastdepth:
                headernum = stack.pop()
                lastdepth -= 1

            headernum += 1

            if depth == 1:
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

        return transforms
