---
title: iPhone中，点击换行，键盘消失，键盘退出
tags:
  - iOS
categories:
  - 技术
date: 2025-06-20 09:52:13
---

实现的步骤一个都不能少

1、要在声明文件中实现 UItextFieldDelegate 协议

2、在实现文件中实现 UItextFieldDelegate 协议 中键盘消失的方法即：

```objectivec
-(BOOL)textFieldShouldReturn:(UITextField *)textField{

     [textField resignFirstResponder];

     return YES;

}
```

3、在viewDidLoad方法中添加代理。例如：

```objectivec
-(void)viewDidLoad{

    [super viewDidLoad];

    //设置代理点击换行，键盘消失

     textSample.delegate =self;
}
```
