---
title: VirtualBox 7.0.10 kernel 6.5.x on ubuntu 22.04
tags:
  - VirtualBox
  - Linux
categories:
  - 技术
date: 2025-07-15 10:29:23
---

今天启动Virtualbox后启动不了报错，提示我运行

/sbin/vboxconfig

得到的结果提示如下

```bash
Kernel driver not installed (rc=-1908)

The VirtualBox Linux kernel driver is either not loaded or not set up correctly. Please try setting it up again by executing

'/sbin/vboxconfig'

as root.

If your system has EFI Secure Boot enabled you may also need to sign the kernel modules (vboxdrv, vboxnetflt, vboxnetadp, vboxpci) before you can load them. Please see your Linux system's documentation for more information.

where: suplibOsInit what: 3 VERR_VM_DRIVER_NOT_INSTALLED (-1908) - The support driver is not installed. On linux, open returned ENOENT.
```

社区的解决方案https://forums.virtualbox.org/viewtopic.php?t=110128

```bash
$ sudo add-apt-repository ppa:ubuntu-toolchain-r/ppa -y
$ sudo apt update
$ sudo apt install g++-12 gcc-12
```

我执行上面的步骤没有问题后，重新运行还是不行

于是又执行了

/sbin/vboxconfig
