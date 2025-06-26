---
title: "iOS7 - 如何在Objective C中创建一个空白的透明PNG"
tags:
  - iOS
categories:
  - 技术
date: 2025-06-26 14:55:13
---

google后的结果很神奇，这里就是一小段的代码

```objectivec
UIGraphicsBeginImageContextWithOptions(CGSizeMake(36, 36), NO, 0.0); 
UIImage *blank = UIGraphicsGetImageFromCurrentImageContext(); 
UIGraphicsEndImageContext();
```

---

参考文章

http://www.16kan.com/question/detail/109385.html

