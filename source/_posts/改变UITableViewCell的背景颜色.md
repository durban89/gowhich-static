---
title: 改变UITableViewCell的背景颜色
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 11:49:43
---

最有效的解决方式是: 使用

```objectivec
- (void) tableView: (UITableView *) tableView willDisplayCell:(UITableViewCell *)cell forRowAtIndexPath:(NSIndexPath *)indexPath
```

托管函数中定义Cell的背景颜色值。(注意：cell.textLabel的背景颜色默认为white, 如有要自定义还是需另用代码来控制实现)

```objectivec
- (UITableViewCell *) tableView: (UITableView *) tableView cellForRowAtIndexPath: (NSIndexPath *) indexPath {
        [cell.contentView setBackgroundColor: [UIColor redColor] ];
}
```
