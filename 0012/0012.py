# 0012
# 2018/08/02
# 当用户输入敏感词语，则用 星号 * 替换。

__author__ = 'czhzz'

def filter_word(text):
  f = open('filtered_words.txt', encoding='utf-8')
  for word in f.read().split('\n'):
    if word in text:
      text = text.replace(word, '*' * len(word))
  return text

if __name__ == '__main__':
  text = input('>')
  output = filter_word(text)
  print(output)
