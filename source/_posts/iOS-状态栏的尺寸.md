---
title: iOS 状态栏的尺寸
tags:
  - iOS
categories:
  - 技术
date: 2025-06-11 11:06:58
---

状态栏尺寸的获取方式：

```objectivec
CGRect statusFrame;
statusFrame = [[UIApplication sharedApplication] statusBarFrame];
CGFloat statusHeight = statusFrame.size.height;
CGFloat statusWidth = statusFrame.size.width;
```
