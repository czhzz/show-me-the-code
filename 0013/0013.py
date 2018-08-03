# 0013
# 2018/08/03
# 写一个爬图片的程序

__author__ = 'czhzz'

import os
from urllib import request, parse
from bs4 import BeautifulSoup

def catch_pics(url):
  print('catch pics')
  html = request.urlopen(url)
  bs = BeautifulSoup(html, 'html.parser')
  for i in bs.find_all('img'):
    download_pics('http:' + i['src'])

def download_pics(pic_url):
  print('download pics')
  image = request.urlopen(pic_url).read()
  filename = os.path.basename(parse.urlsplit(pic_url).path)
  print(filename)
  output = open(filename, 'wb')
  output.write(image)
  output.close()

if __name__ == '__main__':
  url = 'http://www.baidu.com'
  catch_pics(url)
