---
title: Linux系统信息查看命令大全
tags:
  - Linux
categories:
  - 技术
date: 2025-06-26 11:45:15
---

最近看了一些Linux命令行的文章，在系统信息查看方面学到不少命令。 想起以前写过的一篇其实Linux这样用更简单， 发现这些系统信息查看命令也可以总结出一篇小小的东西来了。

另外这里还有非常多的命令， 可以作为参考。

#### [系统](#1)

```bash
# uname -a               # 查看内核/操作系统/CPU信息
# head -n 1 /etc/issue   # 查看操作系统版本
# cat /proc/cpuinfo      # 查看CPU信息
# hostname               # 查看计算机名
# lspci -tv              # 列出所有PCI设备
# lsusb -tv              # 列出所有USB设备
# lsmod                  # 列出加载的内核模块
# env                    # 查看环境变量
```

#### [资源](#2)

```bash
# free -m                # 查看内存使用量和交换区使用量
# df -h                  # 查看各分区使用情况
# du -sh <目录名>        # 查看指定目录的大小
# grep MemTotal /proc/meminfo   # 查看内存总量
# grep MemFree /proc/meminfo    # 查看空闲内存量
# uptime                 # 查看系统运行时间、用户数、负载
# cat /proc/loadavg      # 查看系统负载
```

#### [磁盘和分区](#3)

```bash
# mount | column -t      # 查看挂接的分区状态
# fdisk -l               # 查看所有分区
# swapon -s              # 查看所有交换分区
# hdparm -i /dev/hda     # 查看磁盘参数(仅适用于IDE设备)
# dmesg | grep IDE       # 查看启动时IDE设备检测状况
```

#### [网络](#4)

```bash
# ifconfig               # 查看所有网络接口的属性
# iptables -L            # 查看防火墙设置
# route -n               # 查看路由表
# netstat -lntp          # 查看所有监听端口
# netstat -antp          # 查看所有已经建立的连接
# netstat -s             # 查看网络统计信息
```

#### [进程](#5)

```bash
# ps -ef                 # 查看所有进程
# top                    # 实时显示进程状态
```

#### [用户](#6)

```bash
# w                      # 查看活动用户
# id <用户名>            # 查看指定用户信息
# last                   # 查看用户登录日志
# cut -d: -f1 /etc/passwd   # 查看系统所有用户
# cut -d: -f1 /etc/group    # 查看系统所有组
# crontab -l             # 查看当前用户的计划任务
```

#### [服务](#7)

```bash
# chkconfig --list       # 列出所有系统服务
# chkconfig --list | grep on    # 列出所有启动的系统服务
```

#### [程序](#8)

```bash
# rpm -qa                # 查看所有安装的软件包
```

---

参考文章：

http://tech.idv2.com/2008/01/11/linux-sysinfo-cmds/

