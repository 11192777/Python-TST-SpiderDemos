# coding=utf-8
import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def ___parse_url(url, headers, timeout, method, data, proxies):
    if method == "GET":
        response = requests.get(url, headers=headers, timeout=timeout, proxies=proxies)
    else:
        response = requests.post(url, headers=headers, timeout=timeout, data=data, proxies=proxies)
    assert response.status_code == 200
    return response.content


def parse_url(url, headers, timeout, method="GET", data=None, proxies={}):
    try:
        html_str = ___parse_url(url=url, headers=headers, timeout=timeout, method=method, data=data, proxies=proxies)
    except:
        html_str = None

    return html_str


if __name__ == '__main__':
    url = "https://www.baidu.com"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
    print(parse_url(url=url, headers=headers, timeout=1))
