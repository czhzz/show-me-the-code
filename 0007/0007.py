# 0007
# 2018/07/26
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

__author__ = 'czhzz'

import os
import re
import glob
from numpy import array

def count_num(code):
  num = array([0, 0, 0])
  f = open(code, encoding='utf-8')
  fl = f.readlines()
  for line in fl:
    if re.match(r'^#', line) == None:
      pass
    else:
      num[1] += 1
  num[2] = fl.count('\n')
  num[0] = len(fl) - num[1] - num[2]
  return num

def code_analysis(path):
  codes = glob.glob(path + r'*.py')
  code_num = array([0, 0, 0])
  for code in codes:
    num = count_num(code)
    code_num += num
  print('代码\t注释\t空行')
  for item in code_num:
    print(str(item)+'\t', end='')
    
if __name__ == '__main__':
  path = '..\\0000\\'
  code_analysis(path)
