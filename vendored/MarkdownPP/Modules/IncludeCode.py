# Copyright (C) 2016 Smart Software Solutions, Inc
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import re

from os import path

from MarkdownPP.Modules.Include import Include


class IncludeCode(Include):
    """
    Module for recursively including the contents of other local code
    files into the current document using a command like
    `!INCLUDECODE "codes/mycode.py"`.
    Targets must be valid, absolute urls.
    """

    includere = re.compile(r"^!INCLUDECODE\s+(?:\"([^\"]+)\"|'([^']+)')"
                           r"(?:\s*\(\s*(.*)\s*\)\s*)?"
                           r"\s*(?:,\s*(\d+|(\d*:\d*)))?\s*$")

    # include code should happen after includes, but before everything else
    priority = 0.1

    def _select_lines(self, code_file, lines):
        # No lines given
        if lines is None:
            return code_file
        # Single line
        if ':' not in lines:
            # Line counting starts at 1. Need to offset by -1
            return code_file[(int(lines) - 1)]

        # Multiline python style e.g. 1:5, :5, 5:
        from_line, to_line = [int(x) if x else None for x in lines.split(':')]
        if from_line is None or from_line <= 0:
            from_line = 1
        if to_line is None or to_line > len(code_file):
            to_line = len(code_file)
        # Line counting starts at 1. Need to offset by -1
        return code_file[(from_line - 1):to_line]

    def include(self, match, pwd=""):
        code_file = match.group(1) or match.group(2)
        lang = match.group(3)
        lines = match.group(4)

        if not path.isabs(code_file):
            code_file = path.join(pwd, code_file)

        try:
            with open(code_file, "r") as fs:
                code_data = fs.readlines()

            return (
                "```" + (str(lang) if lang is not None else "") + "\n"
                + "".join(self._select_lines(code_data, lines))
                + "\n```\n"
            )

        except (IOError, OSError) as exc:
            print(exc)

        return []
