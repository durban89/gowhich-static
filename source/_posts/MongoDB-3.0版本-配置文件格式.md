---
title: MongoDB 3.0版本 配置文件格式
tags:
  - MongoDB
categories:
  - 技术
date: 2025-07-01 11:54:27
---

配置文件的格式变了

是这样子的啦：

```bash
systemLog:
   destination: file
   path: "/var/log/mongodb/mongodb.log"
   logAppend: true
storage:
   journal:
      enabled: trueprocessManagement:
   fork: true
net:
   bindIp: 127.0.0.1
   port: 27017
setParameter:
   enableLocalhostAuthBypass: false
   
...
```

如果想要添加其他参数，请到这里查看吧：http://docs.mongodb.org/manual/reference/configuration-options/


