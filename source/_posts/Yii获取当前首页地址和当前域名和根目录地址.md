---
title: Yii获取当前首页地址和当前域名和根目录地址
tags:
  - PHP
  - Yii
categories:
  - 技术
date: 2025-06-19 09:58:12
---

### [当前域名](#1)

```php
echo Yii::app()->request->hostInfo;
```

### [除域名外的URL](#2)

```php
echo Yii::app()->request->getUrl();
```

### [除域名外的首页地址](#3)

```php
echo Yii::app()->user->returnUrl;
```

### [除域名外的根目录地址](#4)

```php
echo Yii::app()->homeUrl;
```
