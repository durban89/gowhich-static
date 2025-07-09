---
title: Yii2 how get domain name(Yii2如何获取域名)
tags:
  - PHP
  - Yii
categories:
  - 技术
date: 2025-07-09 10:42:08
---

使用Yii2的都是知道如何使用hostInfo获取域名地址，这个域名地址我解释为域名信息，是包括schema，大家可以去看下URL 中的schema是什么意思，网上搜索了好多  
搜索关键字`yii2 get domain name`结果给出来的都是带有schema的结果

我这里使用的twig模板，调用方式如下

```php
{{ app.request.hostName }} // 如果访问https://www.gowhich.com 则得到的结果是 www.gowhich.com
{{ app.request.hostInfo }} // 如果访问https://www.gowhich.com 则得到的结果是 https://www.gowhich.com
```

