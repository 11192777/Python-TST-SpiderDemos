# coding=utf-8
import requests
import os


class TiebaSpider:
    def __init__(self, tieba_name, save_path, tieba_total_num):
        self.tieba_total_num = tieba_total_num
        self.tieba_name = tieba_name
        self.save_path = save_path
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

    def get_url_list(self):  # 构造url列表
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format(i * 50))
        # return url_list
        return [self.url_temp.format(i * 50) for i in range(self.tieba_total_num)]

    def parse_url(self, url):  # 发送请求，获取响应
        print(url)
        response = requests.get(url=url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_no):  # 保存html字符串
        file_path = "{}/{}-第{}页.html".format(self.save_path, self.tieba_name, page_no)
        with open(file_path, "w", encoding="utf-8") as f:  # "lol-第i页.html"
            f.write(html_str)

    def run(self):  # 实现主要逻辑
        # 1.构造url列表
        url_list = self.get_url_list()
        # 2.遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.保存
            page_no = url_list.index(url) + 1
            self.save_html(html_str, page_no)  # 页码数


if __name__ == '__main__':
    save_path = "G:/百度贴吧/肖战"
    folder = os.path.exists(save_path)
    if not folder:
        os.makedirs(save_path)
        print("create folder{}")
    else:
        print("it exist!")
    tieba_spider = TiebaSpider(tieba_name="肖战", save_path=save_path, tieba_total_num=20)
    tieba_spider.run()
