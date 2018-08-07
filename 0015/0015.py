# 0015
# 2018/08/07
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

  for k, v in sorted(file_content.items(),key=lambda d:d[0]):
    ws.write(row, col, k)
    col += 1
    ws.write(row, col, v)
    row += 1
    col = 0

  wb.save('city.xls')

if __name__ == '__main__':
  filename = 'city.txt'
  save_to_excel(filename)
