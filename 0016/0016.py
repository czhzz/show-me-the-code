# 0016
# 2018/08/08
# 将txt内容写到excel中

__author__ = 'czhzz'

import json
import xlwt

def save_to_excel(filename):
  f = open(filename, encoding='utf-8')
  file_content = json.load(f)
  print(file_content)
  wb = xlwt.Workbook()
  ws = wb.add_sheet('city')
  row = 0
  col = 0

  for i in file_content:
    for j in i:
      ws.write(row, col, j)
      col += 1
    row += 1
    col = 0

  wb.save('numbers.xls')

if __name__ == '__main__':
  filename = 'numbers.txt'
  save_to_excel(filename)
