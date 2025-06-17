---
title: UIButton的image和title位置设置
tags:
  - iOS
categories:
  - 技术
date: 2025-06-17 11:59:49
---

通过setTitle和titleEdgeInsets，setImage和imageEdgeInsets，能够实现title和image位置的变化

具体的代码我以实现title的位置变化为例子：

```objectivec
UIButton *addButton = [UIButton buttonWithType:UIButtonTypeCustom];
addButton.layer.borderColor = [[UIColor whiteColor] CGColor];
addButton.layer.borderWidth = 2.0;
addButton.layer.cornerRadius = 10.0;
addButton.titleLabel.font = [UIFont systemFontOfSize:54.0];
addButton.titleLabel.textAlignment = NSTextAlignmentCenter;
[addButton sizeToFit];
[addButton setTitleEdgeInsets:UIEdgeInsetsMake(-10.0, 0.0, 0.0, 0.0)];
[addButton setFrame:CGRectMake(0.0, 5.0, 60.0, 60.0)];
[addButton setTitle:@"+" forState:UIControlStateNormal];
[addButton addTarget:self
              action:@selector(addAction:)
    forControlEvents:UIControlEventTouchUpInside];
```
