---
title: 创建透明的UIToolbar
tags:
  - iOS
categories:
  - 技术
date: 2025-06-17 17:04:04
---

写描述方法：

正确的方法是子类化UIToolbar，设置其backgroundColor

```objectivec
@interface TranslucentToolbar : UIToolbar  
  
@end  
 
@implementation TranslucentToolbar  
  
- (void)drawRect:(CGRect)rect {  
    // do nothing   
}  
  
- (id)initWithFrame:(CGRect)aRect {  
    if ((self = [super initWithFrame:aRect])) {  
        self.opaque = NO;  
        self.backgroundColor = [UIColor clearColor];  
        self.clearsContextBeforeDrawing = YES;  
    }  
    return self;  
}  
@end
```

在需要创建的地方使用子类化的UIToolbar

如果你说不知道这些代码放在哪里。好吧我告诉你，其实这个就在自定义的UIoolbar中，如果你还不知道的话，请联系我好了，或者留言
