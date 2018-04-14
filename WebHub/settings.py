# -*- coding: utf-8 -*-

# Scrapy settings for pornhub project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WebHub'

SPIDER_MODULES = ['WebHub.spiders']
NEWSPIDER_MODULE = 'WebHub.spiders'

DOWNLOAD_DELAY = 0.5  # 间隔时间
# LOG_LEVEL = 'INFO'  # 日志级别
CONCURRENT_REQUESTS = 20  # 默认为16
# CONCURRENT_ITEMS = 1
# CONCURRENT_REQUESTS_PER_IP = 1
REDIRECT_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'pornhub (+http://www.yourdomain.com)'

# 请求超时
DOWNLOAD_TIMEOUT = 5
# 重新请求
RETRY_ENABLED = True
# 重试次数
RETRY_TIMES = 3


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    "WebHub.middlewares.UserAgentMiddleware": 401,
    "WebHub.middlewares.CookiesMiddleware": 402,
}
ITEM_PIPELINES = {
    "WebHub.pipelines.PornhubMongoDBPipeline": 403,
}

FEED_URI = u'../data/pornhub.json'
FEED_FORMAT = 'JSON'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
