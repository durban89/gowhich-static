---
title: 查看Python库的安装目录
tags:
  - Python
categories:
  - 技术
date: 2025-06-23 16:27:01
---

查看python中库的位置，其实就是几个命里行的方法

我这里的方法是：

```bash
davidzhang@192:/Library$ python
Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ftplib
>>> reload(ftplib)
<module 'ftplib' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ftplib.py'>
>>>
```

