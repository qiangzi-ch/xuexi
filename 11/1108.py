# -*- coding: utf-8 -*-
"""
#Author:changchuchu
@File ：1107_1.py
@Time ： 2024/11/7 16:23
"""
# print(sum(range(1,101)))

# list1=[1,2,5,7]
# list2=[3,4,6,8]
# list1.extend(list2)
#
# list4=sorted(list1,reverse=False)
# print(list4)

# print(sorted(list1+list2,reverse=False))
# list1=[1,2,5,7]
# list2=[3,4,6,8]
# list3=list1+list2
# print(list3)

# for i  in  range(len(list3)-1):
#     for j in range(len(list3)-i-1):
#
#         if list3[j]>list3[j+1]:
#             list3[j],list3[j+1]=list3[j+1],list3[j]


list1=[1,2,5,7]
list2=[3,4,6,8]
list3=list1+list2
print(list3)
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bubble_sort_recursive(arr, n-1)
    return arr

print(bubble_sort_recursive(list3))
