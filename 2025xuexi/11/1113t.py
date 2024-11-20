# -*- coding: utf-8 -*-
"""
#Author:changchuchu
@File ：1113t.py
@Time ： 2024/11/13 13:24
"""
import json

students_data = '''
{
    "students": [
        {"id": 1, "name": "Alice", "grade": "A"},
        {"id": 2, "name": "Bob", "grade": "B"}
    ]
}
'''

grades_data = '''
{
    "grades": [
        {"student_id": 1, "subject": "Math", "score": 95},
        {"student_id": 1, "subject": "Science", "score": 90},
        {"student_id": 2, "subject": "Math", "score": 85}
    ]
}
'''
# 方法一：
s_data=json.loads(students_data)
g_data=json.loads(grades_data)

total=[]
student={}

for s in s_data['students']:
    # print(s)
    u = {}



    student=s
    score={}
    for g in g_data['grades']:

        if s['id']==g['student_id']:
            # a=s['id']

            score[g['subject']]=g['score']
    print(score)
    student['score']=score
    # print(u)

    total.append(student)
print(total)

# 方案二
# 解析 JSON 数据
students = json.loads(students_data)["students"]
grades = json.loads(grades_data)["grades"]
print(students)
print(grades)

student_map= {student['id']: student for student in students}
print(student_map)
for g in grades:
    student_id = g.pop('student_id')
    if student_id in student_map:
        if 'grades' not in student_map[student_id]:
            student_map[student_id]['grades']=[]

        student_map[student_id]['grades'].append(g)
print(student_map)