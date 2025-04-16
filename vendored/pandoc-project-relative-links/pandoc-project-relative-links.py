#!/usr/bin/env python3
## Created by Mike Fuller (FinOps Foundation)
#  Based on Daniel Jour (musteresel)'s Haskell version of this plugin:
#  https://github.com/musteresel/pandoc-project-relative-links/tree/master
#
#  Licensed under the MIT license
#
#  Permission is hereby granted, free of charge, to any person obtaining
#  a copy of this software and associated documentation files (the
#  "Software"), to deal in the Software without restriction, including
#  without limitation the rights to use, copy, modify, merge, publish,
#  distribute, sublicense, and/or sell copies of the Software, and to
#  permit persons to whom the Software is furnished to do so, subject to
#  the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
##

import panflute as pf

def consider_as_project_relative(url):
    return url.startswith('/')

def adjust_link(elem, doc):
    path = doc.get_metadata('pathToProjectRoot')
    if not path:
        return None

    if isinstance(elem, pf.Link) and consider_as_project_relative(elem.url):
        elem.url = path + elem.url
    elif isinstance(elem, pf.Image) and consider_as_project_relative(elem.url):
        elem.url = path + elem.url
    return elem

def main(doc=None):
    return pf.run_filter(adjust_link, doc=doc)

if __name__ == '__main__':
    main()

