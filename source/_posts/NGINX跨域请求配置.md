---
title: NGINX跨域请求配置
tags:
  - NGINX
categories:
  - 技术
date: 2025-07-14 14:45:04
---

nginx跨域请求配置

同域名，如果相互访问其子域名的时候，比如h5.xx.com要访问api.xx.com，如果在h5.xx.com页面中访问api.xx.com的话，就会遇到跨域的问题

解决办法，在代码端也是可以解决的

通过设置

1. Access-Control-Allow-Origin
2. Access-Control-Allow-Headers
3. Access-Control-Allow-Methods

不过今天这里要说的是在nginx层面做处理

在conf中添加如下配置

```ini
add_header Access-Control-Allow-Origin *;
add_header Access-Control-Allow-Headers X-Requested-With;
add_header Access-Control-Allow-Methods GET,POST,OPTIONS;
```
