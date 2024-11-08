# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
* 游戏开始，初始状态下用户和电脑都有 100 分，赢一局+10 分，输一局-10 分。
* 当用户为 0 分时，游戏结束，提示游戏结束，比赛输了
* 当用户为 200 分时，游戏结束，提示游戏结束，赢得比赛、每轮比赛都输出当前的分数
* 1 代表剪刀 2 代表石头 3 代表布
'''
##自己编写的逻辑
# import random
# user=100
# computer=100
# n=0
#
# while True:
#     userrandom = random.randint(1, 3)
#     computerrandom = random.randint(1, 3)
#     if user==0:
#         print('游戏结束，电脑胜出')
#         break
#     if user==200:
#         print('游戏结束，用户胜出')
#         break
#     if userrandom==1:
#         if computerrandom==1:
#             pass
#         if computerrandom==2:
#             user=user-10
#             computer=computer+10
#         if computerrandom==3:
#             user=user+10
#             computer=computer-10
#     if userrandom==2:
#         if computerrandom==1:
#             user = user + 10
#             computer = computer - 10
#         if computerrandom==2:
#             pass
#         if computerrandom==3:
#             user = user - 10
#             computer = computer + 10
#     if userrandom==3:
#         if computerrandom==1:
#             user = user - 10
#             computer = computer + 10
#         if computerrandom==2:
#             user = user + 10
#             computer = computer - 10
#         if computerrandom==3:
#             pass
#     n=n+1
#     print(f'游戏为第{n}轮')
# ai给出优化后的逻辑
import random

user = 100
computer = 100
n = 0

# 定义得分规则
rules = {
    (1, 1): (0, 0),
    (1, 2): (-10, 10),
    (1, 3): (10, -10),
    (2, 1): (10, -10),
    (2, 2): (0, 0),
    (2, 3): (-10, 10),
    (3, 1): (-10, 10),
    (3, 2): (10, -10),
    (3, 3): (0, 0)
}

while True:
    userrandom = random.randint(1, 3)
    computerrandom = random.randint(1, 3)

    # 根据规则调整分数
    user_change, computer_change = rules[(userrandom, computerrandom)]

    user += user_change
    computer += computer_change

    # 检查结束条件
    if user <= 0:
        print('游戏结束，电脑胜出')
        break
    elif user >= 200:
        print('游戏结束，用户胜出')
        break

    n += 1
    print(f'游戏为第{n}轮，用户分数: {user}, 电脑分数: {computer}')

# 合并两个有序列表 list1=[1,2,5,7] list2=[3,4,6,8] 最终输出结果[1,2,3,4,5,6,7,8]

list1=[1,2,5,7,10]
list2=[3,4,6,8,9]
list3=[]

for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i]< list2[j]:
            if  list1[i] not in list3 :
                list3.append(list1[i])
        elif list1[i]>list2[j] and list2[j] not in list3:
            list3.append(list2[j])
##剩下的元素放进去
for i in list1:
    if i not in list3:
        list3.append(i)
for j in list2:
    if j not in list3:
        list3.append(j)
print(list3)