---
title: 国内解决github访问慢的办法
tags:
  - Github
categories:
  - 技术
date: 2025-07-01 11:53:20
---

github 慢, 或者说是它的资源 host 被堵而已, 大家可以通过简单的 hosts 映射解决:

```bash
185.31.16.184 github.global.ssl.fastly.net
```

原因是这样的吧： http://weibo.com/1415338244/ACTYkq8xK


