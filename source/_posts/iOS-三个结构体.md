---
title: iOS 三个结构体
tags:
  - PHP
categories:
  - 技术
date: 2025-06-11 10:47:17
---

**三个结构体：CGPoint、CGSize、CGRect**

1. CGPoint

```objectivec
/* Points. */    
struct CGPoint {    
  CGFloat x;    
  CGFloat y;    
};    
typedef struct CGPoint CGPoint;
```

2. CGSize

```objectivec
/* Sizes. */    
struct CGSize {    
  CGFloat width;    
  CGFloat height;    
};    
typedef struct CGSize CGSize;
```

3.CGRect

```objectivec
/* Rectangles. */    
struct CGRect {    
  CGPoint origin;//偏移是相对父窗口的    
  CGSize size;    
};    
typedef struct CGRect CGRect;
```

这三个结构体均在一个头文件里：CGGeometry.h
