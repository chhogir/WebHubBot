from scrapy import cmdline

cmdline.execute(
    "echo > /root/PyProject/py2/projects/WebHub/logs/cataline.log".split())
cmdline.execute("scrapy crawl pornHubSpider".split())
