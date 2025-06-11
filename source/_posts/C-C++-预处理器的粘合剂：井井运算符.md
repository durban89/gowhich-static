---
title: C/C++ 预处理器的粘合剂：##运算符
tags:
  - C/C++
categories:
  - 技术
date: 2025-06-11 11:00:03
---

实例代码:

```c
/* glue.c -- 使用##运算符 */
#include <stdio.h>
#define XNAME(n) x ## n
#define PRINT_XN(n) printf("x" #n " = %d\n", x ## n)

int main(void)
{
	int XNAME(1) = 14;
	int XNAME(2) = 20;
	PRINT_XN(1);
	PRINT_XN(2);
	return 0;
}
```

运行结果如下：

```shell
x1 = 14
x2 = 20
```
