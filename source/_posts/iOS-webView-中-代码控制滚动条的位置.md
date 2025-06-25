---
title: iOS webView 中 代码控制滚动条的位置
tags:
  - iOS
categories:
  - 技术
date: 2025-06-25 11:34:35
---

得到当前webView 中 Scroll的坐标

```objectivec
int scrollPosition = [[DataWebView stringByEvaluatingJavaScriptFromString:@"window.pageYOffset"] intValue];
```

得到当前webView页

```objectivec
int sizePage = [[DataWebView stringByEvaluatingJavaScriptFromString:@"document.getElementById(\"foo\").offsetHeight;"] intValue];
```

跳到你指定的位置

```objectivec
[DataWebView stringByEvaluatingJavaScriptFromString: [NSString stringWithFormat:@"window.scrollBy(0,%d);", 200] ];
```

`0，200`改为你所要改的坐标

