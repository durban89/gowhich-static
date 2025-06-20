---
title: Objective-C中NSString与int和float的相互转换.md
tags:
  - Objective-C
categories:
  - 技术
date: 2025-06-12 17:44:47
---

```objectivec
NSString *tempA = @"123";
NSString *tempB = @"456";
```

### [字符串拼接](#1)

```objectivec
NSString *newString = [NSString stringWithFormat:@"%@%@",tempA,tempB];
```

### [字符转int](#2)

```objectivec
int intString = [newString intValue];
```

### [int转字符](#3)

```objectivec
NSString *stringInt = [NSString stringWithFormat:@"%d",intString];
```

### [字符转float](#4)

```objectivec
float floatString = [newString floatValue];
```

### [float转字符](#5)

```objectivec
NSString *stringFloat = [NSString stringWithFormat:@"%f",intString];
```
