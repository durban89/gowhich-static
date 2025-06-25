---
title: Python assert 和 repr小实例
tags:
  - Python
categories:
  - 技术
date: 2025-06-25 10:09:29
---

关于assert和repr的使用，对我来说还是很迷糊，于是有搜索了一些资料进行了整理

```python
#!/usr/bin/env python
#!-*-coding=utf-8-*-
#!Filename:more_example.py
#assert 实例
#assert语句用来声明某个条件是真的
mylist = ['items']
assert len(mylist) >= 1
mylist.pop()
try:
    assert len(mylist) >= 1
except Exception:
    print 'AssertionError assert 报错'
#repr实例
#repr函数用来取得对象的规范字符串表示。反引号（也称转换符）可以完成相同的功能。
>>> i  = []
>>> i.append('item')
>>> i
['item']
>>> `i`
"['item']"
>>> repr(i)
"['item']"
>>>
```

虽然简短，但是我觉得容易理解
