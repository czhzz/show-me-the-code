# BeautifulSoup模块

> [Beautiful Soup 4.2.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

## 引用方式
* 安装 `pip install beautifulsoup4`
* 引用 `from bs4 import BeautifulSoup`

## 存在问题
中文解析乱码

## find_all()
```
find_all( name , attrs , recursive , text , **kwargs )
```
搜索当前tag的所有tag子节点，并判断是否符合过滤器的条件。

### keyword 参数
如果传入`href`参数,Beautiful Soup会搜索每个`tag`的`href`属性。
例如：
```
content = testHtml.find_all(href=True)
```
返回所有包含`href`链接的节点。

# 待续
