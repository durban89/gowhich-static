---
title: Android中Activity之间的跳转借助Intent
tags:
  - Android
categories:
  - 技术
date: 2025-07-03 11:58:39
---

相对于iOS要简单的多了。哈哈。

```java
Intent intent = new Intent(MainActivity.this, OtherActivity.class);
intent.putExtra("key","value");
startActivity(intent);
```


