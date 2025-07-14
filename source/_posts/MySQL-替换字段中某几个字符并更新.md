---
title: MySQL 替换字段中某几个字符并更新
tags:
  - MySQL
categories:
  - 技术
date: 2025-07-14 16:28:12
---

mysql 替换字段中某几个字符并更新

```sql
UPDATE `database`.`table` 
SET `column` = REPLACE(column,'旧字符串','新字符串');
```
