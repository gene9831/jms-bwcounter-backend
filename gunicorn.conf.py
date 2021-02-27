import multiprocessing

debug = False
# gunicorn监控的地址和端口
bind = '0.0.0.0:5000'
# 设置守护进程，默认 False
daemon = True
# 进程数，默认1
workers = 1  # multiprocessing.cpu_count() * 2 + 1
# 每个进程开启的线程数，默认1
threads = 1
# 工作模式协程详看https://ox0spy.github.io/post/web-test/gunicorn-worker-class/
worker_class = 'gevent'
# gunicorn进程idkill掉该文件的id, gunicorn就停止
pidfile = './app.pid'
# 默认 'info'
loglevel = 'info'
# 默认 None
accesslog = './access.log'
# 默认输出到标准输出
errorlog = './error.log'
