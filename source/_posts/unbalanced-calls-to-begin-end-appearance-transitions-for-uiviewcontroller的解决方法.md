---
title: unbalanced calls to begin/end appearance transitions for uiviewcontroller的解决方法
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 09:40:47
---

由于上个uivewcontroller的动画没做完，导致下一个的页面无法顺利压栈，这个只需要上一个页面返回的时候不要做动画就可以了。（这是其中的一种情况），

如果不想去掉这个动画，需要做动画的操作，该怎么办呢，我这里给出一篇文章的做法，基本上都是类似的，我这里贴出地址：

http://www.cfanz.cn/?c=article&a=read&id=23441
