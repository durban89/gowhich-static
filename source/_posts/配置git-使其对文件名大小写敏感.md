---
title: 配置Git 使其对文件名大小写敏感
tags:
  - Git
categories:
  - 技术
date: 2025-07-02 16:00:43
---

执行如下代码：

```bash
git config core.ignorecase false
```

另外一个问题

当我们遇到文件大小写的时候，当在编辑器改完之后，提交代码，实际上仓库中并没有改变这个文件的大小写，可以通过下面的方式来修改

```bash
git mv A B
```

实例演示如下，如果我有个文件是

components/StatCNZZWidget.php

想要修改为

components/StatCnzzWidget.php

执行如下代码

```bash
$ git mv components/StatCNZZWidget.php components/StatCnzzWidget.php
```

当执行如下代码的时候

```bash
$ git status
```

会有如下类似的输出

```bash
renamed:    components/StatCNZZWidget.php -> components/StatCnzzWidget.php
```


