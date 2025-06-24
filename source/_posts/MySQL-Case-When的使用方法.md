---
title: MySQL Case When的使用方法
tags:
  - MySQL
categories:
  - 技术
date: 2025-06-24 15:04:22
---

关于Mysql Case When的使用方法，官方文档是这样写的

```sql
CASE case_value
    WHEN when_value THEN statement_list
    [WHEN when_value THEN statement_list] ...
    [ELSE statement_list]
END CASE
```

OR

```sql
CASE
    WHEN search_condition THEN statement_list
    [WHEN search_condition THEN statement_list] ...
    [ELSE statement_list]
END CASE
```

有个注意事项是这样的：

> Note
>
> There is also a CASE expression, which differs from the CASE statement described here. See Section 12.4, “Control Flow Functions”. The CASE statement cannot have an ELSE NULL clause, and it is terminated with END CASE instead of END.

原文地址：<http://dev.mysql.com/doc/refman/5.6/en/case.html>

下面列举几个经常使用的方法

第一个：

```sql
select name,  
 case   
        when birthday<'1981' then 'old'  
        when birthday>'1988' then 'yong'  
        else 'ok' END YORN  
from lee;
```

第二个：

```sql
select NAME,  
 case name  
     when 'sam' then 'yong'  
        when 'lee' then 'handsome'  
        else 'good' end  
from lee;
```

第三个：

```sql
select name,birthday,  
 case   
     when birthday>'1983' then 'yong'  
        when name='lee' then 'handsome'  
        else 'just so so ' end  
from lee;
```

