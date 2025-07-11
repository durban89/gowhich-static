---
title: CSS小技巧 - CSS实现光标
tags:
  - CSS
categories:
  - 技术
date: 2025-07-11 10:40:48
---

原理使用css的伪类':before'和':after'

如果想要光标在内容的后面

```css
.class:before {
	content: ''
}

.class:after {
	content: '';
	border-right: 2px solid #ffd500;
	height: 50%;
	opacity: 1;
	animation: focus .7s forwards infinite;
}

@keyframes focus {
	from {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}
```

如果想要光标在内容的前面

```css
.class:before {
	content: ''
	border-right: 2px solid #ffd500;
	height: 50%;
	opacity: 1;
	animation: focus .7s forwards infinite;
}

.class:after {
	content: '';
}

@keyframes focus {
	from {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}
```
