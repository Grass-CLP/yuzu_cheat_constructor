#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3
#
# created by Lipson on 2022/12/30.
# email to LipsonChan@yahoo.com
#

import codecs
import os
import pathlib
import shutil
from typing import List


def write_epoch(name: str, d: str, context: List[str], sep: int):
    invalid = '<>:"/\\|?* []{}-\r\n'
    dir_name = context[0]
    for char in invalid:
        dir_name = dir_name.replace(char, '')
    dir_name = "#{:02d} {}".format(sep, dir_name)
    target_path = os.path.join(d, dir_name, 'cheats')
    os.makedirs(os.path.join(d, dir_name, 'cheats'), exist_ok=True)

    target = os.path.join(target_path, name + ".txt")
    print("write file: {}".format(target))
    with codecs.open(target, 'w', 'utf-8') as file:
        file.writelines(context)


def expand_txt(path: str, f: str):
    target = os.path.join(path, f)
    name = pathlib.Path(target).stem
    target_path = os.path.join(path, name)
    if os.path.exists(target_path):
        print("directory exist, delete: {}".format(name))
        shutil.rmtree(target_path, ignore_errors=True)

    os.makedirs(target_path, exist_ok=True)

    with codecs.open(target, 'r', 'utf-8') as file:
        content = file.readlines()

    epoch = list()
    sep = 0
    for line in content:
        if line[0] in ['[', '{']:
            if epoch:
                write_epoch(name, target_path, epoch, sep)
                epoch.clear()
                sep += 1
        epoch.append(line)


def list_txt(path: str):
    for f in os.listdir(path):
        target = os.path.join(path, f)
        if os.path.isfile(target) and pathlib.Path(target).suffix == ".txt":
            print("expand file: {}".format(f))
            expand_txt(path, f)
    pass


if __name__ == '__main__':
    list_txt(os.path.dirname(os.path.realpath(__file__)))
