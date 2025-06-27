---
title: jQuery 消息提醒插件 toastmessage
tags:
  - jQuery
  - JavaScript
categories:
  - 技术
date: 2025-06-27 14:14:50
---

最近做系统，想到使用后台要使用消息提醒，但是一直苦恼消息提醒的效果，于是找了一个toastmessage，还不错。记录下使用的方法。

第一步：引入需要的文件

```html
<script type="text/javascript" src="/js/admin/toastmessage/jquery.toastmessage.js"></script>
<link href="/js/admin/toastmessage/css/jquery.toastmessage.css" type="text/css" rel="stylesheet" />
```

第二步：测试使用的函数

```html
<script>
    function showSuccessToast() {
        $().toastmessage('showSuccessToast', "Success Dialog which is fading away ...");
    }
    function showStickySuccessToast() {
        $().toastmessage('showToast', {
            text     : 'Success Dialog which is sticky',
            sticky   : true,
            position : 'top-right',
            type     : 'success',
            closeText: '',
            close    : function () {
                console.log("toast is closed ...");
            }
        });
 
    }
    function showNoticeToast() {
        $().toastmessage('showNoticeToast', "Notice  Dialog which is fading away ...");
    }
    function showStickyNoticeToast() {
        $().toastmessage('showToast', {
             text     : 'Notice Dialog which is sticky',
             sticky   : true,
             position : 'top-right',
             type     : 'notice',
             closeText: '',
             close    : function () {console.log("toast is closed ...");}
        });
    }
    function showWarningToast() {
        $().toastmessage('showWarningToast', "Warning Dialog which is fading away ...");
    }
    function showStickyWarningToast() {
        $().toastmessage('showToast', {
            text     : 'Warning Dialog which is sticky',
            sticky   : true,
            position : 'top-right',
            type     : 'warning',
            closeText: '',
            close    : function () {
                console.log("toast is closed ...");
            }
        });
    }
    function showErrorToast() {
        $().toastmessage('showErrorToast', "Error Dialog which is fading away ...");
    }
    function showStickyErrorToast() {
        $().toastmessage('showToast', {
            text     : 'Error Dialog which is sticky',
            sticky   : true,
            position : 'top-right',
            type     : 'error',
            closeText: '',
            close    : function () {
                console.log("toast is closed ...");
            }
        });
    }
</script>
```

实例网站：

http://akquinet.github.io/jquery-toastmessage-plugin/demo/demo.html

