---
title: 'Error: "DEVELOPER_DIR" is not defined at ./symbolicatecrash line 53.'
tags:
  - PHP
categories:
  - 技术
date: 2025-06-20 11:50:30
---

项目问题解析“Error: "DEVELOPER_DIR" is not defined at ./symbolicatecrash line 53.”这个问题是最近调试app的时候出现的，因为自己提交的app遭到拒绝，需要调试，在使用symbolicatecrash的时候出现了问题。

在这里的解决办法是：

在不关闭当前终端的情况下，输入：

```bash
export DEVELOPER_DIR="/Applications/XCode.app/Contents/Developer"
```

然后再试试就可以了。
