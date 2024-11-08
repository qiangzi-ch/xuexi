# -*- coding: utf-8 -*-
"""

@File ：1108.py
@Time ： 2024/11/8 13:59
"""
from collections import Counter

list1=['a','b','v','234','654','po']
list2=['b','a','v','654','234']

#方法一：
# list3=list1+list2
# count=Counter(list3)
# print(count)
# list_qc=[]
# for k,v in count.items():
#     if v>1:
#         list_qc.append(k)
# print(list_qc)


#方法二：
list4=set(list1+list2)
list_qc=[]
for i in list4:
    if i in list1  and i in list2:
        list_qc.append(i)
print(list_qc)
