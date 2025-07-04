---
title: 学习下CSS选择器 奇偶匹配nth-child(even)
tags:
  - CSS
categories:
  - 技术
date: 2025-06-17 15:50:52
---

CSS3伪类选择器：nth-child()
简单的归纳下nth-child()的几种用法。
第一：nth-child(number) 直接匹配第number个元素。参数number必须为大于0的整数。

```css
(EG) li:nth-child(3){background:orange;}/*把第3个LI的背景设为橙色*/
```

第二：nth-child(an) 匹配所有倍数为a的元素。其中参数an中的字母n不可缺省，它是倍数写法的标志，如3n、5n。

```css
(EG) li:nth-child(3n){background:orange;}/*把第3、第6、第9、…、所有3的倍数的LI的背景设为橙色*/
```

第 三：nth-child(an+b) 与 :nth-child(an-b) 先对元素进行分组，每组有a个，b为组内成员的序号，其中字母n和加号+不可缺省，位置不可调换，这是该写法的标志，其中a,b均为正整数或0。如 3n+1、5n+1。但加号可以变为负号，此时匹配组内的第a-b个。（其实an前面也可以是负号，但留给下一部分讲。）

```css
(EG)li:nth-child(3n+1){background:orange;}/*匹配第1、第4、第7、…、每3个为一组的第1个LI*/ 
li:nth-child(3n+5){background:orange;}/*匹配第5、第8、第11、…、从第5个开始每3个为一组的第1个LI*/ 
li:nth-child(5n-1){background:orange;}/*匹配第5-1=4、第10-1=9、…、第5的倍数减1个LI*/ 
li:nth-child(3n±0){background:orange;}/*相当于(3n)*/ 
li:nth-child(±0n+3){background:orange;}/*相当于(3)*/
```

第四：nth-child(-an+b) 此处一负一正，均不可缺省，否则无意义。这时与:nth-child(an+1)相似，都是匹配第1个，但不同的是它是倒着算的，从第b个开始往回算，所以它所匹配的最多也不会超过b个。

```css
(EG) li:nth-child(-3n+8){background:orange;}/*匹配第8、第5和第2个LI*/ 
li:nth-child(-1n+8){background:orange;}/*或(-n+8)，匹配前8个（包括第8个）LI，这个较为实用点，用来限定前面N个匹配常会用到*/
```

第五：nth-child(odd) 与 :nth-child(even) 分别匹配序号为奇数与偶数的元素。奇数(odd)与(2n+1)结果一样；偶数(even)与(2n+0)及(2n)结果一样。

参考:http://www.cnblogs.com/pansly/archive/2011/05/04/2037003.html
