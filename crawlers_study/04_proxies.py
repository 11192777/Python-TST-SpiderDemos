import requests

proxies = {
    "http": "http://113.103.226.174"
}
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

if __name__ == '__main__':
    response = requests.get("https://www.baidu.com", proxies=proxies, headers=headers)
    print(response.status_code)
