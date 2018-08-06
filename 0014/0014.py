# 0014
# 2018/08/06
# 将txt内容写到excel中

__author__ = 'czhzz'

import json
import xlwt

def save_to_excel(filename):
  f = open(filename, encoding='utf-8')
  file_content = json.load(f)

  wb = xlwt.Workbook()
  ws = wb.add_sheet('student')
  row = 0
  col = 0

  for k, v in sorted(file_content.items(),key=lambda d:d[0]):
    ws.write(row, col, k)
    for i in v:
      col += 1
      ws.write(row, col, i)
    row += 1
    col = 0

  wb.save('student.xls')

if __name__ == '__main__':
  filename = 'student.txt'
  save_to_excel(filename)
