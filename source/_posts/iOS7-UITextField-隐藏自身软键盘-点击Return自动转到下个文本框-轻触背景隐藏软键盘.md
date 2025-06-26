---
title: iOS7 UITextField 隐藏自身软键盘、点击Return自动转到下个文本框、轻触背景隐藏软键盘
tags:
  - iOS
categories:
  - 技术
date: 2025-06-26 11:37:49
---

关于UITextField的几种常用的方法，隐藏自身软键盘、点击Return自动转到下个文本框、轻触背景隐藏软键盘，经过google的查找，现在总结如下：

#### [一、隐藏自身软键盘](#1)

　　当对于有多个UITextField控件都想通过点击“Return”来隐藏自身软键盘的情况，这时的最好办法是使用Did End on Exit事件。在点击软键盘右下角的“Return”按钮后，会触发该事件。

　　该事件有一个sender参数表示当前文本框，这样便可以编写一个通用的事件处理方法（.m文件）——

```objectivec
- (IBAction)TextField_DidEndOnExit:(id)sender {
    // 隐藏键盘.
    [sender resignFirstResponder];
}
```

　　然后在.h文件中填写该方法的声明——

```objectivec
- (IBAction)TextField_DidEndOnExit:(id)sender;
```

　　回到storyboard，并按command+option+enter打开辅助窗口，使辅助窗口显示.h文件。

　　选中一个UITextField控件，点击鼠标右键弹出面板，鼠标左键按住Did End on Exit事件旁边的圆圈，然后拖曳到右侧.h文件的TextField_DidEndOnExit方法上，便会建立好事件连接。

　　随后按照同样的做法，将其他UITextField控件的Did End on Exit事件也连接到TextField_DidEndOnExit方法。

　　运行一下，可发现每个文本框的软键盘都可以通过点击“Return”来隐藏了。

#### [二、点击Return自动转到下个文本框](#2)

　　当页面中有很多个文本框时，如果每次都需要点文本框激活软键盘、输入后点击Return隐藏软键盘、再点击下一个文本框……这样操作起来太繁琐了。

　　于是我们希望能够实现点击Return时能够自动转到下一个文本框。尤其是对于最后一个文本框，希望能够在点击Return时执行下一步操作。

　　例如对于登录页面。它上面有 账号文本框（nameTextField）、密码文本框（passTextField）、登录按钮（loginButton）。

　　我们希望——点击账号文本框软键盘的Return时跳转到密码文本框，点击密码文本框软键盘的Return时执行登录。

　　因为这两个文本框的功能不同，不能像上一节那样写一个TextField_DidEndOnExit做统一处理，而应该分别建立各自的事件处理方法。

　　回到storyboard，右击账号文本框（nameTextField）弹出面板，按住Did End on Exit事件旁边的圆圈，然后拖曳到右侧.h文件的空白地方，此时会弹出一个对话框给方法命名。输入名称（nameTextField_DidEndOnExit）后回车确定，便自动生成了该事件方法。

　　随后按照同样的做法，为密码文本框（passTextField）的Did End on Exit事件连接方法（passTextField_DidEndOnExit）。

　　来到.m文件，填写具体代码——

```objectivec
- (IBAction)nameTextField_DidEndOnExit:(id)sender {
    // 将焦点移至下一个文本框.
    [_passTextField becomeFirstResponder];
}
```

　　对于账号文本框转密码文本框，不需要隐藏软键盘，只需要调用becomeFirstResponder激活新的文本框就行了。

　　对于密码文本框Return后执行登录。因为不再需要显示软键盘，所以还是得调用resignFirstResponder隐藏软键盘，然后触发登录按钮（loginButton）的UIControlEventTouchUpInside事件进行登录。

　　运行一下，可发现已经达到我们希望的效果了。点击账号文本框软键盘的Return时跳转到密码文本框，点击密码文本框软键盘的Return时执行登录。

　　怎么都是“Return”，转换文本框与执行登录明明是不同的功能？

　　于是将账号文本框的Return Key属性设为“Next”，将密码文本框的Return Key属性设为“Done”，使界面与功能一致。

#### [三、轻触背景隐藏软键盘](#3)

　　只能通过Return关闭软键盘太不灵活了，应该提供轻触背景隐藏软键盘的功能。

　　在storyboard，点击背景View，将它的Custom Class设置为UIControl，这样才会出现Touch Down事件。

　　右击背景View弹出面板，按住Touch Down事件旁边的圆圈，然后拖曳到右侧.h文件的空白地方建立该事件的处理方法。

　　来到.m文件，填写具体代码——

```objectivec
- (IBAction)View_TouchDown:(id)sender {
    // 发送resignFirstResponder.
    [[UIApplication sharedApplication] sendAction:@selector(resignFirstResponder) to:nil from:nil forEvent:nil];
}
```

---

参考文章：

http://www.cnblogs.com/zyl910/archive/2013/03/29/ios_textfield_keyboard.html

