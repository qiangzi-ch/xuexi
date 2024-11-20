# 第六题：字典操作描述： 编写一个函数 word_count，该函数接受一个字符串 s 作为输入，返回一个字典，键是字符串中的单词，值是每个单词出现的次数。示例如下
# s = "hello world hello"
# output: {'hello': 2, 'world': 1}

sss = "hello world hello"
output={}
def word_count(sss):
    sss = "hello world hello"
    sss_list=sss.split()
    for ss in sss_list:
        num=sss_list.count(ss)
        output[ss]=num

    print(output)


word_count(sss)