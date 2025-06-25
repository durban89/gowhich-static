---
title: Python中的储存器的使用
tags:
  - Python
categories:
  - 技术
date: 2025-06-25 09:58:00
---

python中这个储存器功能，还是蛮特别的

dump函数，实现了存储，load实现了读取，Objective-C语言的encode和php的数组序列化是差不多的

gowhich邀您看看下面简单的实例：

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#!Filename: pickling
__author__ = 'Durban Zhang'
import cPickle as p
shoplistfile = 'shoplist.data'
shoplist = ['apple','banana','carrot']
f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()
del shoplist
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
```

