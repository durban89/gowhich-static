---
title: Nodejs 中解决 no-await-in-loop
tags:
  - Nodejs
categories:
  - 技术
date: 2025-07-03 17:37:49
---

在使用nodejs中的async/await方法的时候，在map,forEach中使用await的时候，eslint总是提示我no-await-in-loop。对于我比较喜欢正规写代码的人讲，忍受不了这种错误提示。最终还是找到了解决办法。

一般什么情况会有这个错误的呢，如下

```javascript
async test() {
  const testData = [1, 2, 3];
  testData.forEach((v) => {
    // 这里就会提示 no-await-in-loop
    const res = await getItem(v); // 假设这里的getItem是一个Promise 
  })
}
```

解决的办法如下,改成如下方式就可以了，针对forEach也一并改为map。

```js
async test() {
  const testData = [1, 2, 3];
  testData.map(async (v) => {
    // 这里就会提示 no-await-in-loop
    const res = await getItem(v); // 假设这里的getItem是一个Promise 
  })
}
```
