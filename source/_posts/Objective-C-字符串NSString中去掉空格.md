---
title: Objective-C 字符串NSString中去掉空格
tags:
  - Objective-C
categories:
  - 技术
date: 2025-06-16 14:38:17
---

1,使用NSString中的`stringByTrimmingCharactersInSet:[NSCharacterSet whitespaceCharacterSet]];` 方法只是去掉左右两边的空格  
2,使用`NSString *strUrl = [urlString stringByReplacingOccurrencesOfString:@" " withString:@""];` 使用替换的方法去掉空格

示例：

```objectivec
NSString *personIdString = [[NSString alloc] init];
for (id item in _compareDataDic) {
    personIdString = [personIdString stringByAppendingString:[NSString stringWithFormat:@"%@ ",[[_compareDataDic valueForKey:[NSString stringWithFormat:@"%@",item]] valueForKey:@"person_id"]]];
}
personIdString = [personIdString stringByTrimmingCharactersInSet:[NSCharacterSet whitespaceCharacterSet]];
personIdString = [personIdString stringByReplacingOccurrencesOfString:@" " withString:@","];
```

`_compareDataDic`是一个`NSMutableDictionary`类型的变量
