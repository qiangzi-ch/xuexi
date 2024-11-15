# -*- coding: utf-8 -*-
"""
#Author:changchuchu
@File ：1115.py
@Time ： 2024/11/15 14:47
"""
data = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': {'d': 7, 'e': 8}
}



# 输出：[1, 2, 3, 4, 5, 6, 7, 8]
result=[]
def create_list(data):
    for d in data.values():
        print(d)
        print(type(d))
        if isinstance(d,list):
            result.extend([i for i in d])
        else:
            result.extend([i for i in d.values()])
    return result
print(create_list(data))

