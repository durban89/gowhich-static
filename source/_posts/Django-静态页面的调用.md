---
title: Django 静态页面的调用
tags:
  - Django
  - Python
categories:
  - 技术
date: 2025-06-26 10:32:48
---

关于django的静态页面的调用方法很是简单，也是最近google后发现的

只要在urls.py添加类似如下的代码就可以了

```python
urlpatterns += patterns('django.views.generic.simple',
    (r'^zhanzhang\.html', 'direct_to_template', {'template': 'zhanzhang.html'}),
)
```

上面的代码的意思是追加了一条url匹配规则

---

参考的文章：

<https://docs.djangoproject.com/en/1.2/ref/generic-views/>

<http://python-china.org/topic/326>
