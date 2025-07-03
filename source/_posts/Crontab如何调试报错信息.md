---
title: Crontab如何调试报错信息
tags:
  - Crontab
categories:
  - 技术
date: 2025-07-03 11:59:06
---

看下面这个crontab

```bash
* * * * * /usr/bin/python /home/zhangdapeng/del.py > /dev/null 2>&1
```

一般的比较安全的，无困扰的情况下是这样的

但是调试很不方便，报错了，不知道为啥报错了，找不到原因，改一下

```bash
* * * * * /usr/bin/python /home/zhangdapeng/del.py > /path/result.log 2>&1
```

这样的话就能在result.log知道原因了。


