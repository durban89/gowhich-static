---
title: PHP POST 提交 JSON 数据（data）
tags:
  - PHP
categories:
  - 技术
date: 2025-06-26 11:45:12
---

记录一下，php通过curl提交json数据的方法

```php
if ($sandbox != 0) {
	$serviceURL = 'https://sandbox.itunes.apple.com/verifyReceipt';
} else {
	$serviceURL = 'https://buy.itunes.apple.com/verifyReceipt';
}

$ch = curl_init ( $serviceURL );
curl_setopt ( $ch, CURLOPT_CUSTOMREQUEST, "POST" );
curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, true );
curl_setopt ( $ch, CURLOPT_POSTFIELDS, $data );
curl_setopt ( $ch, CURLOPT_SSL_VERIFYPEER, false );
curl_setopt ( $ch, CURLOPT_SSL_VERIFYHOST, false );
curl_setopt ( $ch, CURLOPT_HTTPHEADER, array (
		'Content-Type:application/json',
		'Content-Length: ' . strlen ( $data ) 
) );
$result = curl_exec ( $ch );
$errorNo = curl_errno ( $ch );
curl_close ( $ch );
```

---

参考文章：

http://www.qingliangcn.com/2013/05/php-post-json-data/

