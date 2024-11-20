data = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': {'d': 7, 'e': 8}
}

#输出：[1, 2, 3, 4, 5, 6, 7, 8]
list_output=[]
for value in data.values():
    if isinstance(value, list):
        for i in value:
            list_output.append(i)
    elif isinstance(value,dict):
        for value2 in value.values():
            list_output.append(value2)
print(list_output)