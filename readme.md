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

## 运行

```bash
gunicorn -b 127.0.0.1:5000 app:app -D
```

> `-D`: 以守护进程形式来运行 `gunicorn` 进程，即后台运行
