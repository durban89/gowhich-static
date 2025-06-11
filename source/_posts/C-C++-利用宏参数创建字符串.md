---
title: C/C++ 利用宏参数创建字符串
tags:
  - C/C++
categories:
  - 技术
date: 2025-06-11 10:59:10
---

代码示例：

```c
/* subst.c -- 在字符串中进行替换 */
#include <stdio.h>
#define PSOR(x) printf("The square of " #x " is %d\n", ((x)*(x)))

int main(void){
	int y = 5;
	PSOR(y);
	PSOR(2 + 4);
	return 0;
}
```

运行结果为：

```shell
The square of y is 25
The square of 2 + 4 is 36
```

