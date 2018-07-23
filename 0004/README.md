# 正则表达式

>[正则表达式教程 -- 菜鸟教程](http://www.runoob.com/regexp/regexp-tutorial.html)

## 0.引用方式
```
import re
```

## 1.模块方法
### compile()
```
compile(pattern,flags=0)
```
可以把那些常用的正则表达式编译成正则表达式对象。pattern指编译时用的表达式字符串，flags指编译标志位，用于修改正则表达式的匹配方式。
| Flag              | 含义|
| --------          | ----- |
| re.S(DOTALL)      | 匹配包括换行在内的所有字符 |
| re.I(IGNORECASE)  | 使匹配对大小写不敏感 |
| re.L(LOCALE)      | 做本地化识别（locale-aware)匹配，法语等 |
| re.M(MULTILINE)   | 多行匹配，影响^和$ |
| re.X(VERBOSE)     | 该标志通过给予更灵活的格式以便将正则表达式写得更易于理解 |
| re.U              | 根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B |
例如：
```
tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))
```
输出`['good', 'cool']`

### match()
```
match(pattern, string, flags=0)
```
尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
例如：
```
print(re.match('com','comwww.runcomoob').group())
print(re.match('com','Comwww.runcomoob',re.I).group())
```
输出`com`, `com`


### search()
```
search(pattern, string, flags=0)
```
扫描整个字符串并返回第一个成功的匹配。
例如：
```
print(re.search('\dcom','www.4comrunoob.5com').span())
```
输出：`(4, 7)`

>注：match和search一旦匹配成功，就是一个match object对象，而match object对象有以下方法：
> * group() 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
> * start() 返回匹配开始的位置
> * end() 返回匹配结束的位置
> * span() 返回一个元组包含匹配 (开始,结束) 的位置

### findall()
```
findall(pattern, string, flags=0)
```
遍历匹配，可以获取字符串中所有匹配的字符串，返回一个列表。
例如：
```
word_list = re.findall(r'[\w\-\_\.\']+', file)
```

### split()
```
split(pattern, string[, maxsplit])
```
按照能够匹配的子串将string分割后返回列表。
例如：
```
print(re.split('\d+','one1two2three3four4five5'))
```
输出`['one', 'two', 'three', 'four', 'five', '']`

### sub()
```
sub(pattern, repl, string, count)
```
替换string中每一个匹配的子串后返回替换后的字符串。
count指替换个数。默认为0，表示每个匹配项都替换。
例如：
```
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', '-', text))
```
输出`JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...`

# 待续
