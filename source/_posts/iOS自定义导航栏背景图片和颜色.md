---
title: iOS自定义导航栏背景图片和颜色
tags:
  - iOS
categories:
  - 技术
date: 2025-06-13 10:13:39
---

修改导航栏的背景图片，可按照下面的方法操作：

```objectivec
UINavigationBar *navBar = self.navigationController.navigationBar;  
  
#define kSCNavBarImageTag 10  
if ([navBar respondsToSelector:@selector(setBackgroundImage:forBarMetrics:)])  
{  
    //if iOS 5.0 and later  
    [navBar setBackgroundImage:[UIImage imageNamed:@"navbar1.png"] forBarMetrics:UIBarMetricsDefault];  
}  
else  
{  
    UIImageView *imageView = (UIImageView *)[navBar viewWithTag:kSCNavBarImageTag];  
    if (imageView == nil)  
    {  
        imageView = [[UIImageView alloc] initWithImage:  
                     [UIImage imageNamed:@"navbar1.png"]];  
        [imageView setTag:kSCNavBarImageTag];  
        [navBar insertSubview:imageView atIndex:0];  
        [imageView release];  
    }  
}
```

修改导航栏的背景色的方法，可按照下面的办法来操作：

```objectivec
navBar.tintColor = [UIColor greenColor];
```
