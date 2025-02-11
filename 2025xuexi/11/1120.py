# -*- coding: utf-8 -*-
"""
#Author:changchuchu
@File ：1120.py
@Time ： 2024/11/20 13:12
"""
# write() 方法用于将字符串写入文件。它不接受任何形式的数字或列表，只能写入字符串。
# 它不会在写入的字符串后添加换行符（\n），如果需要换行，必须在字符串中包含。
# f=open('ccc.txt','w')
# f.write('hello,world')
# f.close()

# writelines() 方法用于将一个字符串序列写入文件。这个序列可以是一个列表或元组，其中每个元素都是一个字符串。
# 与 write() 类似，writelines() 也不会自动添加换行符，如果需要换行，每个字符串元素必须
# lines=['chuchu\n','test\n']
# f=open('dh.txt','w')
# f.writelines(lines)
# f.close()

# lines=('chuchu\n','test\n')
# f=open('dhyz.txt','w')
# f.writelines(lines)
# f.close()

# read() 方法用于从文件中读取内容。如果没有指定 size 参数，它会读取整个文件内容直到文件末尾，并返回一个字符串。
# 如果指定了 size 参数，它会读取指定数量的字符。
# f=open('ccc.txt','r')
# line=f.read(2)
# print(line)
# f.close()

# readline() 方法用于从文件中读取一行内容。如果没有指定 size 参数，它会读取一行直到换行符，并返回该行内容。
# 如果指定了 size 参数，它会读取指定数量的字符，但不会超过换行符。
# f=open('dh.txt','r')
# line=f.readline()
# print(line)
# f.close()


# readlines() 方法用于从文件中读取所有行，并返回一个包含每行内容的列表。如果没有指定 size 参数，它会读取整个文件。
# 如果指定了 size 参数，它会读取指定数量的行。
# f=open('dh.txt','r')
# line=f.readlines()
# print(line)
# f.close()
