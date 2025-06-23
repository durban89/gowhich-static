---
title: 使用JS在textarea在光标处插入内容
tags:
  - JavaScript
categories:
  - 技术
date: 2025-06-23 15:49:14
---

今天在写一个小功能，就是添加视频，然后将视频的标题和链接添加到textarea中，其实是如此的简单，我确如此的...

```javascript
//插入数据到指定的位置
function insertText(string){
    var obj = $("#description").get(0);
    var str = string;
    if (document.selection) {
        obj.focus();
        var sel = document.selection.createRange();
        sel.text = str;
    } else if (typeof obj.selectionStart === 'number' && typeof obj.selectionEnd === 'number') {
        var startPos = obj.selectionStart;
        var endPos = obj.selectionEnd;
        var tmpStr = obj.value;
        obj.value = tmpStr.substring(0, startPos) + str + tmpStr.substring(endPos, tmpStr.length);
    } else {
        obj.value += str;
    }
}
```

