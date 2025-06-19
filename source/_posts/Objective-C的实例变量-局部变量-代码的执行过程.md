---
title: Objective-C的实例变量，局部变量，代码的执行过程
tags:
  - Objective-C
categories:
  - 技术
date: 2025-06-19 10:29:17
---

实例变量是在类里面的变量  
比如：

```objectivec
@implementation FindPerformersViewController{
    int i;
}
```

i就是实例变量

局部变量是在方法里面的变量  
比如：

```objectivec
-(void) getVariable {
    int i = 0;
}
```

这里的i就是局部变量
