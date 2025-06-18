---
title: UIActivityIndicatorView简单的使用方法
tags:
  - iOS
categories:
  - 技术
date: 2025-06-17 18:57:52
---

关于UIActivityIndicatorView的简单的使用方法，最近突然就学会了，这个要归咎于，要多看别人的东西，多用用别人的东西，就能学到很多。

第一步：属性声明

```objectivec
@property (retain, nonatomic) UIActivityIndicatorView *indicatorView;
```

第二步：实现过程

```objectivec
indicatorView = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle:UIActivityIndicatorViewStyleGray];
indicatorView.autoresizingMask =
UIViewAutoresizingFlexibleTopMargin | UIViewAutoresizingFlexibleBottomMargin
| UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleRightMargin;
[self.view addSubview:indicatorView];

[indicatorView sizeToFit];
[indicatorView startAnimating];
indicatorView.center = weiboLoginWeb.center;
```
