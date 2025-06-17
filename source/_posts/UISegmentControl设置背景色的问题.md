---
title: UISegmentControl设置背景色的问题
tags:
  - iOS
categories:
  - 技术
date: 2025-06-17 17:20:59
---

关于UISegmentControl设置背景色的问题，我也遇到了，还查找了不少的资料，最终答案我在文档里面找到了。

链接我记录一下：https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UISegmentedControl_Class/Reference/UISegmentedControl.html

搜索一下tintcolor就可以知道了，说的很清楚的

> tintColor The tint color of the segmented control. @property(nonatomic, retain) UIColor \*tintColor Discussion The default value of this property is nil (no color). UISegmentedControl uses this property only if the style of the segmented control is UISegmentedControlStyleBar.

说的就是，首先有个属性要改一下

```objectivec
sexSegment.segmentedControlStyle = UISegmentedControlStyleBar;
```

下面代码是我的：

```objectivec
NSArray *item = [[NSArray alloc] initWithObjects:@"男",@"女", nil];

UISegmentedControl *sexSegment = [[UISegmentedControl alloc] initWithItems:item];
sexSegment.layer.borderWidth = 0.0;
sexSegment.tintColor = [ColorConfig NavigationColor];    
sexSegment.segmentedControlStyle = UISegmentedControlStyleBar;
[sexSegment setFrame:CGRectMake(segmentX, segmentY, segmentWidth, segmentHeight)];
[sexSegment addTarget:self
               action:@selector(selectSex:)
     forControlEvents:UIControlEventValueChanged];

[_contentView addSubview:sexSegment];
```
