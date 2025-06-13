---
title: iOS设备 获取Model（设备型号）、Version（设备版本号）、app（程序版本号）
tags:
  - iOS
categories:
  - 技术
date: 2025-06-13 15:33:00
---

最近想到了这些的东西，就去google搜索了一下，结果还真有，哈，知识在于发现，代码贴到下面了：

```objectivec
NSLog(@"uniqueIdentifier: %@", [[UIDevice currentDevice] uniqueIdentifier]);
NSLog(@"name: %@", [[UIDevice currentDevice] name]);
NSLog(@"systemName: %@", [[UIDevice currentDevice] systemName]);
NSLog(@"systemVersion: %@", [[UIDevice currentDevice] systemVersion]);
NSLog(@"model: %@", [[UIDevice currentDevice] model]);
NSLog(@"localizedModel: %@", [[UIDevice currentDevice] localizedModel]);

NSDictionary *infoDictionary = [[NSBundle mainBundle] infoDictionary];

CFShow(infoDictionary);

// app名称
NSString *app_Name = [infoDictionary objectForKey:@"CFBundleDisplayName"];

// app版本
NSString *app_Version = [infoDictionary objectForKey:@"CFBundleShortVersionString"];

// app build版本
NSString *app_build = [infoDictionary objectForKey:@"CFBundleVersion"];
```
