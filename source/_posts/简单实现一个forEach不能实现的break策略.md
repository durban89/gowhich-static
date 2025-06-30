---
title: 简单实现一个forEach不能实现的break策略
tags:
  - PHP
categories:
  - 技术
date: 2025-06-30 15:15:59
---

简单实现一个forEach不能实现的break策略：  
这个策略也是很多人都遇到过的。

代码如下：

```js
var list = [
  {'id':'1','title':'你好','regExp':'/你好/i'},
  {'id':'2','title':'我好','regExp':'/我好/i'},
  {'id':'3','title':'大家好','regExp':'/大家好/i'}
  ];
var match_id;
var match_string = '我好';
list.some(function(i){
  console.log(i);
  if(match_string.match(eval(i.regExp))){
    match_id = i.id;
    return true;
  }
});
console.log('match_id',match_id);
```

运行一下试试：结果如下

```
{ id: '1', title: '你好', regExp: '/你好/i' }
{ id: '2', title: '我好', regExp: '/我好/i' }
match_id 2
```


