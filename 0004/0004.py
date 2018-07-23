# 0004
# 2018/07/23
# 任一个英文的纯文本文件，统计其中的单词出现的个数。

__author__ = 'czhzz'

import re

def count_the_words(filename):
  file = open(filename).read()
  word_list = re.findall(r'[\w\-\_\.\']+', file)
  print(len(word_list))

if __name__ == '__main__':
  filename = 'English.txt'
  count_the_words(filename)
