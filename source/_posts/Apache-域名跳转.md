---
title: Apache 域名跳转
tags:
  - Apache
categories:
  - 技术
date: 2025-06-27 14:13:59
---

如果想要实现访问jingguan.365use.com时，跳转到<http://www.landscapemedia.cn ，可以做如下操作>

```bash
<VirtualHost *:80>
    ServerName jingguan.365use.com
    RewriteEngine on
    RewriteCond %{HTTP_HOST} ^jingguan.365use.com  [NC]
    RewriteRule ^(.*) http://www.landscapemedia.cn$1 [R=permanent,L]
</VirtualHost>
```

