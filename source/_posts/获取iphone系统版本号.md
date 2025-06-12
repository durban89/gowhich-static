---
title: 获取iphone系统版本号
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 17:18:38
---


为了使用版本号的问题，我搜了点资料，做点记录

```objectivec
NSLog([[UIDevice currentDevice] name]); // Name of the phone as named by user
NSLog([[UIDevice currentDevice] uniqueIdentifier]); // A GUID like string
NSLog([[UIDevice currentDevice] systemName]); // "iPhone OS"
NSLog([[UIDevice currentDevice] systemVersion]); // "2.2.1"
NSLog([[UIDevice currentDevice] model]); // "iPhone" on both devices
NSLog([[UIDevice currentDevice] localizedModel]); // "iPhone" on both devices
float version = [[[UIDevice currentDevice] systemVersion] floatValue];
if (version >= 4.0)
{
// iPhone 4.0 code here
}
```
