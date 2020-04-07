import requests
import json
import os


class DoubanSpider:
    def __init__(self):
        self.start_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        self.proxies = {
            "http": "http://113.103.226.174"
        }
        self.save_path = "g:/豆瓣/豆瓣高分/"
        folder = os.path.exists(self.save_path)
        if not folder:
            os.makedirs(self.save_path)
            print("create folder{}")
        else:
            print("it exist!")

    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subjects"]
        return content_list

    def save_content_list(self, content_list):
        with open(self.save_path + "豆瓣.txt", "a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

    def parse_url(self, url):
        print(url)
        return requests.get(url, headers=self.headers, proxies=self.proxies).content.decode()

    def run(self):  # 实现主要逻辑
        page_index = 0
        while True:
            url = self.start_url.format(page_index)
            json_str = self.parse_url(url)
            content_list = self.get_content_list(json_str)
            self.save_content_list(content_list)
            if len(content_list) < 20:
                break
            page_index += 20

if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()