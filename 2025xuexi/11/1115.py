# -*- coding: utf-8 -*-
"""
#Author:changchuchu
@File ：1115.py
@Time ： 2024/11/15 14:47
"""
# data = {
#     'a': [1, 2, 3],
#     'b': [4, 5, 6],
#     'c': {'d': 7, 'e': 8}
# }



# 输出：[1, 2, 3, 4, 5, 6, 7, 8]
# result=[]
# def create_list(data):
#     for d in data.values():
#         print(d)
#         print(type(d))
#         if isinstance(d,list):
#             result.extend([i for i in d])
#         else:
#             result.extend([i for i in d.values()])
#     return result
# print(create_list(data))

def get_leaf_values(data):
    leaf_values = []

    def _get_leaf_values_recursive(item):
        if isinstance(item, list):
            for sub_item in item:
                _get_leaf_values_recursive(sub_item)
        elif isinstance(item, dict):
            for value in item.values():
                _get_leaf_values_recursive(value)
        else:
            leaf_values.append(item)

    _get_leaf_values_recursive(data)
    return leaf_values


data = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': {'d': 7, 'e': 8}
}

print(data.values())

leaf_values = get_leaf_values(data)
print(leaf_values)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8]
