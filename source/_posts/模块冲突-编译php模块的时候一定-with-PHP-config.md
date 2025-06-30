---
title: 模块冲突 编译php模块的时候一定--with-PHP-config
tags:
  - PHP
categories:
  - 技术
date: 2025-06-30 12:01:18
---

一般的错误提示是：

```bash
NOTICE: PHP message: PHP Warning: PHP Startup: mcrypt: Unable to initialize module
```

或者

```bash
PHP Warning:  Module 'gd' already loaded in Unknown on line 0
```

当服务器中安装了2个以上的php环境时会出现以上错误,这是由于phpize编译的版本不一致，所以安装扩展的时候 一定要加上--with-php-config

```bash
/usr/local/php/bin/phpize #写全phpize的路径
./configure --with-php-config=/usr/local/php/bin/php-config  #配置时 要将php-config的路径附上
make && make install
```

上面的路径根据具体情况具体分析

