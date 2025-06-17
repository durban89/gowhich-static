---
title: iOS 毫秒级的计算 毫秒时间
tags:
  - iOS
categories:
  - 技术
date: 2025-06-17 17:21:14
---

毫秒级很简单

看代码示例

```objectivec
_imageNameDic = [NSMutableDictionary dictionaryWithCapacity:IMAGE_SUM];
for(int i=0;i<IMAGE_SUM;i++){
    NSDate *date = [NSDate date];
    NSTimeInterval aInterval =[date timeIntervalSince1970];
    
    NSString *timeString = [NSString stringWithFormat:@"%f", aInterval];

    NSString *uuid = [postData uuid];
    NSString *filename = [NSString stringWithFormat:@"%@_%@.png",uuid,timeString];
    NSMutableDictionary *tmpDic = [NSMutableDictionary dictionaryWithObjectsAndKeys:@"",@"state",[NSString stringWithFormat:@"%@",filename],@"name", nil];
    [_imageNameDic setObject:tmpDic
                      forKey:[NSString stringWithFormat:@"%d",i]];
}
```
