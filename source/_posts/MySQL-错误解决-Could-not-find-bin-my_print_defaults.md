---
title: MySQL 错误解决“Could not find ./bin/my_print_defaults”
tags:
  - MySQL
categories:
  - 技术
date: 2025-06-27 10:59:23
---

Mysql 错误解决“Could not find ./bin/my\_print\_defaults”

运行下面这条语句就可以搞定了。

```zsh
sudo mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data &
```
