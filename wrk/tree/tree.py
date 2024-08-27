#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import os
from colorama import init, Fore, Style

def tree(directory=None):
    """
    Recursively walks through a directory structure and prints it in a tree format.

    Args:
        directory (str, optional): The directory to start traversing. Defaults to None,
            in which case the user will be prompted for input.
    """

    if directory is None:
        directory = input("Ingrese el directorio (o deje en blanco para usar el directorio actual): ")
        if not directory:
            directory = os.getcwd()

    level = 0  # Initialize level for indentation

    for root, dirs, files in os.walk(directory):
        print('│   ' * level + '├──', os.path.basename(root), sep='')
        for file in files:
            print('│   ' * level + '│   ├──', file)
        for dir in dirs:
            tree(os.path.join(root, dir), level+1)  # Pass level for indentation

if __name__ == '__main__':
    init()
    tree()
