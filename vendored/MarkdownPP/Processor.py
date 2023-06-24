# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys

if sys.version_info[0] != 2:
    basestring = str


class Processor:
    """
    Framework for allowing modules to modify the input data as a set of
    transforms. Once the original input data is loaded, the preprocessor
    iteratively allows Modules to inspect the data and generate a list of
    Transforms against the data.  The Transforms are applied in descending
    order by line number, and the resulting data is used for the next pass.
    Once all modules have transformed the data, it is ready for writing out
    to a file.
    """

    data = []
    transforms = {}
    modules = []

    def register(self, module):
        """
        This method registers an individual module to be called when processing
        """
        self.modules.append(module)

    def input(self, file):
        """
        This method reads the original data from an object following
        the file interface.
        """
        self.data = file.readlines()

    def process(self):
        """
        This method handles the actual processing of Modules and Transforms
        """
        self.modules.sort(key=lambda x: x.priority)

        for module in self.modules:
            transforms = module.transform(self.data)
            transforms.sort(key=lambda x: x.linenum, reverse=True)

            for transform in transforms:
                linenum = transform.linenum

                if isinstance(transform.data, basestring):
                    transform.data = [transform.data]

                if transform.oper == "prepend":
                    self.data[linenum:linenum] = transform.data

                elif transform.oper == "append":
                    self.data[linenum+1:linenum+1] = transform.data

                elif transform.oper == "swap":
                    self.data[linenum:linenum+1] = transform.data

                elif transform.oper == "drop":
                    self.data[linenum:linenum+1] = []

                elif transform.oper == "noop":
                    pass

    def output(self, file):
        """
        This method writes the resulting data to an object following
        the file interface.
        """
        file.writelines(self.data)
