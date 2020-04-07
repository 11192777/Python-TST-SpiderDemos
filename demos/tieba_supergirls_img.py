# coding=utf-8
import requests
from lxml import etree
import os
from retrying import retry
import hashlib

m = hashlib.md5()

class SuperGirlsSpilder:
    def __init__(self):
        self.start_url = ""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        self.proxies = {
            "http": "http://119.120.183.197"
        }
        self.name = 1

        self.save_path = "g:/百度贴吧/supergirl/"
        folder = os.path.exists(self.save_path)
        if not folder:
            os.makedirs(self.save_path)
            print("create folder{}")
        else:
            print("it exist!")

    def get_big_png(self, content):
        html = etree.HTML(content.replace('<!--', '"').replace('-->', '"'))
        return html.xpath('//li[@class="shown"]/a/img/@src')

    def get_url(self, page_no):
        return self.start_url.format(page_no)

    def parse_url(self, url):
        response = requests.get(url=url, headers=self.headers, proxies=self.proxies)
        return response.content.decode()

    def down_imgs(self, img_list):
        for img_url in img_list:
            with open(img_url.split("/")[5], "wb") as f:
                print(img_url.split("/")[6])
                response = requests.get(img_url,headers=self.headers, proxies=self.proxies)
                # response = parse_url(img_url)
                if response is not None:
                    f.write(response.content)
                else:
                    pass
                self.name += 1

    def run(self):
        page_index = 1

        while True:
            url = self.get_url(page_index)
            page_index += 1
            content = self.parse_url(url)
            img_list = self.get_big_png(content)
            self.down_imgs(img_list)


if __name__ == '__main__':
    spilder = SuperGirlsSpilder()
    spilder.run()
