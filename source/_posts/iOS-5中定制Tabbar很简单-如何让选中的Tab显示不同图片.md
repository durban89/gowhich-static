---
title: iOS 5中定制Tabbar很简单，如何让选中的Tab显示不同图片
tags:
  - iOS
categories:
  - 技术
date: 2025-06-25 09:57:45
---

第一步：获取tabbar

```objectivec
UITabBar *tabBar = self.tabBarController.tabBar;
```

第二步：获取tababr的所有选项

```objectivec
UITabBarItem *item = [tabBar.items objectAtIndex:0];
```

第三步：设置图片，选择要设置的tabbaritem

```objectivec
NSString *homePath = [[NSBundle mainBundle] pathForResource:@"btn_home_highlight@2x" ofType:@"png"];
if(item.tag == 1)
{
    item.selectedImage = [UIImage imageWithContentsOfFile:homePath];
}
```

这个就搞定了
