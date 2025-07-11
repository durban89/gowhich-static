---
title: Laravel Security Release 6.18.34, 7.23.2
tags:
  - PHP
  - Laravel
categories:
  - 技术
date: 2025-07-11 11:15:53
---

Security Release: Laravel 6.18.34, 7.23.2

By Taylor Otwell  
Time Aug, 6 2020

在Laravel的早期版本中，可以批量分配包含模型表名的Eloquent属性：

```php
$model->fill(['users.name' => 'Taylor']);
```

这样做时，Eloquent会为您从属性中删除表名。这是Eloquent的“便利”功能，没有记录。

但是，与验证配对时，这可能导致意外的和未经验证的值被保存到数据库中。因此，我们从批量分配操作中删除了对表名的自动剥离，以使属性通过典型的“可填充” /“受保护”逻辑。包含未明确声明为可填充的表名的任何属性都将被丢弃。

对于在批量分配期间依赖未记录的表名称剥离的应用程序，此安全版本将是一项重大更改。

原文地址：  
https://blog.laravel.com/security-release-laravel-61834-7232
