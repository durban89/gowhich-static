---
title: PHP 版本的startsWith 和 endsWith
tags:
  - PHP
categories:
  - 技术
date: 2025-07-03 11:07:53
---

JS处理字符串的时候，有些地方还是很方便的。

但是PHP也不是很逊色，也有对应的解决方案。

```php
function startsWith($haystack, $needle){
    return strncmp($haystack, $needle, strlen($needle)) === 0;
}

function endsWith($haystack, $needle){
    return $needle === '' || substr_compare($haystack, $needle, -strlen($needle)) === 0;
}
```

不理解`strcmp`和`substr_compare`的可以自己去查查文档


