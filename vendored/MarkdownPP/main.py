#!/usr/bin/env python

# Copyright (C) 2010 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import sys
import MarkdownPP

import os
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


# Terminal output ANSI color codes
class colors:
    BLUE = '\033[36;49;22m'
    MAGB = '\033[35;49;1m'
    GREEN = '\033[32;49;22m'
    NORMAL = '\033[0m'


# Custom event handler for watchdog observer
class MarkdownPPFileEventHandler(PatternMatchingEventHandler):
    # Look for .mdpp files
    patterns = ["*.mdpp"]

    def process(self, event):
        modules = MarkdownPP.modules.keys()
        mdpp = open(event.src_path, 'r')

        # Output file takes filename from input file but has .md extension
        md = open(os.path.splitext(event.src_path)[0]+'.md', 'w')
        MarkdownPP.MarkdownPP(input=mdpp, output=md, modules=modules)

        # Logs time and file changed (with colors!)
        print(time.strftime("%c") + ":",
              colors.MAGB + event.src_path,
              colors.GREEN + event.event_type,
              "and processed with MarkdownPP",
              colors.NORMAL)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


def main():
    # setup command line arguments
    parser = argparse.ArgumentParser(description='Preprocessor for Markdown'
                                     ' files.')

    parser.add_argument('FILENAME', help='Input file name (or directory if '
                        'watching)')

    # Argument for watching directory and subdirectory to process .mdpp files
    parser.add_argument('-w', '--watch', action='store_true', help='Watch '
                        'current directory and subdirectories for changing '
                        '.mdpp files and process in local directory. File '
                        'output name is same as file input name.')

    parser.add_argument('-o', '--output', help='Output file name. If no '
                        'output file is specified, writes output to stdout.')
    parser.add_argument('-e', '--exclude', help='List of modules to '
                        'exclude, separated by commas. Available modules: '
                        + ', '.join(MarkdownPP.modules.keys()))
    args = parser.parse_args()

    # If watch flag is on, watch dirs instead of processing individual file
    if args.watch:
        # Get full directory path to print
        p = os.path.abspath(args.FILENAME)
        print("Watching: " + p + " (and subdirectories)")

        # Custom watchdog event handler specific for .mdpp files
        event_handler = MarkdownPPFileEventHandler()
        observer = Observer()
        # pass event handler, directory, and flag to recurse subdirectories
        observer.schedule(event_handler, args.FILENAME, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    else:
        mdpp = open(args.FILENAME, 'r')
        if args.output:
            md = open(args.output, 'w')
        else:
            md = sys.stdout

        modules = list(MarkdownPP.modules)

        if args.exclude:
            for module in args.exclude.split(','):
                if module in modules:
                    modules.remove(module)
                else:
                    print('Cannot exclude ', module, ' - no such module')

        MarkdownPP.MarkdownPP(input=mdpp, output=md, modules=modules)

        mdpp.close()
        md.close()


if __name__ == "__main__":
    main()
