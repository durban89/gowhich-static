---
title: Objective-C四舍五入保留两位小数
tags:
  - Objective-C
categories:
  - 技术
date: 2025-06-16 14:37:43
---

Objective-C也需要这个，我真是用到了才去看，这叫遇到了才学，不主动，呵呵，废话少说，见代码

```objectivec
NSNumber* tempnumber = [NSNumber numberWithDouble:[[NSString stringWithFormat:@"%.2f",  
                                                  (float)(rand()%100001)*0.001f -20] doubleValue]]; 
cell.listProgressScore = [NSString stringWithFormat:@"%0.2f",[[detailDic valueForKey:@"current_index"] doubleValue]];
```
