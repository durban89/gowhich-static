---
title: iOS 小提示 respondsToSelector
tags:
  - iOS
categories:
  - 技术
date: 2025-06-11 10:44:01
---

respondsToSelector的大概方法如下：

```objectivec
if ([NSArray respondsToSelector:@selector(arrayWithObjects:)]){
}
```

就是NSArray是否会执行arrayWithObjects:方法，一般在执行代理函数之前先这样respondsToSelector检测一下。
