---
title: iOS 点击屏幕任意空白处，键盘消失
tags:
  - iOS
categories:
  - 技术
date: 2025-06-13 11:34:44
---

点击屏幕任意空白处，键盘消失的方法：

在这个方法里面实现就好了：

```objectivec
-(void) touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    [self.teleplayDescription resignFirstResponder];
    [self.teleplayTitle resignFirstResponder];
    [self.teleplayContactPeople resignFirstResponder];
    [self.teleplayContactPeoplePhone resignFirstResponder];
}
```
