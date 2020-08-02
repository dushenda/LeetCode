#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : read.py
@author     : CALIBRATION
@time       : 2020/7/21 16:18
@description: None
"""


def copy(read_path, write_path):
    with open(read_path, 'r') as f:
        with open(write_path, 'w') as fw:
            fw.write(f.read())
        print(f)
    return


def main():
    copy('./POSCAR-00002.txt', 'output.txt')


if __name__ == '__main__':
    main()
