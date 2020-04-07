# coding=utf-8
import requests

start_url = "https://careers.tencent.com/search.html?index=2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
proxies = {
    "http": "http://119.120.183.197"
}

img_path = "http://tiebapic.baidu.com/forum/pic/item/cf0ceafe9925bc3111da7ff849df8db1c91370c0.jpg"
response = requests.get(start_url, headers=headers, proxies=proxies, verify=False)

print(response.content.decode())
