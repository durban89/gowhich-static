---
title: 通过ps、grep和kill批量杀死进程
tags:
  - Linux
categories:
  - 技术
date: 2025-07-01 11:36:15
---

这两天Node的程序kill到手都软了，网上查了一个很好的方法，直接拿来用了。

功能：杀死进程名称中包含node的所有进程

```bash
ps -ef | grep node | awk '{print $2}' | xargs kill -9
```


