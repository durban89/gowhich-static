---
title: Python开发解决依赖库的办法
tags:
  - Python
categories:
  - 技术
date: 2025-07-01 11:54:18
---

**python开发解决依赖库的办法**

你可以用pip导出你的dependency:

```bash
$ pip freeze > requirements.txt
```

然后在通过以下命令安装dependency:

```bash
$ pip install -r requirements.txt
```

如此依赖如果你在服务器部署的话，就可以直接安装需要的依赖库，就不用等着报错才去一个一个安装了。


