# -*- coding: utf-8 -*-
"""
#Author:changchuchu
@File ：1112t.py
@Time ： 2024/11/13 11:03
"""
# s = "hello world hello"
# output: {'hello': 2, 'world': 1}

# 方法一

# def word_count(s:str)->dict:
#     s=s.split(' ')
#     print(s)
#
#     m = {}
#     for j in s:
#         if j in m:
#             print(m)
#             m[j]+=1
#         else:
#             m[j]=1
#     return m
# s = "hello world hello"
# print(word_count(s))

# 方法二
from collections import Counter

def word_count(s:str):
    return dict(Counter(s.split()))
s = "hello world hello"
print(word_count(s))

