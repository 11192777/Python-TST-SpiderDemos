# coding=utf-8
import requests
import datetime
import time

session = requests.session()
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
}

# print(cookies)

dt = "2019-4-13 10:02:23"
# 转为时间数组
dt = datetime.datetime.now().__str__().split(".")[0]
print(dt)
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# 转为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)
cookies = "dy_did=d39547cd76073da1fdaeec5900061501; smidV2=20200308130726d55a66382f082cd3a3074178716c01fb00ebe235aa1bf53b0; PHPSESSID=49pgpubjddoce80mn3p4vg9l74; " \
          "acf_auth=de72gX4JFlXj90dsAAQwy205usqtRf2SBXMur1dF%2FZfor0xE5qv3RShqmui3seL5rVioJbV8Rix%2FWnXn93HZ3MYkMm9R7qAgsVcTHtshb7l8XMdUIpzsN5A; " \
          "dy_auth=5556octBRt6oiCja5IIzACtbj11waMGLNKF4jaSi3yP%2Bu7%2BB9%2FZtx4wc%2FQQsyBvu%2FBvq1iFduOONQ7XLlegYWX2Ejg6pSVdZiZHZ7uS57%2F4%2BiM3FWe0ysNg; " \
          "wan_auth37wan=e524ae81a805aVQjdFBsVhYOejixAEvJSYNsf9QbYsGJ%2F3%2FYUjrhRiaQh4nq31WK5ZusIpuFJJRIbgvOkdbSI7ho4A892MRfAZd5oR23HCQlmfLPru4; acf_uid=210807849; " \
          "acf_username=210807849; acf_nickname=Qing709282; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; " \
          "acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar_v3%2F201807%2F4438877af21af88a802eb59fbc895803_; acf_ct=0; acf_ltkid=11685998; acf_biz=1; " \
          "acf_stk=d87342e8b7b11cfd; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1583644047,1583644152; acf_did=d39547cd76073da1fdaeec5900061501; " \
          "Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7={}".format("1583647309")

cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
print(cookies)
proxies = {
    "http": "http://113.103.226.174"
}
post_url = "https://www.douyu.com/member/cp"

resonse = session.get(url=post_url, headers=headers, proxies=proxies, cookies=cookies)
print(resonse.content.decode())

print(resonse.content)