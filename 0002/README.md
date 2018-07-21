# 连接MySQL

## 0.引用方式
* pip安装相应模块 `pip install mysql-connector`

  or

  安装 [mysql-connector-python](https://dev.mysql.com/downloads/connector/python/)

* 引入 `import mysql.connector`

## 1.方法
### 打开连接
```
mysql.connector.connect(*args, **kwargs)
```
按照参数打开数据库连接。
例如：
```
conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='123456', database='python-code')
```

### cursor()
利用cursor()方法创建数据库对象。
例如：
```
cursor = conn.cursor()
```

### execute()
```
execute(self, operation, params=None, multi=False)
```
利用execute()方法执行SQL语句。其中默认传入operation参数。
例如：
```
create_table = 'CREATE TABLE act_code(id int AUTO_INCREMENT PRIMARY KEY, code varchar(50) NOT NULL)'
cursor.execute(create_table)
```

### commit()
提交对数据库的操作。

>注意：不执行commit()，数据库中不会有更改

### close()
关闭数据库对象或数据库连接。
例如：
```
cursor.close()
conn.close()
```
>注意：一般不需要数据库操作后就要关闭数据库连接，通常先关闭cursor对象，再关闭连接。

# 字符串格式化
## 占位符方式
### %s
字符串占位符。
```
str = 'World'
output = 'Hello, %s' % str
```
输出`Hello, World`
