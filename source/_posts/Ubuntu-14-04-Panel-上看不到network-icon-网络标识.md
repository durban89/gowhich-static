---
title: Ubuntu 14.04  Panel 上看不到network icon[网络标识]
tags:
  - Ubuntu
categories:
  - 技术
date: 2025-06-30 15:15:42
---

之前有写过一篇类似的文章，但是如果你安装了google的话，会依然有这种问题出现，主要问题是,在安装google的时候他卸载了**indicator-application**，所以网络标识消失了，就连输入法或者其他的第三方的标识也没有了。解决的办法就是重新安装回来就好了。

```bash
sudo apt-get install indicator-application
```


