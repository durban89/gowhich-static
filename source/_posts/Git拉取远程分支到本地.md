---
title: Git拉取远程分支到本地
tags:
  - Git
categories:
  - 技术
date: 2025-07-02 15:39:59
---

前提是远程仓库已经存在某个分支，本地并没有对应的分支【这是情景描述前提】

对应的标题操作很简单，方法如下：

```bash
git fetch origin remote_branch:local_branch
```


