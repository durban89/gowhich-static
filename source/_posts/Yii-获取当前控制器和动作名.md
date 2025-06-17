---
title: Yii 获取当前控制器和动作名
tags:
  - PHP
categories:
  - 技术
date: 2025-06-17 17:19:48
---

我的总结是这样的：

1. 获取控制器名

```php
$this->controller = Yii::app()->controller->id;
```

2. 获取动作名

```php
$this->action = Yii::app()->controller->action->id;
```

参考的原文是这样的：

> 1. 获取控制器名

> 在控制器中获取控制器名:

> $name = $this->getId();

> 在视图中获取控制器名:

> $name = Yii::app()->controller->id;

> 2. 获取动作名

> 在控制器beforeAction()回调函数中获取动作名:

> $name = $action->id;

> 在其他地方获取动作名:

> $name = $this->getAction()->getId();

我试过几个，有几个不是很好用，但是我的总结里面是绝对可以使用的，因为是一个全局变量。
