import time
import os
from flask import Flask, request
from flask_apscheduler import APScheduler
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import logging
import coloredlogs
import pymongo
import requests

# 加载.env中的变量
load_dotenv()  # take environment variables from .env.

jms_getbwcounter_url = os.environ.get('JMS_GETBWCOUNTER_URL')
scheduler_api_enabled = bool(os.environ.get('SCHEDULER_API_ENABLED'))
log_filename = os.environ.get('LOG_FILENAME') or 'a.log'

# 配置logger和coloredlogs
logger = logging.getLogger(__name__)

# Create a filehandler object
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.INFO)

# Create a ColoredFormatter to use as formatter for the FileHandler
formatter = coloredlogs.ColoredFormatter(
    '%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Install the coloredlogs module on the root logger
coloredlogs.install(level='INFO')


if scheduler_api_enabled:
    logger.warning(
        'SCHEDULER_API_ENABLED is set to true, DO NOT use it in production deployment')


class Config(object):
    SCHEDULER_API_ENABLED = scheduler_api_enabled
    MONGO_URI = os.environ.get('MONGO_URI')


app = Flask(__name__)
app.config.from_object(Config())


mongo = PyMongo(app)


# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def index():
    try:
        n = int(request.args.get('n'))
    except ValueError:
        n = 10
    n = 24 if n > 24 else n
    n = 1 if n <= 0 else n

    data = []
    for item in mongo.db.bwcounter.find({}, {'_id': 0}).sort([('update_time', pymongo.DESCENDING)]).limit(n):
        data.append(item)

    return {
        'data': data
    }


# cron examples
@scheduler.task('cron', id='get_bwcounter', hour='*')
def get_bwcounter():
    logger.info('Acquiring bandwidth counter...')
    current_time = round(time.time()) * 1000

    if jms_getbwcounter_url:
        r = requests.get(jms_getbwcounter_url)
        data = {
            **r.json(),
            'update_time': current_time
        }

        mongo.db.bwcounter.insert_one(data)
        logger.info('Bandwidth counter acquired.')
    else:
        logger.warning('JMS_GETBWCOUNTER_URL is empty')
