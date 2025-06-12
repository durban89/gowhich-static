---
title: 使用for...in...输出NSMutableArray内容和输入NSMutableDictionary
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 17:45:02
---

### [for...in...输出NSMutableDictionary（代码片段摘录如下）](#1)

```objectivec
NSString *path = [[NSBundle mainBundle] pathForResource:@"attention" ofType:@"plist"];
self.dataDic = [NSDictionary dictionaryWithContentsOfFile:path];
self.items = [NSMutableArray arrayWithCapacity:0];
for (id section in self.dataDic) {
    Item *item = [[Item alloc] init];
    item.title = [[self.dataDic objectForKey:section] valueForKey:@"title"];
    item.isChecked = NO;
    [_items addObject:item];
}
```

### [for...in...输出NSMutableArray（代码片段摘录如下）](#2)

```objectivec
for (NSDictionary *item in _items) {
    NSLog(@"item.title = %@",[item valueForKey:@"title"]);
    NSLog(@"item.isChecked = %@",[item valueForKey:@"isChecked"]);
}
```
