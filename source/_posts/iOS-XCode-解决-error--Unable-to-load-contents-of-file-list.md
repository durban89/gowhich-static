---
title: "iOS XCode 解决 error: Unable to load contents of file list"
tags:
  - PHP
categories:
  - 技术
date: 2025-07-15 09:50:46
---

问题：`error: Unable to load contents of file list ......`

原因是：升级了一下 cocoapods的版本后，由于版本不同导致

重新安装或者升级一下就好

```bash
gem install cocoapods --pre
```

然后把工程里面的 Pod 文件夹和 Podfile.lock 文件删掉，然后 cd 到项目根目录，然后重新运行一下 pod install 命令，重新编译即可。
