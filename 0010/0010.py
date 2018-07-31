# 0010
# 2018/07/31
# 生成字母验证码图片

__author__ = 'czhzz'

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def random_letter():
  return chr(random.randint(65, 90))

def random_bg_color():
  return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def random_letter_color():
  return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def create_check_code():
  # size
  width = 60 * 4
  height = 60

  #font
  font = ImageFont.truetype('arial.ttf', 36)

  # draw
  image = Image.new('RGB', (width, height), (255, 255, 255))
  draw = ImageDraw.Draw(image)

  # 填充背景颜色
  for x in range(width):
    for y in range(height):
      draw.point((x, y), fill=random_bg_color())
  
  # 填充字母
  for n in range(4):
    draw.text((60 * n + 10, 10), random_letter(), font=font, fill=random_letter_color())

  # 模糊
  image = image.filter(ImageFilter.BLUR)

  image.save('code.jpg', 'jpeg')

if __name__ == '__main__':
  create_check_code()
