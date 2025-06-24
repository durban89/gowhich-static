---
title: mac关闭指定端口
tags:
  - Unix
  - MacOS
categories:
  - 技术
date: 2025-06-11 11:06:53
---

先执行如下命令:

```sh
lsof -i:端口号
```

会有类似下面的结果：

```shell
COMMAND     PID       USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
WebProces 42624 davidzhang    5u  IPv4 0x907152bbf7b2a875      0t0  TCP localhost:64438->localhost:radan-http (ESTABLISHED)
WebProces 42624 davidzhang   10u  IPv4 0x907152bbf7b64a05      0t0  TCP localhost:64439->localhost:radan-http (ESTABLISHED)
```

然后执行：

```sh
kill -9 42624
```

结束进程就搞定了
