# 有序词典OrderedDict

## 引入方式
```
from collections import OrderedDict
```

## 含义
> 旧版本，但可以用。

在使用普通`dict`时，Key是无序的。在对`dict`做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用`OrderedDict`。
例如：
```
d = dict([('a', 1), ('b', 2), ('c', 3)])
{'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```
> 注意，`OrderedDict`的Key会按照插入的顺序排列，不是Key本身排序。

## 方法

### items()
返回由“键值对组成元素”的列表。

#待续