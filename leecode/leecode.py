# from bs4 import BeautifulSoup
# from lxml import html
import xml
import requests
import sys
import urllib.request


url = "https://www.kaggle.com/zhangliey187/visa-free-travel/downloads/visa-free-travel.zip/1"



url = "https://mp.csdn.net/postlist"
headers = {'User-Agent:': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
req = urllib.request.Request(url=url, headers=headers)
content = urllib.request.urlopen(req)


f = requests.get(url)
sys.getsizeof(f)

with open("visa-free-travel.zip", "wb") as code:
    code.write(f.content)

import zipfile

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')

unzip_file("visa-free-travel.zip", "visa-free-travel")






import urllib.request

urllib.request.urlretrieve(url, "demo.zip")

unzip_file("demo.zip", "visa-free-travel")











import urllib.request

url = "https://mp.csdn.net/postlist"
headers = {'User-Agent:': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
req = urllib.request.Request(url=url)
content = urllib.request.urlopen(req)

with open('a.html', 'w', encoding='utf-8') as f:
    f.write(content.read().decode('utf-8'))





import urllib.request

url = "https://mp.csdn.net/postlist"
headers = {'cookie': "uuid_tt_dd=10_19448638060-1544431065265-418791; ARK_ID=JS9d83dc2486565dda8e75483479b682239d83; smidV2=2018121114504373023ccc85f3b0ed528d24b58843a24a002a800eef6b518b0; UN=qq_33685421; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!5744*1*qq_33685421!6525*1*10_19448638060-1544431065265-418791; ADHOC_MEMBERSHIP_CLIENT_ID1.0=1ccb96b6-d124-d23e-273a-9b552a81f0c3; _ga=GA1.2.1835859471.1557036332; dc_session_id=10_1558004357176.880630; acw_tc=2760823215640380034524796eeab2064361c3ce9ac450ada2ae1c77564bca; firstDie=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1564799838,1564800089,1564800491,1564801278; c-login-auto=25; SESSION=93813ff7-0dc7-474f-be2f-b3606f764256; UserName=qq_33685421; UserInfo=ad621ecf08f84957b81aba1c1b397d29; UserToken=ad621ecf08f84957b81aba1c1b397d29; UserNick=qq_33685421; AU=176; BT=1564801655546; p_uid=U000000; TY_SESSION_ID=b633a89c-357d-40f4-9f99-87a6ce80e9a5; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1564801659; dc_tos=pvn4oq"}
req = urllib.request.Request(url=url, headers=headers)
content = urllib.request.urlopen(req)

with open('b.html', 'w', encoding='utf-8') as f:
    f.write(content.read().decode('utf-8'))




import pandas as pd
def hallenge_three(country_from , country_to):
    url = 'https://storage.googleapis.com/kaggle-datasets/159274/364937/cleandata.json?' \
          'GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&' \
          'Expires=1565055906&' \
          'Signature=IicyBtBiDuVwVr3QL9eb6khs8nLkvze9Xcmot%2FO6RrdvDhr0kbvdG1%2FoCf569fAHtIgV83t5ITxks3coGI6hnIUEHxTWh' \
          'WrKTwW9SFvirVUAm5vIKTFygHhYMjNKsQ5Yikrqd89TXmu1Wc5wKA9oqXbeBVA8gtfZYvsSGuSt8aSswB0s4ygcKB7jkNYW' \
          '8gCZZDisRQ0jT3EHVm%2FFS0HDvF0j1YM2%2FEz3cXUtLvuCR%2FepZfY4AkzGixMNnDgPHMrB6j2F5fKBnBDqGgO2YNKqd' \
          'EDTDBiEUcaKUh6qua7bodp99KvnOCyxo3gXRpBG4jsTaLT4wt0lKbYHoU4wUaQsMA%3D%3D'
    response = requests.get(url)
    data_json = response.json()
    data_pd = pd.DataFrame(data_json)

    if country_from == country_to:
        raise ValueError('Please input two different country')

    if country_from in list(data_pd.country_name):
        if country_to in list(data_pd[data_pd.country_name == country_from].connections)[0]:
            return True
        else:
            return False

    else:
        raise ValueError('This country do not exist in the list')









import requests
import urllib
import random
from datetime import datetime


# session代表某一次连接
huihuSession = requests.session()
# 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
huihuSession.cookies = cookielib.LWPCookieJar(filename="huihuCookies.txt")

header = {
    # "origin": "https://passport.huihu.cn",
    "Referer": "http://hh.haiper.com.cn/w/wander/user/login/",

}


def huihuLogin(account, password):
    #
    print("开始模拟登录嘻嘻嘻")

    postUrl = "https://www.kaggle.com/zhangliey187/visa-free-travel"
    postData = {
        "username": account,
        "password": password,
    }

    # 使用session直接post请求
    responseRes = huihuSession.post(postUrl, data=postData, headers=header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    # responseRes = requests.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    # print(f"text = {responseRes.text}")
    huihuSession.cookies.save()


def isLoginStatus():
    # 通过访问个人中心页面的返回状态码来判断是否为登录状态
    for i in range(2131, 2134):
        routeUrl = "http://hh.haiper.com.cn/w/bench/extend/health/trade/all?nickname=&type=&gender=&level=&range%5Bstart%5D=2014-11-11+14%3A57&range%5Bend%5D=2018-06-06+14%3A57&page=" + str(
            i)

        # 下面有两个关键点
        # 第一个是header，如果不设置，会返回500的错误
        # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
        # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
        # allow_redirects = False  就是不允许重定向
        try:
            responseRes = huihuSession.get(routeUrl, headers=header, allow_redirects=False)
            result = responseRes.text
        except:
            continue
        start = result.find('<div class="form-control-static form-control-static-list">')
        result = result[start:]
        # print (result)
        for j in range(1, 16):
            start = result.find('擦擦擦图片')
            if start == -1:
                break
            else:
                result = result[start:]
                start = result.find('src="')
                result = result[start + 5:]
                end = result.find('" class="img-rounded"')
                imgpath = result[:end]
                print(imgpath)
                if imgpath == '/attachment/':
                    continue
                randomname = datetime.now().strftime("%Y%m%d_%H%M%S") + str(random.randint(1, 100)) + '.jpg'
                try:
                    urllib.request.urlretrieve(imgpath, './擦擦擦/' + randomname)
                except:
                    continue
        print(i)
    print(f"isLoginStatus = {responseRes.status_code}")
    # print(f"text = {responseRes.text}")
    if responseRes.status_code != 200:
        return False
    else:
        return True


if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    huihuLogin("xxxx", "xxxx")
    isLogin1 = isLoginStatus()
    print(f"is login huihu = {isLogin1}")
