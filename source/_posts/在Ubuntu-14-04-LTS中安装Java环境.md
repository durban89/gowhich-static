---
title: 在Ubuntu 14.04 LTS中安装Java环境
tags:
  - Ubuntu
  - Linux
categories:
  - 技术
date: 2025-06-30 15:15:56
---

对于开发Android应用，jSP开发的同学，福利来了，这里有如何安装Oracle的JDK了。

方法很简单，不需要自己去下载源码进行安装，这样就确保了各个方面的安全。

安装过程如下：

```bash
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo apt-get install oracle-java8-set-default
```

如果想安装7的话将java8改为java7。安装完之后，执行命令看下吧。

```bash
java --version
```


