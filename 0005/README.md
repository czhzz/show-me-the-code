# glob模块

## 引用方式
```
import glob
```

## 主要方法
### glob()
返回所有匹配的文件路径列表。
需要一个参数用来指定匹配的路径字符串。
返回的文件名只包括当前目录里的文件名，不包括子文件夹里的文件。
例如：
```
glob.glob(r'c:*.txt')
```
返回C盘下的所有txt文件名

# os模块

## 引用方式
```
import os
```

## 主要方法
### 查看文件是否存在
```
os.path.exists(path)
```
是否存在文件或者文件夹。
例如：
```
os.path.exists('C:/none')
```
返回`false`

### 创建目录
```
os.mkdir(path)
```
创建一个文件夹。
例如：
```
os.mkdir('C:/none')
```
在C盘下创建none文件夹

### 查看文件名
```
os.path.basename(path)
```
返回path中的文件名部分。
例如：
```
path = 'C:/none/test.txt'
print(os.path.basename(path))
```
输出：`test.txt`

# Image模块

## 引用方式
```
from PIL import Image
```

## 主要方法

### thumbnail()
制作缩略图。
例如：
```
im=Image.open(path)
im.thumbnail((80,80))
im.save(path, 'JPEG')
```
