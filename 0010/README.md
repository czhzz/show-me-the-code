# Pillow

# 引入方式
* 安装`pip install pillow`
* 引入`from PIL import *`

## Image模块
`from PIL import Image`

### 创建新图片
`Image.new(mode, size, color?)`

* `mode`指图像中像素的类型和深度，例如`RGB`、`RGBA`。
* `size`指图像二维像素尺寸，宽和高，例如`(240, 60)`。
* `color`指图像颜色，可选，例如`RGB`下`(255, 255, 255)`。

## ImageDraw模块
`from PIL import ImageDraw`

### Point
`draw.point(xy, options)`
在给定的坐标点上画一些点。

* `xy`指点的二维坐标。
* `options`包含`fill`指点中填充的颜色。

## ImageFilter模块
`from PIL import ImageFilter`

### Filter
`image.filter(mode)`

对图像进行平滑、锐化、边界增强等滤波处理。
