# Copyright (C) 2012 Alex Nisnevich
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import re
from contextlib import closing

try:
    from http.client import HTTPConnection
    from urllib.parse import urlencode
except ImportError:
    from httplib import HTTPConnection
    from urllib import urlencode

from MarkdownPP.Module import Module
from MarkdownPP.Transform import Transform

# $...$ (or $$...$$)
singlelinere = re.compile(r"\$(\$?)..*\$(\$?)")
# $... or ...$ (or $$... or ...$$)
startorendre = re.compile(r"^\$(\$?)|^\S.*\$(\$?)$")

codere = re.compile(r"^(    |\t)")
spancodere = re.compile(r'(`[^`]+\`)')  # code between backticks

# Support for Pandoc style code blocks with attributes
fencedcodere = re.compile(r"^((> *)?```\w*|(> *)?~~~~*(\s*{.*})?)$")


class LaTeXRender(Module):
    """
    Module for rendering LaTeX enclosed between $ dollar signs $.
    Rendering is performed using QuickLaTeX via ProblemSetMarmoset.
    """

    def transform(self, data):
        transforms = []
        linenum = 0
        in_block = False
        current_block = ""
        in_fenced_code_block = False

        for line in data:
            # Handling fenced code blocks (for Github-flavored markdown)
            if fencedcodere.search(line):
                if in_fenced_code_block:
                    in_fenced_code_block = False
                else:
                    in_fenced_code_block = True

            # Are we in a code block?
            if not in_fenced_code_block and not codere.search(line):
                # Is this line part of an existing LaTeX block?
                if in_block:
                    transforms.append(Transform(linenum, "drop"))
                    current_block += "\n" + line

                match = singlelinere.search(line)
                if match:
                    code_pos = []
                    for m in spancodere.finditer(line):
                        code_pos += range(*m.span())

                    if not (match.start(0) in code_pos or
                            match.end(0) in code_pos):

                        # Single LaTeX line
                        tex = match.group(0)
                        before_tex = line[0:line.find(tex)]
                        after_tex = line[(line.find(tex) + len(tex)):
                                         len(line)]
                        transforms.append(Transform(linenum, "swap",
                                                    before_tex +
                                                    self.render(tex) +
                                                    after_tex))
                else:
                    match = startorendre.search(line)
                    if match:
                        # Starting or ending a multi-line LaTeX block
                        if in_block:
                            # Ending a LaTeX block
                            transforms.pop()  # undo last drop
                            transforms.append(Transform(linenum, "swap",
                                              self.render(current_block)))
                        else:
                            # Starting a LaTeX block
                            current_block = line
                            transforms.append(Transform(linenum, "drop"))
                        in_block = not in_block

            linenum += 1

        return transforms

    def render(self, formula):
        # Prepare the formula
        formula = formula.replace("$", "")
        encoded_formula = formula.replace("%", "[comment]").replace("+", "%2B")
        display_formula = formula.replace("\n", "")
        print('Rendering: %s ...' % display_formula)

        # Prepare POST request to QuickLaTeX via ProblemSetMarmoset
        # (for added processing)
        params = urlencode({
            'engine': 'quicklatex',
            'input': encoded_formula,
        })
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}

        # Make the request
        with closing(HTTPConnection("www.problemsetmarmoset.com")) as conn:
            conn.request("POST", "/latex/render.php", params, headers)
            response = conn.getresponse()
            img_url = response.read()

        # Display as Markdown image
        rendered_tex = '![{0}]({1} "{0}")\n'.format(display_formula,
                                                    img_url.decode('utf-8'))
        return rendered_tex
