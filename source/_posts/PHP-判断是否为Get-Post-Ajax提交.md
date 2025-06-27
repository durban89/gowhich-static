---
title: PHP 判断是否为Get/Post/Ajax提交
tags:
  - PHP
categories:
  - 技术
date: 2025-06-27 10:59:43
---

PHP 判断是否为Get/Post/Ajax提交

```php
/**
 * 是否是AJAx提交的
 * @return bool
 */
function isAjax(){
    if(isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest'){
        return true;
    }else{
        return false;
    }
}

/**
 * 是否是GET提交的
 */
function isGet(){
    return $_SERVER['REQUEST_METHOD'] == 'GET' ? true : false;
}

/**
 * 是否是POST提交
 * @return int
 */
function isPost() {
    return ($_SERVER['REQUEST_METHOD'] == 'POST' && checkurlHash($GLOBALS['verify']) && (empty($_SERVER['HTTP_REFERER']) || preg_replace("~https?:\/\/([^\:\/]+).*~i", "\\1", $_SERVER['HTTP_REFERER']) == preg_replace("~([^\:]+).*~", "\\1", $_SERVER['HTTP_HOST']))) ? 1 : 0;
}
```
