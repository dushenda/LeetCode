#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeeCode
@file       : test.py
@author     : CALIBRATION
@time       : 2020/5/22 17:11
@description: None
"""


class Rectangle:
    a = 0  # 静态数据，可以通过类名直接访问

    def __init__(self, h, w):
        self.b = 5  # 成员数据，只能通过对象访问
        self._width = w
        self._height = h
        self._area = self._width * self._height

    def __str__(self):
        return "width:{0}\nheight:{1}\narea:{2}".format(self._width, self._height, self._area)

    def __repr__(self):
        return "area%s" % self._area

    def __le__(self, other):
        return self._area <= other._area

    def cal_area(self):
        return self._area


import time


# 装饰器
def tick(func):
    def inner(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        return {"time": "%.8lf" % (end - start), "result": "{}".format(res)}

    return inner


@tick
def fib(v):
    a, b = 0, 1
    for i in range(2, v + 1):
        a, b = b, a + b
    return b


import netrc


def t1():
    a = netrc.netrc()
    s = a.authenticators("202.127.202.6")
    print(repr(a))


import datetime


def main():
    dt = datetime.datetime(year=2019, month=12, day=1)
    print(dt.strftime("%j"))


if __name__ == '__main__':
    main()
