---
title: 自定义NavigationBar
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 17:18:45
---

最近写app，在一个部分想自定义一下NavigationBar：

```objectivec
self.navigationBar = [[UINavigationBar alloc]
                            initWithFrame:CGRectMake(0.0, 0.0, width, 40.0)];
[self.navigationBar setBackgroundColor:[UIColor redColor]];
    
self.navigationBar.tintColor = [UIColor redColor];
[self.view addSubview:self.navigationBar];
    
UINavigationItem *navigationTitle = [[UINavigationItem alloc] initWithTitle:@"艺人指数排行榜"];
[self.navigationBar pushNavigationItem:navigationTitle animated:NO];
```

别忘记一个操作就是隐藏掉默认的navigationBar:

代码如下：

```objectivec
[self.navigationController setNavigationBarHidden:YES];
```

这行代码可以加到`didFinishLaunchingWithOptions`中，也可以加到`viewDidLoad`中
