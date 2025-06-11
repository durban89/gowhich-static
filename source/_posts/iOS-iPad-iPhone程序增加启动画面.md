---
title: iOS iPad iPhone程序增加启动画面
tags:
  - iOS
categories:
  - 技术
date: 2025-06-11 11:07:03
---


为iPad和iPhone程序增加启动画面非常简单，基本思路就是增加启动图片资源Default.png即可，只是要根据不同的分辨率和旋转方向需要有不同的图片尺寸。

目前的iOS设备有三种不同的分辨率：

**iPad 768x1024**  
**iPhone4 640x960**  
**iPhone 320x480**  
如果一个程序，既要支持iPad又要支持iPhone，那么它需要包含下面几个图片：

**Default-Portrait.png iPad专用竖向启动画面 768x1024或者768x1004**  
**Default-Landscape.png iPad专用横向启动画面 1024x768或者1024x748**  
**Default-PortraitUpsideDown.png iPad专用竖向启动画面(Home按钮在屏幕上面)，可省略 768x1024或者768x1004**  
**Default-LandscapeLeft.png iPad专用横向启动画面(可省略), 1024x768或者1024x748**  
**Default-LandscapeRight.png iPad专用横向启动画面(可省略), 1024x768或者1024x748**  
**Default.png iPhone默认启动图片，如果没有提供上面几个iPad专用启动图片，则在iPad上运行时也使用Default.png（不推荐） 320x480或者320x460**  
**[[email protected]](/cdn-cgi/l/email-protection) iPhone4启动图片640x960或者640x920**  
为了在iPad上使用上述的启动画面，你还需要在xxxx\_info.plist中加入key(根据下拉菜单中的可选项选择):

**UISupportedInterfaceOrientations** 或 **Supported interface orientations**  
同时，为其加入值(根据下拉菜单中的可选项选择):

**UIInterfaceOrientationPortrait 或 Portrait (bottom home button)**  
**UIInterfacOrientationPortraitUpsideDown 或 Portrait (top home button)**  
**UIInterfaceOrientationLandscapeLeft 或 Landscape (left home button)**  
**UIInterfaceOrientationLandscapeRight 或 Landscape (right home button)**
