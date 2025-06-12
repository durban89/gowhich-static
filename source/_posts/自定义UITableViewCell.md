---
title: 自定义UITableViewCell
tags:
  - iOS
categories:
  - 技术
date: 2025-06-12 17:18:57
---

自己的应用中需要一种非普通格式的cell，于是自己就定义了一下；基本上的代码类似如下：

```objectivec
static NSString *captionCellWithIdentifier = @"captionCell";

//使用自定义的cell模板
static BOOL nibRegistered = NO;
if(!nibRegistered){
    UINib *nib = [UINib nibWithNibName:@"captionCell" bundle:nil];
    [self.personTable registerNib:nib forCellReuseIdentifier:captionCellWithIdentifier];
    nibRegistered = YES;
}


captionCell *cell = [self.personTable dequeueReusableCellWithIdentifier:captionCellWithIdentifier];
if(cell == nil){
    cell = [[captionCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:captionCellWithIdentifier];
}


cell.contentView.backgroundColor = [UIColor grayColor];

cell.firstTitle.text = @"3月4日 艺人新媒体指数";
cell.firstTitle.textColor = [UIColor whiteColor];
cell.secondTitle.text = @"www.vlinkage.com";
cell.secondTitle.textColor = [UIColor whiteColor];
cell.selectionStyle=UITableViewCellSelectionStyleNone;
return cell;
```
