# 0018
# 2018/08/10
# 将ecxel内容写到xml中

__author__ = 'czhzz'

import json

import xlrd
import json
from lxml import etree

def read_excel(file_name):
  exl = xlrd.open_workbook(file_name, encoding_override='utf-8')
  exl_sheet = exl.sheet_by_name('city')
  data = {}
  for i in range(exl_sheet.nrows):
    data[exl_sheet.row_values(i)[0]] = exl_sheet.row_values(i)[1]
  return json.dumps(data, ensure_ascii=False)

def save_to_xml(data, new_file_name):
  root = etree.Element('root')
  students = etree.SubElement(root, 'city')
  students.text = data

  student_xml = etree.ElementTree(root)
  student_xml.write(new_file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
  content = read_excel('city.xls')
  save_to_xml(content, 'city.xml')
