---
title: "CodeSign error: code signing is required for product type 'Application' in SDK 'iOS 5.0'"
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 09:56:44
---

解决方法如下:

选择工程－>Build Settings -> Code Signing -> Code Signing Identity -> Debug -> Any ios SDK 将选项改为：iPhone Developer
