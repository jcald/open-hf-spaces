#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import os
from colorama import init, Fore, Style

def tree(directory, level=0):
    for root, dirs, files in os.walk(directory):
        print('│   ' * level + '├──', os.path.basename(root), sep='')
        for file in files:
            print('│   ' * level + '│   ├──', file)
        for dir in dirs:
            tree(os.path.join(root, dir), level+1)

if __name__ == '__main__':
    init()
    directory = input("Ingrese el directorio: ")
    tree(directory)
