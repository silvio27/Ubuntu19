#!/usr/bin/python3
#Author:Silvio27
# -*-coding: utf-8 -*-
#@Time  :2019/6/14 10:19
#@Author:Silvio27


import os
import requests
from bs4 import BeautifulSoup
import json

url = 'https://free.ishadowx.org/'

app_dir = r'C:\ssr\ShadowsocksR-dotnet4.0.exe'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.content, 'lxml')
content = soup.body.find_all('div', attrs={'class': 'hover-text'})
content1 = soup.select('body > div > div > div > div > div > div > div > div > h4')


aa = []
bb = []
for data in content1:

    if data.text in ['Click to view QR Code', 'Copy config URL ', 'Setup Guide']:
        continue
    data = data.text.split(':')
    if len(bb) > 7:
        aa.append(bb)
        bb = []

    for b in data:
        if b == '\n ':
            continue
        bb.append(b.strip())

for i in aa:
    for j in ['IP Address', 'Port', 'Password', 'Method']:
        i.remove(j)

aa.pop()
cc = {}
dd =[]
for i in aa:
    #print(i)
    cc["server"] = i[0]
    cc["server_port"] = int(i[1])
    cc["password"] = i[2]
    cc["method"] = i[3]
    dd.append(cc)
    cc={}

dd.pop()
# print(dd)

jsonurl = 'C:/ssr/gui-config.json' #文件的保存路径

f = open(jsonurl)
res = f.read()
res = json.loads(res)
res["configs"] = dd
f.close()

res = json.dumps(res)
f = open(jsonurl, 'w')
f.write(res)
f.close()
print('Done')



os.system(r'taskkill /F /IM ShadowsocksR-dotnet4.0.exe')
os.startfile(app_dir)
print('Done')


# import os
# def open_app(app_dir):
#     os.startfile(app_dir)
# if __name__ == "__main__":
#     app_dir = r'C:\ssr\ShadowsocksR-dotnet4.0.exe'
#     open_app(app_dir)

