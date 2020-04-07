# coding=utf-8
import requests
import json
from pprint import pprint

proxies = {
    "http": "http://113.103.226.174"
}
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start=20"
response = requests.get(url, headers=headers, proxies=proxies)

json_str = response.content.decode()
json_str = json.loads(json_str)

# json.dumps能够吧python类型转换成json字符串
with open("douban.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(json_str,ensure_ascii=False, indent=4))


# with open("douban.json", "r", encoding="utf-8") as f:
#     ret2 = f.read()
#     print(json.loads(ret2))
#     print(type(json.loads(ret2)))

# json.loal提取类问文件对象中的数据
# with open("douban.json", "r", encoding="utf-8") as f:
#     ret3 = json.load(f)
#     print(ret3)
#     print(type(ret3))


# json.dump能够把python类型放入对象文件中
with open("douban.json", "w", encoding="utf-8") as f:
    json.dump(json_str, f, ensure_ascii=False, indent=4)
