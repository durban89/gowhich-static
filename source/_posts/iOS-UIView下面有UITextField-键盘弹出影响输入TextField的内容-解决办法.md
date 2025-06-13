---
title: iOS UIView下面有UITextField,键盘弹出影响输入TextField的内容，解决办法
tags:
  - iOS
categories:
  - 技术
date: 2025-06-13 11:34:40
---

在viewdidload的时候，把每个TextField设好tag。之后就可以根据最下面的UITextField的内容来判断键盘的弹出和关闭了

实例代码：

```objectivec
- (void)textFieldDidBeginEditing:(UITextField *)textField 

{ //当点触textField内部，开始编辑都会调用这个方法。textField将成为first responder  

    if (textField.tag == 2) {

        NSTimeInterval animationDuration = 0.30f;     

        CGRect frame = self.view.frame; 

        frame.origin.y -=216; 

        frame.size.height +=216; 

        self.view.frame = frame; 

        [UIView beginAnimations:@"ResizeView"context:nil]; 

        [UIView setAnimationDuration:animationDuration]; 

        self.view.frame = frame;                 

        [UIView commitAnimations];

    }
} 

 

- (BOOL)textFieldShouldReturn:(UITextField *)textField  

{//当用户按下ruturn，把焦点从textField移开那么键盘就会消失了 

//    textField

    if (textField.tag == 2) {

        NSTimeInterval animationDuration = 0.30f; 

        CGRect frame = self.view.frame;     

        frame.origin.y +=216;       

        frame.size. height -=216;    

        self.view.frame = frame; 

        //self.view移回原位置   

        [UIView beginAnimations:@"ResizeView"context:nil]; 

        [UIView setAnimationDuration:animationDuration]; 

        self.view.frame = frame; 

        [UIView commitAnimations];

    }

    [textField resignFirstResponder];    

    returnYES;
}
```
