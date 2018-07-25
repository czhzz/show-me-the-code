# 0006
# 2018/07/25
# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

__author__ = 'czhzz'

import os
import glob
import re
from collections import OrderedDict

def get_num(word, list):
  word_num = 0
  for item in list:
    if item.lower() == word.lower():
      word_num += 1
  return word_num


def text_analysis(path):
  articles = glob.glob(path+r'*.txt')
  word_dict = OrderedDict()
  for article in articles:
    file = open(article, encoding='utf-8').read()
    file_word_list = re.findall(r'[\w\-\_\'\’]+', file)
    for word in file_word_list:
      word_dict[word] = get_num(word, file_word_list)
    sort_dict = OrderedDict(sorted(word_dict.items(), key=lambda x: x[1], reverse = True))
    print('在%s中出现的最多的单词是：' % os.path.basename(article))
    for item in sort_dict:
      print(item + ': %s次' % sort_dict[item])
      break

if __name__ == '__main__':
  path = 'diary/'
  text_analysis(path)
