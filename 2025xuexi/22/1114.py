# 第7题：常见json处理练习题 合并学生信息与成绩信息

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

import json

json_data1=json.loads(students_data)
json_data2=json.loads(grades_data)
print(json_data1['students'])
for i in json_data1['students']:
    i['grades']=[]
    for j in json_data2['grades']:
        if 'student_id'in j and i['id']==j['student_id'] :
            j.pop('student_id',None)
            i['grades'].append(j)

print(json.dumps(json_data1))


##附加题：
list1 = [{'name': 'customerReturnOrderNo-detail', 'value': '72'}, {'name': 'item', 'value': '40'}]
list2 = [{'name': 'order-detail', 'value': '38'}, {'name': 'item', 'value': '3100'}]
# [{'name': 'item', 'cpm': '40', 'avg': '3100'},
# {'name': 'customerReturnOrderNo-detail', 'cpm': '72', 'avg': None},
# {'name': 'order-detail', 'cpm': None, 'avg': '38'}]
data=[]

for i in list1:
    dict1 = {}
    dict1['name']=i['name']
    dict1['cpm']=i['value']
    data.append(dict1)

for j in list2:
    dict2 = {}
    dict2['name'] = j['name']
    dict2['avg'] = j['value']
    data.append(dict2)
print(data,'534534534534')
dict123={}
for u in data:
    name = u.get('name',0)
    cpm = u.get('cpm', 0)
    avg = u.get('avg', 0)
    if name not in dict123:
        dict123[name]={'name':name,"cpm":cpm,"avg":avg}
    else:
        if cpm!=0:
            dict123[name]['cpm']=cpm
        if avg!=0:
            dict123[name]['avg'] = avg
print(dict123,'678686789685342')
res=list(dict123.values())

print(res,'GYUTUYIGJGYUOIGUI##########################')







list1 = [{'name': 'customerReturnOrderNo-detail', 'value': '72'}, {'name': 'item', 'value': '40'}]
list2 = [{'name': 'order-detail', 'value': '38'}, {'name': 'item', 'value': '3100'}]

# 创建字典来存储 list1 和 list2 中的值
dict1 = {item['name']: item['value'] for item in list1}
dict2 = {item['name']: item['value'] for item in list2}

# 获取所有唯一的 name
all_names = set(dict1.keys()).union(set(dict2.keys()))

# 合并数据
result = []
for name in all_names:
    cpm = dict1.get(name)
    avg = dict2.get(name)
    result.append({'name': name, 'cpm': cpm, 'avg': avg})

# 打印结果
print(result)



####第三种方法
list1 = [{'name': 'customerReturnOrderNo-detail', 'value': '72'}, {'name': 'item', 'value': '40'}]
list2 = [{'name': 'order-detail', 'value': '38'}, {'name': 'item', 'value': '3100'}]

# 创建字典来存储最终结果
result_dict = {}

# 处理 list1
for item in list1:
    name = item['name']
    value = item['value']
    if name not in result_dict:
        result_dict[name] = {'name': name, 'cpm': value, 'avg': None}
    else:
        result_dict[name]['cpm'] = value

# 处理 list2
for item in list2:
    name = item['name']
    value = item['value']
    if name not in result_dict:
        result_dict[name] = {'name': name, 'cpm': None, 'avg': value}
    else:
        result_dict[name]['avg'] = value


print(result_dict)
# 将结果字典转换为列表
result_list = list(result_dict.values())

# 打印结果
print(result_list)
