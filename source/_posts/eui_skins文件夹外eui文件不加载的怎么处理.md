---
title: eui_skins文件夹外eui文件不加载的怎么处理
tags:
  - Egret
categories:
  - 技术
date: 2025-07-11 11:15:22
---

eui\_skins文件夹外eui文件不加载的怎么处理

修改egretProperties.json配置文件（关闭Egret UI Editor的情况下）

加入如下配置

```json
"eui": {
  "exmlRoot": [
    "resource/eui_skins",
    "resource/scene"
  ],
  "themes": [
    "resource/default.thm.json"
  ],
  "exmlPublishPolicy": "commomjs"
},
```

默认配置是没有这个选项的
