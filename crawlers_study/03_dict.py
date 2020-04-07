# coding=utf-8
import requests
import json


class Dict:
    def __init__(self, url, data, header):
        self.url = url
        self.data = data
        self.header = header

    def send_post(self, url, data):
        return requests.post(url=url, data=data, headers=header).content.decode()

    def run(self):
        # 1.发送post请求
        result = self.send_post(self.url, self.data)
        print(result)


if __name__ == '__main__':
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    url = "http://fy.iciba.com/ajax.php?a=fy"
    data = {
        "f": "auto",
        "t": "auto",
        "w": "今天去哪里呀"
    }
    dicts = Dict(header=header, data=data, url=url)
    dicts.run()

    s = "\u6765\u81ea\u673a\u5668\u7ffb\u8bd1\u3002"
    