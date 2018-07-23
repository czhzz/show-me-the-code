# 0003
# 2018/07/22
# 将 0001 题生成的 200 个激活码保存到Redis非关系型数据库中。

__author__ = 'czhzz'

import redis

def save_to_redis():
  conn = redis.StrictRedis(host='localhost', port=6379, db=0, password='123456')
  conn.flushdb()
  code_file = open('../0001/code.txt').readlines()
  for line, num in zip(code_file, range(1, len(code_file)+1)):
    conn.set(num, line)

def show_code():
  num = int(input('请输入数字（1-200）：'))
  if num > 200 or num < 1:
    print('输入错误')
    return 0
  conn = redis.StrictRedis(host='localhost', port=6379, db=0, password='123456')
  print(str(conn.get(num), 'utf-8'))

if __name__ == '__main__':
  save_to_redis()
  show_code()
