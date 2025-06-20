---
title: iOS 关闭键盘 退出键盘 的5种方式
tags:
  - iOS
categories:
  - 技术
date: 2025-06-20 09:52:17
---


### [点击编辑区以外的地方（UIView）](#1)

这是一种很直觉的方法，当不再需要使用虚拟键盘时，只要点击虚拟键盘和编辑区域外的地方，就可以将键盘收起，下面程式码是在 UIView 中内建的触碰事件方法函式，您可以参考 Touch Panel / 触碰萤幕 / 压力感应器的基本使用方式一文，找到更多关于触碰事件的方法函式。

```objectivec
- (void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {  
    if (![myTextView isExclusiveTouch]) {  
        [myTextView resignFirstResponder];  
    }  
}
```

如果要使用此方式请务必记得，你操作画面的 Custom Class 一定要是 UIView 才行。  
画面的 Custom Class 为 UIView

### [点击编辑区域以外的地方（UIControl）](#2)

收起虚拟键盘的方式与前一种相同，但是如果你的触碰事件里已经且写满了程式码，那么就可以考虑使用，UIControl 的 Touch Up Inside 事件来收起键盘，方法是将以下程式码与 UIControl 的 Touch Up Inside 事件连结即可。

```objectivec
- (IBAction)dismissKeyboard:(id)sender {  
    [myTextView resignFirstResponder];  
}
```

 如果要使用此方式请务必记得，你操作画面的 Custom Class 一定要是 UIControl 才行。  
 画面的 Custom Class 为 UIControl  
 将收起键盘的方法与 UIControl 事件连结

### [使用制作收起键盘的按钮](#3)

当没有编辑区域以外的地方可供点击来收起键盘，自己制作一个按钮来收起目前的虚拟键盘，也是一个不错的方法，由于按钮必须在虚拟键盘出现才能显示于画面上，因此必须借用 NSNotificationCenter 来帮助我们判断目前键盘的状态。  
首先在 viewDidLoad: 事件中，向 NSNotificationCenter 进行註册，告诉 NSNotificationCenter 我们的 doneButtonshow: 方法函式。

```objectivec
- (void)viewDidLoad {  
   [super viewDidLoad];  
   [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector (doneButtonshow:) name: UIKeyboardDidShowNotification object:nil];  
}
```

现在每当虚拟键盘出现时，就会自动呼叫我们自定义的 doneButtonshow: 方法函式，接下来只要在该方法函式里定义按钮出现的方法即可。

```objectivec
-(void) doneButtonshow: (NSNotification *)notification {  
   doneButton = [UIButton buttonWithType: UIButtonTypeRoundedRect];  
   doneButton.frame = CGRectMake(0, 228, 70, 35);  
   [doneButton setTitle:@"完成编辑" forState: UIControlStateNormal];  
   [doneButton addTarget: self action:@selector(hideKeyboard) forControlEvents: UIControlEventTouchUpInside];  
  
   [self.view addSubview:doneButton];  
}
```

最后是实作按钮按下去时的 hideKeyboard: 方法函式，务必记得要在函式中移除该按钮。

```objectivec
-(void) hideKeyboard {  
   [doneButton removeFromSuperview];  
   [myTextView resignFirstResponder];  
}
```

### [使用判断输入字元](#4)

如果要使用输入特定字元（例如 return 换行字元）来收起键盘，必须先在类别内的 @interface 区段採用  协定，您可以参考 Protocol 协定的使用方式一文，获得更多关于协定的资讯。  
在采用  协定之后，接着实作出协定内的 textView:shouldChangeTextInRange:replacementText:方法函式，此方法函式会在字元输入时触发，而回传的 BOOL 值则代表该字元是否要作用，下列程式码就是在此方法函式中，使用判断输入字元的方式来收起虚拟键盘（判断字元为 return 换行字元）。

```objectivec
- (BOOL)textView:(UITextView *)textView shouldChangeTextInRange:(NSRange)range replacementText:(NSString *)text {  
    if ([text isEqualToString:@"\n"]) {  
        [myTextView resignFirstResponder];  
        return NO;  
    }  
    return YES;  
}
```

最后别忘记在 viewDidLoad: 事件中，将 UITextView 的代理物件指向自己，这样程式才能正确找到实作  协定方法函式的类别。

```objectivec
- (void)viewDidLoad  {  
    [super viewDidLoad];  
    myTextView.delegate = self;  
}
```

### [关于键盘遮蔽的问题](#5)

如果您在实作上有遭遇到键盘遮蔽编辑区域的问题，可以参考使用 Animation 解决小键盘挡住 UITextField 的问题一文，透过 Core Graphic 的 Animation 功能，在键盘出现时同时移动编辑区域来解决遮蔽的问题。
