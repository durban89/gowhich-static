---
title: TypeScript 挑战（四）- 第一个元素
tags:
  - TypeScript
categories:
  - 技术
date: 2025-07-14 16:21:42
---

第一个元素 - 实现一个通用`First<T>`，它接受一个数组`T`并返回它的第一个元素的类型。学习记录如下

---

题目简介

---

实现一个通用`First<T>`，它接受一个数组`T`并返回它的第一个元素的类型。

例如

```javascript
type arr1 = ['a', 'b', 'c']
type arr2 = [3, 2, 1]

type head1 = First<arr1> // expected to be 'a'
type head2 = First<arr2> // expected to be 3
```

测试用例

---

```javascript
import { Equal, Expect } from '@type-challenges/utils'

type cases = [
  Expect<Equal<First<[3, 2, 1]>, 3>>,
  Expect<Equal<First<[() => 123, { a: string }]>, () => 123>>,
  Expect<Equal<First<[]>, never>>,
  Expect<Equal<First<[undefined]>, undefined>>
]
```

答案

---

```javascript
type First<T extends any[]> = T extends never[] ? never : T[0]
```
