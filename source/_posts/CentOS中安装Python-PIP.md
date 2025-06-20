---
title: CentOS中安装Python-PIP
tags:
  - CentOS
  - Linux
categories:
  - 技术
date: 2025-06-20 11:50:54
---


首先要安装 Setuptools

```bash
wget --no-check-certificate https://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c11-py2.6.egg
sudo sh ./setuptools-0.6c11-py2.6.egg
```

安装PIP

```bash
wget --no-check-certificate https://pypi.python.org/packages/source/p/pip/pip-1.4.tar.gz
tar -zxvf ./pip-1.4.tar.gz
cd pip-1.4
sudo python setup.py install
```
