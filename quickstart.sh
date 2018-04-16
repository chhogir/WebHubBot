#! /bin/sh

# 等号两边不能有空格
# ENV=py2
# source $WORKON_HOME/$ENV/bin/activate
# nohup ./quickstart.sh >/dev/null 2>&1 &  


export WORKON_HOME=$HOME/PyProject
source /usr/bin/virtualenvwrapper.sh


echo > /root/PyProject/py2/projects/WebHub/logs/cataline.log

workon py2

cd /root/PyProject/py2/projects/WebHub/WebHub

scrapy crawl pornHubSpider

deactivate
