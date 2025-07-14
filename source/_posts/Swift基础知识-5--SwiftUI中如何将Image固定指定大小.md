---
title: swift基础知识（5）- SwiftUI中如何将Image固定指定大小
tags:
  - Swift
categories:
  - 技术
date: 2025-07-14 14:50:42
---

SwiftUI中如何将Image固定指定大小

需求将指定图片做圆角处理，并且最终图片指定大小比如300\*300

这里给一个关于最终可以使用的代码

```cpp
Image("xxx")
            .resizable()
            .scaledToFit()
            .clipShape(Circle())
            .overlay(Circle().stroke(Color.white, lineWidth: 4))
            .shadow(radius: 10)
            .frame(maxWidth: 300, maxHeight: 300)
```

效果如如下

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1599923947/gowhich/%E6%88%AA%E5%B1%8F2020-09-12_%E4%B8%8B%E5%8D%8811.17.28.png)
