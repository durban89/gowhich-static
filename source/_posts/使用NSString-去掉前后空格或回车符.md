---
title: 使用NSString 去掉前后空格或回车符
tags:
  - iOS
categories:
  - 技术
date: 2025-06-19 10:29:24
---

想要去掉字符串的前后空格和回车符，很简单，如下：

```objectivec
NSString *string = @" spaces in front and at the end ";
NSString *trimmedString = [string stringByTrimmingCharactersInSet:
[NSCharacterSet whitespaceAndNewlineCharacterSet]]; 
NSLog(trimmedString);
```
