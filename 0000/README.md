# ImageDraw 模块

## 0.引用方式
```
from PIL import Image, ImageDraw
```

## 1.模块函数
```
Draw(image)
```
创建一个可以在给定图像上绘图的对象。如：
```
image = Image.open('a.jpg')
draw = ImageDraw.Draw(image)
```

## 2.模块方法
### 2.1 添加文字
```
draw.text(position, string, options)
```
在给定的位置（position）绘制一个字符串（String）。
变量option包含font与fill，其中font指定绘制所用字体，fill指定绘制所用颜色。
```
myposition = (0,0)
mytext = 'hello'
myfont = 'Arial.ttf'
mycolor = '#ff0000' # or rgb(255, 0, 0)
draw.text(myposition, mytext, font=myfont, fill=mycolor)
```

### 待续

