import requests
from bs4 import BeautifulSoup
import os
url='https://www.shicimingju.com/book/hongloumeng.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
base_url=url.split('/')[0]+'//'+url.split('/')[2]
print(base_url)
print(url)
html=requests.get(url=url,headers=headers)
##设置编码格式
html.encoding='utf-8'

bs=BeautifulSoup(html.text,'lxml')
##获取书籍的文本名字,因class是关键字所以这里需要再class后面增加_来获取classname参数
title=bs.find('h1',class_='bt').text
##获取
print(title)
if not os.path.exists(f'./{title}'):
    os.mkdir(f'./{title}')

##书籍的章节内容获取,注意类名中间的空格 需要用点代替
zjs=bs.select('.contbox.cont11 >.list a')
for zj in zjs:
    try:
        #获取章节的内容
        zj_text=zj.text
        #获取对应章节的跳转链接
        zj_url=base_url+zj['href']

        detail=requests.get(url=zj_url,headers=headers)
        detail.encoding=detail.apparent_encoding  ##自动转换格式不需要人工指定

        ##lxml是一个强大的解析器 可以处理复杂的 HTML 和 XML 结构，且对不规范的 HTML 也有很好的容错性
        detail_bs=BeautifulSoup(detail.text,'lxml')
        detail_title=detail_bs.find('title').text
        #detail_text=detail_bs.select('.contbox.textinfor > .text.p_pad p')
        detail_text=detail_bs.find('div',class_='text p_pad').text

        #print(detail_text)
        path=f'./{title}/'+detail_title+'.txt'
        with open(path,'w',encoding='utf-8') as f:
            f.write(detail_title+'\n'+detail_text)
        print(f'{detail_title}的详情内容已爬取完成')
    except Exception as e:
        print(f'爬取章节信息过程中出现错误,错误信息如下:{e}')
        break

else:
    print(f'爬虫爬取结束请前往{title}目录中查看数据')