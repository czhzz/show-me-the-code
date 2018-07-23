# 连接Redis

## 0.引用方式
需要Redis数据库
* pip安装相应模块 `pip install redis`
* 引入 `import redis`

## 1.方法
### 打开连接
```
redis.StrictRedis()
```
StricRedis()用于实现Redis官方的命令。
```
redis.Redis()
```
Redis()向后兼容老版本的redis-py。
建议使用StrictRedis()进行连接。例如：
```
conn = redis.StrictRedis(host='localhost', port=6379, db=0, password='123456')
```

### flushdb()
用于清空当前数据库中的所有 key。

### set(key, value)
设置给定 key 的值。如果 key 已经存储其他值， SET 就覆写旧值，且无视类型。
例如：
```
conn.set(0, 'Hello')
```

### get(key)
获取key的值。
例如：
```
conn.get(0)
```
得到`Hello`
