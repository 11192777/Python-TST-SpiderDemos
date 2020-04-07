# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
# params = {
#     "wd": {"孟庆宇"}
# }
# url_temp = "https://www.baidu.com"
# response = requests.get(url=url_temp, headers=headers, params=params)
# print(response.status_code)
# print(response.request.url)


# 拿出参数 （孟庆宇）
url = "https://www.baidu.com/?wd={}".format("孟庆宇")
response = requests.get(url=url, headers=headers)
print(response.status_code)
print(response.request.url)