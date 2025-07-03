---
title: uglify error log 处理
tags:
  - UglifyJS
categories:
  - 技术
date: 2025-07-03 11:07:30
---

使用uglify在做js的处理过程中，会遇到js的各种问题，而导致uglify自己报错，但是往往我们不知道具体是哪个文件的js报错了。

这样情况下

```js
uglify().on('error', gutil.log)
```

gulp-util就能很好的解决我们的问题。

