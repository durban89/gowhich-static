---
title: iOS7 在Appdelegate.m中处理多个handleopenURL
tags:
  - iOS
categories:
  - 技术
date: 2025-06-26 14:55:22
---

类似的情况如下：

```objectivec
return  [WeiboSDK handleOpenURL:url delegate:self];

return [FBAppCall handleOpenURL:url
              sourceApplication:sourceApplication
                fallbackHandler:^(FBAppCall *call) {
                    
                    NSLog(@"In fallback handler");
                    
                }];
```

facebook要调用我的handleOpenUrl，但是Sina Weibo也要调用,导致的结果是如何进行区分，然后进行不同的url调用。

其实很简单，对于这样的接口其实在ios中有过scheme的设置，完全可以判断url的前缀是否含有你自己设置的前缀，可以如下

```objectivec
NSString *string =[url absoluteString];

if ([string hasPrefix:@"微博url的前缀"])
{
     return [WeiboSDK handleOpenURL:url delegate:self];
}
else if ([string hasPrefix:@"Facebook的url的前缀"])
{
    return [WXApi handleOpenURL:url delegate:self];
}
```

嗯，记录下

