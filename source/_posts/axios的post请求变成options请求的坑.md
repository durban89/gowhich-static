---
title: axios的post请求变成options请求的坑
tags:
  - Axios
categories:
  - 技术
date: 2025-07-14 14:45:00
---

不知道其他的类似axios库有没有这个情况，我用的也少，基本很少用，不过其他的库也确实遇到的比较少，这里遇到这个问题记录下解决办法

如果你的代码是下面这个情况

```javascript
var data = {
  'id': 1,
  'name': 'minmin',
  'age': 23
}

axios({
  method: 'POST',
  url: 'http://xx.xxx.xxx',
  data: data,
}).then(function(res){
  console.log(res);
}).catch(function(err){
  console.log(err);
});
```

请换成如下的情况

```javascript
var data = new URLSearchParams();
data.append('id', '1');
data.append('name', 'minmin');
data.append('age', '23')

axios({
  method: 'POST',
  url: 'http://xx.xxx.xxx',
  data: data,
}).then(function(res){
  console.log(res);
}).catch(function(err){
  console.log(err);
});
```
