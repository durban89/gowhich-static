---
title: TypeScript 挑战（五）- 获取元素长度
tags:
  - TypeScript
categories:
  - 技术
date: 2025-07-14 16:21:45
---

学习记录 - 获取元素长度 - 对于给定的元组，您需要创建一个通用的Length，选择元组的长度

题目简介

---

对于给定的元组，您需要创建一个通用的`Length`，选择元组的长度

例如

```javascript
type tesla = ['tesla', 'model 3', 'model X', 'model Y']
type spaceX = ['FALCON 9', 'FALCON HEAVY', 'DRAGON', 'STARSHIP', 'HUMAN SPACEFLIGHT']

type teslaLength = Length<tesla>  // expected 4
type spaceXLength = Length<spaceX> // expected 5
```

---

测试用例

---

```javascript
import { Equal, Expect } from '@type-challenges/utils'

const tesla = ['tesla', 'model 3', 'model X', 'model Y'] as const
const spaceX = ['FALCON 9', 'FALCON HEAVY', 'DRAGON', 'STARSHIP', 'HUMAN SPACEFLIGHT'] as const

type cases = [
  Expect<Equal<Length<typeof tesla>, 4>>,
  Expect<Equal<Length<typeof spaceX>, 5>>,
]
```

---

答案

---

```javascript
type Length<T extends any> = T extends ArrayLike<any> ? T["length"] : never
```
