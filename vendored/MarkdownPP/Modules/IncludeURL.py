# Copyright (C) 2016 Smart Software Solutions, Inc
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import re

try:
    # Python3
    from urllib.request import urlopen
    from urllib.parse import urlparse
except ImportError:
    # Python2
    from urllib import urlopen
    from urlparse import urlparse

from MarkdownPP.Modules.Include import Include


class IncludeURL(Include):
    """
    Module for recursively including the contents of other remote files into
    the current document using a command like
    `!INCLUDEURL "http://www.example.com"`.
    Targets must be valid, absolute urls.
    """

    includere = re.compile(r"^!INCLUDEURL\s+(?:\"([^\"]+)\"|'([^']+)')\s*$")

    # include urls should happen after includes, but before everything else
    priority = 0.1

    def include(self, match):
        if match.group(1) is None:
            url = match.group(2)
        else:
            url = match.group(1)

        parsed_url = urlparse(url)
        if not parsed_url.netloc and not parsed_url.path:
            return []

        binary_data = urlopen(url).readlines()
        data = []
        for datum in binary_data:
            data.append(datum.decode())
        if data:
            # recursively include url data
            for line_num, line in enumerate(data):
                match = self.includere.search(line)
                if match:
                    data[line_num:line_num+1] = self.include(match)

                line_num += 1

            return data

        return []
