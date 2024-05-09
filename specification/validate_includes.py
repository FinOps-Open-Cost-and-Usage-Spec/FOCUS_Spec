#!/usr/bin/env python3
import argparse
from os import listdir
import sys
import re
from os.path import isfile, join, basename, normpath

def validate_includes(keyname):
    """
    This function will validate that a folder has not got any missing 
    includes in its related mdpp file. The final foldername in the path and 
    the mdpp template must match in name (e.g. dimension and dimension.mdpp).
    This function will find all *.md files in the directory and the !INCLUDE 
    lines in the mdpp file. Then confirm they are matching. Function will 
    exit() if they do not match in order to cause GitHub Actions to fail builds
    if they don't match.

    Args:
        keyname: The folder name to run the validation inside (final folder 
        must match the name of the mdpp template).
    """
    base_folder = basename(normpath(keyname))
    template_filename = f'{keyname}/{base_folder}.mdpp'
    include_match_pattern = re.compile('!INCLUDE \"([^/]*.md)\".*')

    found_includes = []
    with open(template_filename, 'r') as f:
        for line in f.readlines():
            match = include_match_pattern.search(line)
            if match:
                found_includes.append(match.group(1))

    required_includes = [includefile for includefile in listdir(keyname) if includefile.endswith('.md') and isfile(join(keyname, includefile))]
    missing_from_template = list(set(required_includes).difference(set(found_includes)))
    missing_from_folder = list(set(found_includes).difference(set(required_includes)))
    if missing_from_template:
        print('The following files:', missing_from_template, f'are missing from the template {template_filename}')
        sys.exit(1)
    if missing_from_folder:
        print('The following files:', missing_from_folder, f'are missing from the folder referenced by {template_filename}')
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog='validate_includes',
                        description='This script will validate the list of *.md files and !INCLUDES match for a folder')

    parser.add_argument('keyname')
    args = parser.parse_args()
    validate_includes(args.keyname)
