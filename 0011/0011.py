# 0011
# 2018/08/01
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

__author__ = 'czh'

def filter_word():
  text = input('>')
  flag = False
  f = open('filtered_words.txt', encoding='utf-8')
  for word in f.read().split('\n'):
    if word in text:
      flag = True
  
  if flag:
    print('Freedom')
  else:
    print('Human Rights')

  f.close()

if __name__ == '__main__':
  filter_word()
