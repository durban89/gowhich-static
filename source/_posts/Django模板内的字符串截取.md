---
title: Django模板内的字符串截取
tags:
  - Django
categories:
  - 技术
date: 2025-06-20 10:31:49
---

django模板内的字符串截取

1,变量前30个字符,用于中文不行

```html
{{ content |truncatewords:"30"}}
```

取变量前500个字符，可用于中文

```html
{{ content |slice:"30" }} 
```
