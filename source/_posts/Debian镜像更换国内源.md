---
title: Debian镜像更换国内源
tags:
  - Debian
categories:
  - 技术
date: 2025-07-04 11:47:58
---

以Jessie为例, 编辑/etc/apt/sources.list文件, 在文件最前面添加以下条目(操作前请做好相应备份)

```bash
deb http://mirrors.163.com/debian/ jessie main non-free contrib
deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib
deb http://mirrors.163.com/debian/ jessie-backports main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie-updates main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie-backports main non-free contrib
deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
deb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
```

或者下载相应版本的sources.list, 覆盖/etc/apt/sources.list即可(操作前请做好相应备份)

转载：http://mirrors.163.com/.help/debian.html
