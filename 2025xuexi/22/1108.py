#第四题：list1=['a','b','v','234','654','po'] list2=['b','a','v','654','234']请用两种写法求出两个列表的交集并打印结果考察点set集合特性，函数推导式与普通写法算一种写法
#第一种方法:基本写法
list1=['a','b','v','234','654','po']
list2=['b','a','v','654','234']
list3=list1+list2
list4=[]
for i in list3:
    if list3.count(i)>1 and i not in list4:
        list4.append(i)
print(list4)
#第二种方法：利用set属性& 只有set才可以使用&代表取交集的意思
list1=['a','b','v','234','654','po']
list2=['b','a','v','654','234']
list3=set(list1)&set(list2)
print(list3)

#第三种方法：函数推导式
list1=['a','b','v','234','654','po']
list2=['b','a','v','654','234']
list3=[i for i in list1 if i in list2]
print(list3)