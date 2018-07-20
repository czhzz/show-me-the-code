# 0001
# 2018/07/20
# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码。
# 使用 Python 生成 200 个激活码

__author__ = 'czhzz'

import random
import string

def random_code(filename, num, length):
  file = open(filename, 'w')
  for i in range(0, num):
    code = ''
    for j in range(0, length):
      code += str(j)+random.choice(string.ascii_letters + string.digits)
      # code += chr(random.randint(65, 90))
    print(str(i+1) + ':' + code)
    file.write(code+'\n')
  file.close()
  return 0

if __name__ == '__main__':
  filename = 'code.txt'
  random_code(filename, 200, 10)
