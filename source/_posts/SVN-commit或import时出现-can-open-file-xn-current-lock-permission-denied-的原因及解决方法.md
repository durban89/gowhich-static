---
title: "SVN commit或import时出现 can't open file 'txn-current-lock' permission denied 的原因及解决方法"
tags:
  - SVN
categories:
  - 技术
date: 2025-06-20 10:36:18
---

SVN commit或import时出现 can't open file 'txn-current-lock' permission denied 的原因及解决方法

> svn: 提交失败(细节如下):  
> svn: can't open file 'txn-current-lock' permission denied
>
> 或者
>
> svn: 提交失败(细节如下):  
> svn: Can't create directory '/usr/local/svn/repos/test/db/transactions/1-2.txn': Permission denied
>
> 这个主要原因：在svnadmin create时是root身份，所以，mod\_dav\_svn就没有write权限等。
>
> 解决办法：

```objectivec
sudo chown -R daemon /var/svnroot/yiiblog
sudo chmod -R 755 /var/svnroot/yiiblog
```
