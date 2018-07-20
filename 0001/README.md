# 文件读写

## 0.引用方式
```
无需引用
```

## 1.函数
### 1.1打开文件
```
open(filname, mode, encoding)
```
按照mode打开路径为filename的文件。如：
```
filename = 'code.txt'
file = open(filename, 'w')
```

mode传入参数如下:
```
r:    以只读模式打开，默认
w：   以写方式打开
a：   以追加方式打开
r+：  以读写模式打开
w+：  以读写模式打开
rb：  以二进制读模式打开
wb：  以二进制写模式打开
ab：  以二进制追加模式打开
rb+： 以二进制读写模式打开
wb+： 以二进制读写模式打开
ab+： 以二进制追加模式打开
```

encoding的含义如下：

要读取非`UTF-8`编码的文本文件，
需要给`open()`函数传入`encoding`参数

### 待续

