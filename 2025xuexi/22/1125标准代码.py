from bs4 import BeautifulSoup
import requests,os

url = "https://www.shicimingju.com/book/hongloumeng.html"
#      https://www.shicimingju.com/book/hongloumeng/1.html
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

if not os.path.exists('./notebook'):
    os.mkdir('./notebook')

main_responce = requests.get(url=url,headers=headers)
main_responce.encoding = main_responce.apparent_encoding        # 自动转码

main_responce = main_responce.text


main_soup = BeautifulSoup(main_responce,'lxml')
main_selects = main_soup.select('.contbox.cont11 >.list a')

for main_titles in main_selects:
    main_title = main_titles.text
    print(main_title)

    main_url = "https://www.shicimingju.com"
    parts_url = main_titles['href']
    detail_url = main_url+parts_url
    print(detail_url)

    #detail_responce = requests.get(url=detail_url,headers=headers).text
    detail_responce = requests.get(url=detail_url,headers=headers)
    detail_responce.encoding=detail_responce.apparent_encoding
    #print(detail_responce.text)
    detail_responce=detail_responce.text

    detail_soup = BeautifulSoup(detail_responce,'lxml')
    detail_find = detail_soup.find('div',class_='text p_pad')
    detail_text = detail_find.text.replace('    ','\n')
    print(detail_text)

    path = './notebook/' + main_title+'.txt'
    with open(path,'w',encoding='utf-8') as f:
        f.write(main_title+':\n'+detail_text)

    print(f'{main_title}   爬取完成...')
print("全部爬取完成。。。")
