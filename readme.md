# JMS 流量统计 API

使用 [just my socks](https://justmysocks3.net/) 官方 api，每隔一小时获取已流量数据，保存至 [mongodb](https://www.mongodb.com/) 中

## 安装

安装依赖

```bash
pip install -r requirements.txt
```

编辑`.env`文件

```ini
# mongodb 地址
MONGO_URI=mongodb://username:password@hostname:27017/db_name
# 已购买的jms服务中提供的 getbwcounter api
JMS_GETBWCOUNTER_URL=https://justmysocks3.net/members/getbwcounter.php?service=${service}&id=${id}
# 日志文件名，默认是 a.log
#LOG_FILENAME=a.log
```

## 使用

- 运行

```bash
gunicorn -c gunicorn.conf.py app:app
```

- 停止

```bash
kill $(cat app.pid)
```

- 重启

```bash
kill -HUP $(cat app.pid)
```

- 懒得记命令，写了个简单脚本

```bash
$ ./manage.sh
useage: manage.sh [start | stop | restart]
```
