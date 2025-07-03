---
title: 如何检测javascript的变量是 undefined，防止终止js运行
tags:
  - JavaScript
categories:
  - 技术
date: 2025-07-03 11:08:29
---

为了防止未定义的变量，导致程序运行失败，需要我们判断下变量是否未undefined

```js
typeof(decryptData) != "undefined" ? decryptData.payResult : ''
```

这里还是个对象的值，想想如果不是undefined，但是没有payResult的情况吧。

