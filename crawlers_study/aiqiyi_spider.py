import requests
import json
import os
from lxml import etree


class DoubanSpider:
    def __init__(self):
        self.start_url = "https://list.iqiyi.com/www/1/-------------8-{}-1-iqiyi--.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        self.proxies = {
            "http": "http://113.103.226.174"
        }
        self.save_path = "g:/爱奇艺/爱奇艺高分/"
        folder = os.path.exists(self.save_path)
        if not folder:
            os.makedirs(self.save_path)
            print("create folder{}")
        else:
            print("it exist!")

    def get_content_list(self, html):
        tmlData = etree.HTML(html)
        nameList = tmlData.xpath('//p[@class="main"]/a/@title')
        gradeList = tmlData.xpath('//p[@class="main"]/span/text()')

        str = ""
        for name in  nameList:
            print(name)





    def save_content_list(self, content_list):
        with open(self.save_path + "爱奇艺.txt", "a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

    def parse_url(self, url):
        print(url)
        return requests.get(url, headers=self.headers, proxies=self.proxies).content

    def run(self):  # 实现主要逻辑
        page_index = 1
        while True:
            url = self.start_url.format(page_index)
            html = self.parse_url(url)
            content_list = self.get_content_list(html)
            self.save_content_list(content_list)
            page_index += 1


if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()


