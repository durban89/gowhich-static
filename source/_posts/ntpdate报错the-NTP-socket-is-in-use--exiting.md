---
title: ntpdate报错the NTP socket is in use, exiting
tags:
  - NTP
categories:
  - 技术
date: 2025-07-09 10:42:36
---

***ntpdate报错the NTP socket is in use, exiting***

客户端使用ntpdate与NTP服务器进行时钟同步时，报错"the NTP socket is in use, exiting"，如下：

```bash
[root@h3 vdsm]# ntpdate us.pool.ntp.org
21 Feb 03:04:30 ntpdate[19759]: the NTP socket is in use, exiting
```

原因：`ntp服务已运行`  
解决办法：

```bash
[root@h3 vdsm]# service ntpd stop
Shutting down ntpd:                                        [  OK  ]
[root@h3 vdsm]# ntpdate us.pool.ntp.org
21 Feb 03:06:55 ntpdate[19961]: step time server 192.168.0.253 offset 46.911562 sec
```

更新完之后记得重新启动ntpd

```bash
service ntpd start
```
