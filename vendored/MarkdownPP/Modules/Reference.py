# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import re

from MarkdownPP.Module import Module
from MarkdownPP.Transform import Transform

refre = re.compile(r"^!REF\s*$")
linkre = re.compile(r"^\[([^\]]+)\]:\s+(\S+)(?:\s*[\"'\(](.+)[\"'\(]\s*)?$")


class Reference(Module):
    """
    Module for auto-generating a list of reference links used in the document.
    The referenc list is inserted wherever a `!REF` marker is found at the
    beginning of a line.
    """

    def transform(self, data):
        transforms = []

        reffound = False
        reflines = []
        refdata = ""

        links = []

        # iterate through the document looking for !REF markers and links
        linenum = 0
        for line in data:

            match = refre.search(line)
            if match:
                reffound = True
                reflines.append(linenum)

            match = linkre.search(line)
            if match:
                name = match.group(1)
                if len(match.groups()) > 2:
                    title = match.group(3)
                else:
                    title = name.lower()

                links.append((name, title))

            linenum += 1

        # short circuit if no markers found
        if not reffound:
            return []

        for name, title in links:
            refdata += "*\t[%s][%s]\n" % (title, name)

        # create transforms for each marker
        for linenum in reflines:
            transforms.append(Transform(linenum, "swap", refdata))

        return transforms
