---
title: Java的进制操作
tags:
  - Java
categories:
  - 技术
date: 2025-06-24 15:29:56
---

```java
public class JinZhi {
	public static void main(String args[]){
		int a10 = 12;
		int a8 = 012;
		System.out.println("十进制12等于"+a10);
		System.out.println("八进制12等于"+a8);
	}
}
```

输出的结果是：

```bash
十进制12等于12
八进制12等于10
```

---

十六进制的实例：

```java
public class JinZhi16 {
	public static void main(String args[]){
		int a1 = 0X12;
		int a2 = 0xcafe;
		System.out.println("第一个十六进制数值等于"+a1);
		System.out.println("第一个十六进制数值等于"+a2);
	}
}
```

输出的结果是：

```bash
第一个十六进制数值等于18
第一个十六进制数值等于51966
```

