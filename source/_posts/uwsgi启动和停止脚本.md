---
title: uWSGI启动和停止脚本
tags:
  - uWSGI
categories:
  - 技术
date: 2025-06-12 11:46:37
---

一晚上写的shell的脚本

uwsgi启动和停止脚本（代码如下）：

```sh
#!/bin/bash
if [ ! -n "$1" ]
then
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
    exit 0
fi

if [ $1 = start ]
then
    psid=`ps aux | grep "uwsgi" | grep -v "grep" | wc -l`
    if [ $psid -gt 4 ]
    then
        echo "uwsgi is running!"
        exit 0
    else
        uwsgi /etc/uwsgi.ini
        echo "Start uwsgi service [OK]"
    fi
    

elif [ $1 = stop ];then
    killall -9 uwsgi
    echo "Stop uwsgi service [OK]"
elif [ $1 = restart ];then
    killall -9 uwsgi
    /usr/bin/uwsgi --ini /etc/uwsgi.ini
    echo "Restart uwsgi service [OK]"

else
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
fi
```
