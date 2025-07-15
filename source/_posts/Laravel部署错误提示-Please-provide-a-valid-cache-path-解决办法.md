---
title: Laravel部署错误提示“Please provide a valid cache path.”解决办法
tags:
  - Laravel
categories:
  - 技术
date: 2025-07-15 10:28:35
---

laravel部署错误提示“Please provide a valid cache path.”解决办法

解决方法如下：

1、确保`storage`目录下有如`app`，`framework`，`views`三个目录。

2、确保`storage/framework`目录下也有`cache`，`sessions`，`views`三个目录。

缺少以上目录就手动创建，然后访问网站首页试试。
