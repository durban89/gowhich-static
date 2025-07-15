---
title: "MongoDB小知识 - MongoDB Sort : how to fix maximum RAM exceeded error"
tags:
  - MongoDB
categories:
  - 技术
date: 2025-07-15 09:51:32
---

**MongoDB Sort : how to fix maximum RAM exceeded error**

针对这个问题具体的报错信息如下

> Error: error: {  
> "ok" : 0,  
> "errmsg" : "Executor error during find command :: caused by :: errmsg: \"Sort operation used more than the maximum 33554432 bytes of RAM. Add an index, or specify a smaller limit.\"",  
> "code" : 96,  
> "codeName" : "OperationFailed"  
> }

解决办法：

1、加索引（这个是比较常用的方式）

2、增加RAM大小

```bash
db.adminCommand({setParameter: 1, internalQueryExecMaxBlockingSortBytes: 335544320})
```

具体的大小可以根据具体的情况来设置

查看RAM大小的话，使用下面的命令

```bash
db.runCommand( { getParameter : 1, "internalQueryExecMaxBlockingSortBytes" : 1 } )
```

3、使用*aggregate* 命令

如果用*aggregate*的话，通过设置选项allowDiskUse的值为true，允许临时将数据写到文件中，具体使用参考如下

```bash
db.getCollection('users').aggregate( [
      { $sort : { age : 1} }
   ],
   { allowDiskUse: true }
)
```

如果在排序的时候想要得到一个好的性能，最好是创建索引

```bash
db.users.createIndex( { age: 1 } )
```

参考文章点[击这里](https://developerslogblog.wordpress.com/2019/11/27/mongodb-sort-how-to-fix-maximum-ram-exceeded-error/)
