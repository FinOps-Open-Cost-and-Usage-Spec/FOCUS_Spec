# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from MarkdownPP import Modules
from .Processor import Processor


class MarkdownPP:
    """
    Simplified front-end interface for the Processor and Module systems.
    Takes input and output file names or objects, and a list of module names.
    Automatically executes the preprocessor with the requested modules.
    """

    def __init__(self, input=None, output=None, modules=None):
        pp = Processor()

        for name in [m.lower() for m in modules]:
            if name in Modules.modules:
                module = Modules.modules[name]()
                pp.register(module)

        pp.input(input)
        pp.process()
        pp.output(output)
