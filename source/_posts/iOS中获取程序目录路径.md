---
title: iOS中获取程序目录路径
tags:
  - iOS
categories:
  - 技术
date: 2025-06-10 15:46:19
---

### [获取程序Documents目录路径](#1)

```objectivec
NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory,NSUserDomainMask, YES);
NSString *documentsDirectory = [paths objectAtIndex:0];
```

### [获取程序app文件所在目录路径](#2)

```objectivec
NSHomeDirectory();
```

### [获取程序tmp目录路径](#3)

```objectivec
NSTemporaryDirectory();
```

### [获取程序应用包路径](#4)

```objectivec
[[NSBundle mainBundle] resourcePath];
```

或

```objectivec
[[NSBundle mainBundle] pathForResource: @"info" ofType: @"txt"];
```

来源：http://www.cnblogs.com/kaixuan/archive/2011/05/31/2064796.html

