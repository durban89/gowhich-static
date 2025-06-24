---
title: PHP-fpm 重启 关闭
tags:
  - PHP
categories:
  - 技术
date: 2025-06-24 15:29:38
---

最近在mac下面使用php，启动php的时候，php-fpm一直启动不了，不知道为什么，后来经过查找资料。是这样子的：php 5.3.3 下的php-fpm 不再支持 php-fpm 以前具有的 /usr/local/php/sbin/php-fpm(start|stop|reload)等命令，需要使用信号控制：

master进程可以理解以下信号

* ***INT,TERM  立刻终止***
* ***QUIT  平滑终止***
* ***USR1  重新打开日志文件***
* ***USR2  平滑重载所有worker进程并重新载入配置和二进制模块***

示例：

php-fpm 关闭：

```bash
kill-INT`cat/var/run/php-fpm.pid`
```

php-fpm 重启：

```bash
kill-USR2`cat/var/run/php-fpm.pid`
```

查看php-fpm进程数：

```bash
ps-ef|grepphp-fpm
```

