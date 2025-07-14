---
title: TypeScript 挑战（六）- 实现内置的Exclude <T，U>
tags:
  - TypeScript
categories:
  - 技术
date: 2025-07-14 16:21:49
---

学习记录 - 实现内置的Exclude <T，U>

题目简介

---

实现内置的Exclude <T，U>

> 从T中排除可分配给U的那些类型

---

测试用例

---

```javascript
import { Equal, Expect, ExpectFalse, NotEqual } from '@type-challenges/utils'

type cases = [
    Expect<Equal<MyExclude<"a" | "b" | "c", "a">, Exclude<"a" | "b" | "c", "a">>>,
    Expect<Equal<MyExclude<"a" | "b" | "c", "a" | "b">, Exclude<"a" | "b" | "c", "a" | "b">>>,
    Expect<Equal<MyExclude<string | number | (() => void), Function>, Exclude<string | number | (() => void), Function>>>,
]
```

---

答案

---

```javascript
type MyExclude<T, U> = T extends U ? never : T;
```
