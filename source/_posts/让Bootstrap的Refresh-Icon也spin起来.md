---
title: 让Bootstrap的Refresh Icon也spin起来
tags:
  - Bootstrap
categories:
  - 技术
date: 2025-07-03 11:08:13
---

bootstrap下面有个glyphicon-refresh，但是不会自定动态spin[旋转]，下面提供下我的实例

```css
.spin{
    -webkit-transform-origin: 50% 50%;
    transform-origin:50% 50%;
    -ms-transform-origin:50% 50%; /* IE 9 */
    -webkit-animation: spin .8s infinite linear;
    -moz-animation: spin .8s infinite linear;
    -o-animation: spin .8s infinite linear;
    animation: spin .8s infinite linear;
  }

  @-webkit-keyframes spin {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(359deg);
      transform: rotate(359deg);
    }
  }
  @keyframes spin {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(359deg);
      transform: rotate(359deg);
    }
  }
```

调用方式如下

```html
<span class="glyphicon glyphicon-refresh loading spin"> </span>
```


