#1、readline和readlines区别
#read以及参数用法
with open('./123.txt','r') as f :
    #read()方法是读取所有文件内容，适合处理文件内容较小的数据场景
    re=f.read()
    print(re)

    # 将光标重置到文件的开头,因为在第一次读取文件时，光标已经移动到末尾，如果不重置光标会导致下面打印是空数据
    f.seek(0)
    ##加入了参数之后代表读取全文的前五个字符，注意换行符也占了一个字符
    re1=f.read(10)

    print('##############')
    print(re1)
#readline以及参数用法
with open('./123.txt','r') as f :
    #readline()方法是读取文件的每一行,返回字符串但是会带有\n换行符所以在处理数据时最好去除掉
    re=f.readline()
    print(re.strip())
    re=f.readline()
    print(re.strip())
    # 将光标重置到文件的开头,因为在第一次读取文件时，光标已经移动到末尾，如果不重置光标会导致下面打印是空数据
    f.seek(0)
    #引入参数之后代表读取该行的前多少个字符，当参数为空白，负数，超出索引值 返回该行全部数据并不会报错
    re = f.readline(500)
    print(re.strip())

###输出结果
# ldlsllls

#lfdkds

#readlines以及参数用法
with open('./123.txt','r') as p :
    #readlines()方法是读取文件的所有行，返回一个列表数据，每个列表元素是一行的数据，但是依然注意\n换行符的处理
    #strip()方法会去除字符串中的空白字符其中包含 空格，制表符，换行符，也可以增加参数用单引号引起来 对指定的去除
    rep=p.readlines()
    print(rep)
    for line in rep:
        print(line.strip())
    ##带参数后就是
    print('带参数之后数据')
    # 输出结果为：['ldlsllls\n', 'lfdkds\n', 'lfldkadksa;djfadlsafdsa\n', 'fjdlajdlsjladf']
    p.seek(0)
    ##代表所有行的前多少个字符，当字符值正好落在某行上时，返回该行之前所有行的数据以列表返回
    rep=p.readlines(10)
    print(rep)
    for line in rep:
        print(line.strip())
    ##输出结果['ldlsllls\n', 'lfdkds\n']



##write() with上下文管理器 比不写会更安全因为自带关闭文件功能，用户不需要关心什么时候.close
with open('234.txt','w') as ww:
    ##该方法每次只写入一行数据，注意当写入的数据重复时，会覆盖原有数据
    ww.write('1245454354\n')
    ww.write('111111111')
##如果重复数据不想被覆盖那需要更改open里的参数‘a’改成追加模式
with open('335.txt','a') as ww:
    ##该方法每次只写入一行数据，注意当写入的数据重复时，会覆盖原有数据
    ww.write('1245454354\n')
#运行俩次后的结果
#1245454354
#1245454354

##writelines()方法使用

with open('432.txt','w') as ws:
    ##该方法每次只写入一行数据，注意当写入的数据重复时，会覆盖原有数据
    lst=['用例名称','前置条件','执行步骤','预期结果','实际结果']
    lst1=[x+',' for x in lst[:-1]]+[lst[-1]]
    ws.writelines(lst1)