#!/usr/bin/python3
import urllib.request

url = "http://www.baidu.com"
print('第一种方法')

response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))