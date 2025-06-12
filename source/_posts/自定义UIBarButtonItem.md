---
title: 自定义UIBarButtonItem
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 17:18:50
---

因为按钮的要求，好友导航的限制，想着自己自定义一个barbuttonitem，如下

```objectivec
self.leftBtn = [UIButton buttonWithType:UIButtonTypeCustom];
[self.leftBtn setFrame:CGRectMake(10.0, 5.0, 70.0, 30.0)];
[self.leftBtn setContentHorizontalAlignment:UIControlContentHorizontalAlignmentCenter];
[self.leftBtn setTitle:@"返回" forState:UIControlStateNormal];
[self.leftBtn setTitleColor:[UIColor whiteColor] forState:UIControlStateNormal];
[self.leftBtn setTintColor:[UIColor redColor]];
//    [self.leftBtn setImage:[UIImage imageNamed:@"back_60_30"] forState:UIControlStateNormal];

self.leftBtn.layer.cornerRadius = 10.0;
self.leftBtn.layer.borderWidth = 1.0;

[self.leftBtn addTarget:self
           action:@selector(returnToPrev)
 forControlEvents:UIControlEventTouchUpInside];
[self.leftBtn setTag:1];
[self.navigationBar addSubview:self.leftBtn];
```
