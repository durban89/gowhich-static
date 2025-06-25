---
title: Python 函数参数中*（一个星）和**（两个星）的作用和区别
tags:
  - Python
categories:
  - 技术
date: 2025-06-25 10:09:26
---

一直对python函数中的参数有个迷惑，最近在学习中，发现了“在函数中接收元组和列表”的是时候明白了其代表的意思

一个星（\*）：表示接收的参数作为元组来处理

两个星（\*\*）：表示接收的参数作为字典来处理

在这里举个例子

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#!Filename: powersum.py
__author__ = 'Durban Zhang'
def powersum(power, *args):
    '''Return the sum of each argument raised to specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total
print powersum(2,3,4)
print powersum(2,10)
```

得到的结果是：

```bash
davidzhang@192:~/python/python_project/other_example$ ./powersum.py 
25
100
```

实现参数动态化方法的不错实例

