---
title: jQuery 实现 保持滚动条一直在底部
tags:
  - jQuery
categories:
  - 技术
date: 2025-07-01 11:35:56
---

**jquery 实现 保持滚动条一直在底部**

```js
var e = $('#import-bill');  
e.scrollTop = e.scrollHeight;//让滚动条自动滚动顶部
$("#import-bill").scrollTop($("#import-bill")[0].scrollHeight);
```


