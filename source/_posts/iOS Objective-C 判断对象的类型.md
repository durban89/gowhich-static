---
title: iOS Objective-C 判断对象的类型
tags:
  - iOS
categories:
  - 技术
date: 2025-06-10 15:29:18
---

所有继承 NSObject 的的对象可以调用isKindOfClass 方法

```objectivec
(BOOL)isKindOfClass:(Class)aClass
```

例如:

```objectivec
BOOL test = [obj isKindOfClass:[SomeClass class]];
```

