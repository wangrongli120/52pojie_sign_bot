# -- coding: utf-8 --

import os
import sys
import urllib.parse
import requests
from bs4 import BeautifulSoup


def get_env_cookie():
    cookie = ""
    if cookie == "":
        if os.environ.get("52POJIE_COOKIE"):
            cookie = os.environ.get("52POJIE_COOKIE")
        else:
            print("请配置环境变量52POJIE_COOKIE")
            sys.exit()
    return cookie


def get_input_cookie():
    cookie = ""
    if not cookie:
        cookie = input("请输入52pojie cookie的值：\n")
    return cookie


def sign():
    cookie = get_input_cookie()
    url1 = "https://www.52pojie.cn/CSPDREL2hvbWUucGhwP21vZD10YXNrJmRvPWRyYXcmaWQ9Mg==?wzwscspd=MC4wLjAuMA=="
    url2 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2F'
    url3 = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
    cookie = urllib.parse.unquote(cookie)
    cookie_list = cookie.split(";")
    cookie = ''
    for i in cookie_list:
        key = i.split("=")[0]
        if "htVC_2132_saltkey" in key:
            cookie += "htVC_2132_saltkey=" + urllib.parse.quote(i.split("=")[1]) + "; "
        if "htVC_2132_auth" in key:
            cookie += "htVC_2132_auth=" + urllib.parse.quote(i.split("=")[1]) + ";"
    if not ('htVC_2132_saltkey' in cookie or 'htVC_2132_auth' in cookie):
        print("cookie中未包含htVC_2132_saltkey或htVC_2132_auth字段，请检查cookie")
        sys.exit()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/109.0.0.0 Safari/537.36",
    }
    r = requests.get(url1, headers=headers, allow_redirects=False)
    s_cookie = r.headers['Set-Cookie']
    cookie = cookie + s_cookie
    headers['Cookie'] = cookie
    r = requests.get(url2, headers=headers, allow_redirects=False)
    s_cookie = r.headers['Set-Cookie']
    cookie = cookie + s_cookie
    headers['Cookie'] = cookie
    r = requests.get(url3, headers=headers)
    r_data = BeautifulSoup(r.text, "html.parser")
    jx_data = r_data.find("div", id="messagetext").find("p").text
    if "您需要先登录才能继续本操作" in jx_data:
        print("Cookie 失效")
    elif "恭喜" in jx_data:
        print("签到成功")
    elif "不是进行中的任务" in jx_data:
        print("今日已签到")
    else:
        print("签到失败")

if __name__ == '__main__':
    sign()
