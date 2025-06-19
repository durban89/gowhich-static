---
title: 根据条件判断使用哪个Storyboard
tags:
  - iOS
categories:
  - 技术
date: 2025-06-19 10:29:13
---

关于根据条件选择Storyboard，我之前的一篇文章，今天使用的时候，不起作用了，悲剧，今天又自己写了一个。

```objectivec
//主要的storyboard - xunYi7TabBarViewController
//login的storyboard - login

UIViewController *rootViewController;
self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
self.window.backgroundColor = [UIColor whiteColor];
if([[NSUserDefaults standardUserDefaults] boolForKey:@"logged_in"]) {
  
  rootViewController = [[UIStoryboard 
storyboardWithName:@"MainStoryboard" bundle:nil] 
instantiateViewControllerWithIdentifier:@"xunYi7TabBarViewController"];
}else{
  
  rootViewController = [[UIStoryboard 
storyboardWithName:@"LoginStoryboard" bundle:nil] 
instantiateViewControllerWithIdentifier:@"login"];
}
self.window.rootViewController=rootViewController;

[self.window makeKeyAndVisible];
return yes;
```

如果这个例子不起作用，也可以尝试我之前的那篇文章[iOS启动 判断使用不同的 storyboard](https://www.gowhich.com/blog/268)
