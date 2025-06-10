---
title: Yii框架关于时区的设置
tags:
  - Yii
  - PHP
categories:
  - 技术
date: 2025-06-10 12:03:43
---

时区设置方法：  
- 在php.ini 文件中添加

```
date.timezone = "Asia/Chongqing"
```

- 或者 php中处理代码时候 需要 `echo gmdate('Y-m-d H:m:s', time()+8\*3600)`;

- 在php脚本中加入代码 `date\_default\_timezone\_set("Asia/Shanghai")`;

- 最简便的方法，在`config/main.php` 里

```
return [
    'timeZone' => 'Asia/Chongqing',
];
```
