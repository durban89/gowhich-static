---
title: nginx ssl 配置
tags:
  - NGINX
categories:
  - 技术
date: 2025-07-11 11:16:12
---

ssl证书获取

免费的渠道 https://certbot.eff.org/

也可以去云平台获取 比如阿里云、腾讯云也有免费的

先说下 ssl/dhparam.pem 这个文件如何获取

**如何生成 dhparam.pem 文件**

在命令行执行任一方法:

方法1: 很慢

```bash
openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048
```

方法2: 较快 - 与方法1无明显区别. 2048位也足够用, 4096更强

```bash
openssl dhparam -dsaparam -out /etc/nginx/ssl/dhparam.pem 4096
```

参考 https://gist.github.com/fotock/9cf9afc2fd0f813828992ebc4fdaad6f
