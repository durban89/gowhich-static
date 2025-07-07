---
title: 国内安装oh-my-zsh
tags:
  - oh-my-zsh
  - zsh
categories:
  - 技术
date: 2025-07-07 11:53:11
---
## 安装 zsh

```bash
sudo yum install zsh
```
或者 

```bash
sudo apt install zsh
```


## 安装 oh-my-zsh

wget https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh

进入编辑状态：

```bash
vim install.sh
```

找到以下部分：

```bash
# Default settings
ZSH=${ZSH:-~/.oh-my-zsh}
REPO=${REPO:-ohmyzsh/ohmyzsh}
REMOTE=${REMOTE:-https://github.com/${REPO}.git}
BRANCH=${BRANCH:-master}
```

然后将中间两行改为：

```bash
REPO=${REPO:-mirrors/oh-my-zsh}
REMOTE=${REMOTE:-https://gitee.com/${REPO}.git}
```

然后保存退出：`:wq`

然后给`install.sh`添加权限：

```bash
chmod +x install.sh
```

然后执行install.sh：

```bash
./install.sh
```
执行即可
