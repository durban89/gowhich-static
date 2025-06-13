---
title: PHP针对iPhone和Android设备输出不同的viewport
tags:
  - PHP
  - iOS
  - Android
categories:
  - 技术
date: 2025-06-13 10:13:12
---

PHP针对iPhone和Android设备输出不同的viewport

```php
<?php
//if iphone
$browser = strpos($_SERVER['HTTP_USER_AGENT'], "iPhone");
if (true == $browser) {
    $browser = 'iphone';
}

//if android
$android = strpos($_SERVER['HTTP_USER_AGENT'], "Android");
if (true == $android) {
    $brower = 'android';
}
```

html模版

```php
<?php if ($browser == 'iphone') { ?>
  <meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
<?php } elseif ($brower == 'android') { ?>
  <meta name="HandheldFriendly" content="true" />
  <meta name="viewport" content="width=device-width, height=device-height, user-scalable=no" />
<?php } ?>
```
