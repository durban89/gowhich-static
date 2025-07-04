---
title: Yii Framework中关于Session
tags:
  - PHP
  - Yii
categories:
  - 技术
date: 2025-06-20 14:13:49
---

首先，在Yii框架中，你不需要像标准PHP代码那样使用`session_start()`,  
在Yii框架中，autoStart 属性缺省被设置为true，所以，  
虽然没有使用`session_start()`,你仍然可以使用`$_SESSION`全局变量，但最好使用  
Yii框架封装的`Yii::app->session`:  
  
设置session变量：

```php
Yii::app()->session['var']='value';
```

使用：`Yii::app()->session['var'];`

移除：`unset(Yii::app()->session['var']);`  
  
更为复杂一点的使用时如何配置你的session  
配置项可设在 protected/config/main.php的components中：

```php
'session'=>array(
   'autoStart'=>false(/true),
   'sessionName'=>'Site Access',
   'cookieMode'=>'only',
   'savePath'='/path/to/new/directory',
),
```

将session保持在数据库的设置：

```php
'session' => array (
    'class' => 'system.web.CDbHttpSession',
    'connectionID' => 'db',
    'sessionTableName' => 'actual_table_name',
),
```

好，还有什么呢？对了，为了调试，有时需要知道当前用户的session ID,  
该值就在 Yii::app()->session->sessionID 中。  
  
最后，当用户退出登录(logout),你需要消除痕迹，可使用：  
`Yii::app()->session->clear()`移去所有session变量，然后，调用  
`Yii::app()->session->destroy()`移去存储在服务器端的数据。
