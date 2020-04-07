# coding=utf-8

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
proxies = {
    "http": "http://113.103.226.174"
}

if __name__ == '__main__':
    # url = "https://tieba.baidu.com/f?kw=supergirls"
    # response = requests.get(url=url, headers=headers, proxies=proxies)
    # content = response.content.decode()

    content = '''
        <div><ul>
            <li class="item-1"><a>frist item</a></li>
            <li class="item-1"><a href="link.htm2">second item</a></li>     
            <li class="item-inactive"><a href="link3.html">frist item</a></li>     
            <li class="item-1"><a href="link.htm4">3item</a></li>     
            <li class="item-2"><a href="link.htm5">4444item</a></li>     
            <li class="item-0"><a href="link.htm6">555 item</a></li>     
            <li class="item-1"><a href="link.htm7">88898989item</a></li>     
        </ul></div>
    '''

    html = etree.HTML(content)
    ret1 = html.xpath("//li[@class='item-1']/a/@href")
    print(ret1)

    ret2 = html.xpath("//li[@class='item-1']/a/text()")
    print(ret2)

    print("-" * 100)
    for href in ret1:
        item = {}
        item["href"] = href
        item["html"] = ret2[ret1.index(href)]
        print(item)

    print("-" * 100)
    ret3 = html.xpath("//li[@class='item-1']")
    for i in ret3:
        item = {}
        item["href2"] = i.xpath("./a/text()")[0] if len(i.xpath("./a/text()")) > 0 else None
        item["html2"] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href")) > 0 else None
        print(item)
