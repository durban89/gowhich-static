---
title: "clang: error: unable to execute command: posix_spawn failed: Resource temporarily unavailable"
tags:
  - Xcode
categories:
  - 技术
date: 2025-06-12 09:40:43
---

Xcode下创建一个项目，但是运行的时候出现了如下的错误：

```sh
clang: error: unable to execute command: posix_spawn failed: Resource temporarily unavailable
clang: error: clang frontend command failed due to signal (use -v to see invocation)
```

经过查找资料，有个说明是这样的，如下：

you may be running into too-low limits on the number of concurrent processes allowed on the machine. Check:

```sh
sysctl kern.maxproc
sysctl kern.maxprocperuid
```

You can increase them with e.g.:

```sh
sudo sysctl -w kern.maxproc=2500
sudo sysctl -w kern.maxprocperuid=2500
```

But normally this shouldn't be necessary if you're building on 10.7 or higher. If you see this, check if some rogue program spawned hundreds of processes and kill them first.

我按照上面的流程执行了操作：

```sh
davidzhang@davidzhang:~/command$ sysctl kern.maxproc
kern.maxproc: 1064
davidzhang@davidzhang:~/command$ sysctl kern.maxprocperuid
kern.maxprocperuid: 709
davidzhang@davidzhang:~/command$ sudo sysctl -w kern.maxproc=2500
Password:
kern.maxproc: 1064 -> 2500
davidzhang@davidzhang:~/command$ sudo sysctl -w kern.maxprocperuid=2500
kern.maxprocperuid: 709 -> 2500
```

最后运行我的项目的时候，问题就解决了

查询参考资料:http://code.google.com/p/chromium/wiki/MacBuildInstructions

