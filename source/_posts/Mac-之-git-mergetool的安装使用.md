---
title: Mac 之 git mergetool的安装使用
tags:
  - MacOS
  - Git
categories:
  - 技术
date: 2025-07-03 11:58:29
---

git mergetool 工具安装

```bash
brew install meld 或 brew install homebrew/gui/meld
git config --global merge.tool meld
git mergetool
```

