# 0005
# 2018/07/24
# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。1136*640

__author__ = 'czhzz'

import os
import re
import glob
from PIL import Image

def thumbnail_img(path, result):
  img_list = glob.glob(path+r'*.jpg')
  for img in img_list:
    image = Image.open(img)
    image.thumbnail((1136, 640))
    print(image.format, image.size, image.mode)
    img = os.path.basename(img)
    # img = re.search(r'(?<=\\).\.jpg', img).group()
    new_img = os.path.join(result, img)
    image.save(new_img, 'jpeg')


if __name__ == '__main__':
  filepath = 'img/'
  result = 'result/'
  if not os.path.exists(result):
    os.mkdir(result)
  thumbnail_img(filepath, result)
