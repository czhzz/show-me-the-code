# 0000
# 2018/07/19
# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

__author__ = 'czhzz'

from PIL import Image, ImageDraw, ImageFont

def add_num(filename, result, text, color):
  img = Image.open(filename)
  width = img.size[0]
  myfont = ImageFont.truetype('arial.ttf', size=width//8)
  draw = ImageDraw.Draw(img)
  draw.text((width-width//8, 0), text, font=myfont, fill=color)
  img.save(result, 'png')
  return 0

if __name__ == '__main__':
  filename = 'a.png'
  result = 'b.png'
  text = '4'
  fillcolor = (255, 0, 0)
  add_num(filename, result, text, fillcolor)
