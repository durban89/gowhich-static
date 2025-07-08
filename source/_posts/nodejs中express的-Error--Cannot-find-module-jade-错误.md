---
title: "nodejs中express的“Error: Cannot find module 'jade'”错误"
tags:
  - NodeJS
categories:
  - 技术
date: 2025-06-17 17:01:09
---

安装express之后访问http://localhost:8080 。

会出现500 Error: Cannot find module 'jade'错误

解决方案：  
确定package.json里有添加相应的jade依赖配置

使用npm install -d 可以自动配置package.json，并安装所有需要依赖的包

命令行下执行：

```bash
npm install -d
```
