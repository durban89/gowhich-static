---
title: JavaScript 日期时间戳转换
tags:
  - JavaScript
categories:
  - 技术
date: 2025-07-02 16:01:06
---

日期转时间戳

```js
var date = '2016/05/09';
date = [date, '00:00:00'].join(' ')
date = Math.round(new Date(date).valueOf() / 1000);
```

//以上是我觉得兼容性比较强的

时间戳转日期

```js
new Date().toLocaleString()
```


