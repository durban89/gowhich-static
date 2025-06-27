---
title: Shell获取本机网卡ip
tags:
  - Linux
  - Shell
categories:
  - 技术
date: 2025-06-27 10:07:02
---

#### [获取本机的ip的地址（应该是内网）](#1)

第一个方法：

```bash
ifconfig $1|sed -n 2p|awk  '{ print $2 }'|awk -F : '{ print $2 }'
```

第二个方法：

```bash
ifconfig $1|sed -n 2p|awk  '{ print $2 }'|tr -d 'addr:'
```

#### [获取本机的ip的地址（应该是外网）](#2)

第一个方法：

```bash
local_host="`hostname --fqdn`"
local_ip=`host $local_host 2>/dev/null | awk '{print $NF}'`
```

第二个方法：

```bash
local_host="`hostname --fqdn`"
nslookup -sil $local_host 2>/dev/null | grep Address: | sed '1d' | sed 's/Address://g'
```

---

参考文章：

http://www.cnblogs.com/starspace/archive/2009/02/13/1390062.html

