# 0008
# 2018/07/27
# 一个HTML文件，找出里面的正文。

__author__ = 'czhzz'

from bs4 import BeautifulSoup

def html_analysis(filename):
  f = open(filename)
  testHtml = BeautifulSoup(f, 'html.parser', from_encoding="utf-8")
  content = testHtml.body
  print(content.prettify())

if __name__ == '__main__':
  filename = 'test.html'
  html_analysis(filename)
