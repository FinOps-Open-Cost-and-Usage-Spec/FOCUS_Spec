# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
from os import path

modules = {}


def load_modules():
    dirname = path.dirname(path.abspath(__file__))

    for filename in os.listdir(dirname):
        (modulename, extension) = path.splitext(filename)
        if extension.lower() == ".py" and modulename.lower() != "__init__":
            module = __import__("MarkdownPP.Modules.%s" % modulename,
                                fromlist=[modulename])
            if modulename in dir(module):
                nickname = modulename.lower()
                modules[nickname] = module.__dict__[modulename]


load_modules()
