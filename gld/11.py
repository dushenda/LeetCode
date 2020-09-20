#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@ide        : PyCharm
@project    : LeetCode
@file       : 11.py
@author     : CALIBRATION
@time       : 2020/9/16 19:39
@description: None
"""
# def testfun(num):
#     try:
#         if num==0: raise ValueError('参数错误')
#         elif num> 0: print('A')
#         else: print('B')
#         return num
#     except Exception as e:
#         print(e)
# print(testfun(100))
# print(testfun(0))

# class Parent:
#     def display(self):
#         print("Parent")
#
# class Child(Parent):
#     def display(self):
#         print('Child')
#
# c = Child()
# super(Child,c).display()


# class Animal:
#     type=""
#     age = 0
#     __weight=0
#     def __init__(self,n,a,w):
#         self.type=n
#         self.age=a
#         self.__weight=w
#
#     def eat(self):
#         print(self.type,self.age)
#
# class Bird(Animal):
#     grade = ""
#     def __init__(self,n,a,w,g):
#         Animal.__init__(self,n,a,w)
#         self.grade = g
#     def eat(self):
#         print(self.type,self.age,self.grade)
#
# class Eagle():
#     flag = ""
#     type = ""
#
#     def __init__(self,n,t):
#         self.type = n
#         self.flag = t
#     def eat(self):
#         print(self.type,self.flag)
#
# class Demo(Eagle,Bird):
#     a = ""
#     def __init__(self,n,a,w,g,t):
#         Bird.__init__(self,n,a,w,g)
#         Eagle.__init__(self,n,t)
#
# test = Demo("a",1,2,3,"b")
# test.eat()

# str = "abcdefg"
# print(str[3:5])

# import threading
# import time
# def run(n):
#     print("task",n)
#     time.sleep(1)
#     print('A')
#     time.sleep(1)
#     print("B")
#     time.sleep(1)
#     print('C')
# t = threading.Thread(target=run,args=("t1",))
# t.setDaemon(True)
# t.start()
# t.join()
# print('end')

# def sumofdigits(*args):
#     x = 0
#     for i in args:
#         x+=i*2
#         return x
# print(sumofdigits(1,2,3))

# print(list(map(str,[10,20,30])))

# def foo(x,y):
#     try:
#         res = x/y
#         print("try")
#     except ZeroDivisionError:
#         print("except")
#     else:print("else")
#     finally:print("finally")
# foo(2,1)

class Father(object):
    pass
class Child(Father):
    pass
c = Child()
per = Father()
print(isinstance(c,per))
print(isinstance(per,c))