import requests
from bs4 import BeautifulSoup
import os

def fetch_html(url, headers):
    """Fetch HTML content from a given URL with specified headers."""
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response
    except requests.RequestException as e:
        print(f"Error fetching HTML from {url}: {e}")
        return None

def parse_title(soup):
    """Parse the book title from the BeautifulSoup object."""
    try:
        title_tag = soup.find('h1', class_='bt')
        if title_tag:
            return title_tag.text
        else:
            raise ValueError("Title tag not found")
    except Exception as e:
        print(f"Error parsing title: {e}")
        return None

def parse_chapters(soup, base_url):
    """Parse chapter links from the BeautifulSoup object."""
    try:
        chapters = []
        for zj in soup.select('.contbox.cont11 > .list a'):
            zj_text = zj.text
            zj_url = base_url + zj['href']
            chapters.append((zj_text, zj_url))
        return chapters
    except Exception as e:
        print(f"Error parsing chapters: {e}")
        return []

def fetch_and_save_chapter(url, headers, title):
    """Fetch and save a chapter's content to a file."""
    try:
        response = fetch_html(url, headers)
        if response is None:
            return

        detail_bs = BeautifulSoup(response.text, 'lxml')
        detail_title = detail_bs.find('title').text
        detail_text = detail_bs.find('div', class_='text p_pad').text

        path = f'./{title}/{detail_title}.txt'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(detail_title + '\n' + detail_text)
        print(f'{detail_title}的详情内容已爬取完成')
    except Exception as e:
        print(f'爬取章节信息过程中出现错误,错误信息如下:{e}')

def main():
    url = 'https://www.shicimingju.com/book/hongloumeng.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    base_url = url.split('/')[0] + '//' + url.split('/')[2]

    html = fetch_html(url, headers)
    if html is None:
        return

    bs = BeautifulSoup(html.text, 'lxml')
    title = parse_title(bs)
    if title is None:
        return

    if not os.path.exists(f'./{title}'):
        os.mkdir(f'./{title}')

    chapters = parse_chapters(bs, base_url)
    for _, zj_url in chapters:
        fetch_and_save_chapter(zj_url, headers, title)

    print(f'爬虫爬取结束请前往{title}目录中查看数据')

if __name__ == "__main__":
    main()