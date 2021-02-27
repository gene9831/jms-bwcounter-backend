import multiprocessing

debug = False
# gunicorn监控的地址和端口
bind = '0.0.0.0:5000'
# 设置守护进程
daemon = True
# 进程数
#workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
# 工作模式协程详看https://ox0spy.github.io/post/web-test/gunicorn-worker-class/
worker_class = 'gevent'
# 每个进程开启的线程数
threads = 1
# gunicorn进程idkill掉该文件的idgunicorn就停止
pidfile = './app.pid'
# 日志设置
loglevel = 'info'
accesslog = './access.log'
errorlog = './error.log'

