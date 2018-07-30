# 0009
# 2018/07/30
# 一个HTML文件，找出里面的链接。

__author__ = 'czhzz'

from bs4 import BeautifulSoup

def html_analysis(filename):
  f = open(filename)
  testHtml = BeautifulSoup(f, 'html.parser', from_encoding="utf-8")
  content = testHtml.find_all(href=True)
  print(content)

if __name__ == '__main__':
  filename = 'test.html'
  html_analysis(filename)
