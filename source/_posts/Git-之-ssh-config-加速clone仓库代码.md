---
title: Git 之 ssh config 加速clone仓库代码
tags:
  - Git
categories:
  - 技术
date: 2025-07-03 16:50:12
---

代码记录如下

```bash
Host github.com
    User git
    Hostname ssh.github.com
    Port 443
    ProxyCommand connect -S 127.0.0.1:1180 %h %p
Host bitbucket.org
    User git
    Hostname altssh.bitbucket.org
    Port 443
    ProxyCommand connect -S 127.0.0.1:1180 %h %p
```

操作方式是这里用到了connect 这个功能，所以为了为了使用这个功能，前提是安装connect

```bash
brew install connect
```
