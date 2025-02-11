# -*- coding: utf-8 -*-
"""

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
# from collections import Counter
#
# def word_count(s:str)->dict:
#     return dict(Counter(s.split()))
# s = "hello world hello"
# print(word_count(s))

#方法三
def word_count(s:str)->dict:
    words=s.split()
    words_count={}
    for w in words:
        words_count[w]=words.count(w)

    return words_count

s = "hello world hello"
print(word_count(s))