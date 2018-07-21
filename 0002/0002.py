# 0002
# 2018/07/21
# 将 0001 题生成的 200 个激活码保存到MySQL关系型数据库中。 

__author__ = 'czhzz'

import mysql.connector

# db = {
#   'host': 'localhost',
#   'port': 3306,
#   'database': 'python-code',
#   'user': 'root',
#   'password': '123456'
# }

def save_to_mysql():
  conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='123456', database='python-code')
  cursor = conn.cursor()
  drop_table = 'DROP TABLE IF EXISTS act_code'
  cursor.execute(drop_table)
  cursor.execute()
  create_table = 'CREATE TABLE act_code(id int AUTO_INCREMENT PRIMARY KEY, code varchar(50) NOT NULL)'
  cursor.execute(create_table)

  code_file = open('../0001/code.txt')
  for line in code_file.readlines():
    insert_code = 'INSERT INTO act_code(code) VALUES(\'%s\')' % line.strip()
    cursor.execute(insert_code)

  conn.commit()
  cursor.close()
  conn.close()

if __name__ == '__main__':
  save_to_mysql()
