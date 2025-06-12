---
title: 'loaded the "BlueView" nib but the view outlet was not set 错误的解决办法'
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 09:56:48
---

解决办法：

- 创建控制器. File->New File->Iphone OS->Cocoa Touch Class->UIViewController subclass;

- 创建xib. File->New File->Iphone OS->User Interface->View XIB

- 绑定controller和view. 用Interface Builder打开xxx.xib, 点击Files' Owner, 在Identity Inspector里面的Class Identity, 选择Step 1创建的控制器类, 接着拖拽File's Owner到View中, 选择Outlets->view.先选中file's owner(这个很重要)

来源:http://blog.csdn.net/thebesttome/article/details/7799893
