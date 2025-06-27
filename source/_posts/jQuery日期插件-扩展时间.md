---
title: jQuery日期插件，扩展时间
tags:
  - jQuery
categories:
  - 技术
date: 2025-06-27 14:14:19
---

第一步，导入需要的文件

```html
<link rel="stylesheet" href="//code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css" />
<link rel="stylesheet" href="/wap/js/jquery.datetimepicker/jquery-ui-timepicker-addon.min.css" />
<script src="//code.jquery.com/ui/1.10.4/jquery-ui.js"></script>
<script src="/wap/js/jquery.datetimepicker/jquery-ui-timepicker-addon.min.js"></script>
```

第二步，配置

```js
$( "#starttime" ).datetimepicker({ dateFormat: "yy-mm-dd" });
$( "#endtime" ).datetimepicker({ dateFormat: "yy-mm-dd" });
```


