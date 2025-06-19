---
title: iOS 根据内容计算高度
tags:
  - iOS
categories:
  - 技术
date: 2025-06-19 10:29:01
---

iOS 根据内容计算高度,网络上搜索到的，自己记录下，看到的就看到了

第一步属性声明

```objectivec
@property (strong, nonatomic) NSString *personProfile
```

第二步属性赋值

```objectivec
self.personProfile = @"xxxxxxxxxxxxxxxx x x x  x x xx x ";
```

第三步求出高度

```objectivec
//根据内容计算高度
CGSize lineSize = [self.personProfile sizeWithFont:[UIFont systemFontOfSize:14]
                         constrainedToSize:CGSizeMake(240, 2000)
                             lineBreakMode:UILineBreakModeWordWrap];

NSLog(@" lineSize.height = %f", lineSize.height);
```
