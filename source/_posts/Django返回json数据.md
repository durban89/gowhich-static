---
title: Django返回json数据
tags:
  - Django
categories:
  - 技术
date: 2025-06-24 15:04:28
---

Django在做网站开发的时候，少不了需要将数据转换为什么格式，这里先简单的说说Django返回json格式数据的方法

### [前端：jQuery发送GET请求，并解析json数据](#1)

getJSON方法可参考[这里](http://www.w3school.com.cn/jquery/ajax_getjson.asp)。

```javascript
url = "http://example.com/?q=" + q + "&rand=" + Math.random();
$.getJSON(url, function(json){
    a = json.a;
    alert(a);
});
```

### [后端：Django接收GET请求并返回json数据](#2)

```python
from django.http import HttpResponse
from django.utils import simplejson
if request.method == 'GET' and 'q' in request.GET:
    question = request.GET['q']
    data = {"a": "a"}
    #ensure_ascii=False用于处理中文
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False))
```

总的看来还是比较简答的吧

