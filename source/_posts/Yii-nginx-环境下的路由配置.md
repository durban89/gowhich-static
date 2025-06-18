---
title: Yii nginx 环境下的路由配置
tags:
  - PHP
  - Yii
categories:
  - 技术
date: 2025-06-17 18:57:40
---

### [Nginx配置](#1)

在nginx.conf的server {段添加类似如下代码：  
Nginx.conf代码:

```nginx
location / {
    if (!-e $request_filename){#必须有空格
        rewrite ^/(.*) /index.php last;
    }
}
```

### [在Yii的protected/conf/main.php去掉如下的注释](#2)

Php代码:

```php
'urlManager'=>array(
	'urlFormat'=>'path',
	'rules'=>array(
		'/'=>'/view',
		'//'=>'/',
		'/'=>'/',
	),
),
```
