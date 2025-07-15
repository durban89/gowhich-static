---
title: Curl模拟Get、Post、Put、Delete请求
tags:
  - CURL
categories:
  - 技术
date: 2025-07-15 10:28:41
---

GET

```bash
curl -v www.xxx.com/xxx/xxx/xx
```

POST

```bash
curl -v www.aaa.com/xxx/xxxx -d 'xx=14&xxx=xxx'
curl -v -X POST www.aaa.com/xxxx -d 'xx=14&xxx=ddd'
```

PUT

```bash
curl -v -X PUT -d "xx=19&xx=C" www.xx.com/ss/ss
```

DELETE

```bash
curl -v -X DELETE www.xx.com/xx/sss
```

如何添加HEADER

```bash
curl -v -H 'ApiKey:xxx' -H 'Sign:xxx' -H 'RequestTime:xxx' -H 'Content-Type:application/json' -H 'User-Agent:PostmanRuntime/7.26.10' -H 'Accept:*/*' -H 'Accept-Encoding:gzip, deflate, br' -H 'Connection:keep-alive' -X POST www.xx.com/test/xxxx -d '{"xxx":"xxx","dd":"1"}'
```
