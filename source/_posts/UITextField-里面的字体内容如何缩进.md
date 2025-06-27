---
title: UITextField 里面的字体内容如何缩进
tags:
  - iOS
categories:
  - 技术
date: 2025-06-27 10:07:13
---

实现的代码如下，记录下

```objectivec
_searchTextField = [[UITextField alloc] initWithFrame:CGRectMake(self.navigationController.navigationBar.frame.size.width - 235.0 - 10.0,
                                                                 (self.navigationController.navigationBar.frame.size.height - 30.0) / 2 ,
                                                                 235.0,
                                                                 30.0)];
_searchTextField.delegate = self;
_searchTextField.placeholder = @"输入艺人名称";

UIView *view = [[UIView alloc] initWithFrame:CGRectMake(0.0, 0.0, 10.0, 30.0)];//左端缩进15像素
_searchTextField.leftView = view;
_searchTextField.leftViewMode = UITextFieldViewModeAlways;
```

