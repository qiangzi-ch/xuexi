# -*- coding: utf-8 -*-
"""
#Author:changchuchu
@File ：1119.py
@Time ： 2024/11/19 16:58
"""
x=2
print(type(x))
def f():
    print(type(str(x)))
    x=3
    print(type(x))
f()

# 程序运行报错