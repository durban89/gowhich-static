---
title: XCode帮助文档离线使用
tags:
  - Xcode
categories:
  - 技术
date: 2025-06-10 13:39:10
---

1.在线查看帮助文件：  
  
Xcode下查看帮助文件，菜单Help-Developer Documentation在右上角搜索框中即可检索，但速度很慢，在线查看。  
  
2.下载帮助文件到本地：  
  
要想下载帮助文件，菜单Xcode-preferences-Documentation 右键Get Info可以看到Feed URL找到.atom文件地址，用FF浏览器访问可以看到下载列表，用迅雷下载即可。  
  
atom链接如下，复制到浏览器地址栏即可见到下载列表（用IE浏览器好像不行）  
  
http://developer.apple.com/rss/com.apple.adc.documentation.AppleiPhone4\_2.atom  
  
http://developer.apple.com/rss/com.apple.adc.documentation.AppleSnowLeopard.atom  
  
http://developer.apple.com/rss/com.apple.adc.documentation.AppleXcode3\_2.atom  
  
也可直接用下面的链接下载  
  
http://devimages.apple.com/docsets/20101122/com.apple.adc.documentation.AppleLegacy.CoreReference.xar  
  
http://devimages.apple.com/docsets/20101122/com.apple.ADC\_Reference\_Library.DeveloperTools.xar  
  
http://devimages.apple.com/docsets/20101122/com.apple.adc.documentation.AppleSnowLeopard.JavaReference.xar  
  
http://devimages.apple.com/docsets/20101122/com.apple.adc.documentation.AppleSnowLeopard.CoreReference.Xcode4.xar  
  
http://devimages.apple.com/docsets/20101122/com.apple.adc.documentation.AppleiOS4\_2.iOSLibrary.Xcode4.xar  
  
3.下载后，拷贝到Mac的/Developer/Documentations/Docset目录下，  
  
使用终端命令：

```shell
sudo xar -xf 下载的文件名.xar
```

将其解压，然后修复权限:

```shell
sudo chown -R -P devdocs 解压后的文件名.docset
```

打开Xcode就可以离线浏览了。

