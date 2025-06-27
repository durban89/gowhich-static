---
title: iOS7 中 UIActionSheet的简单应用
tags:
  - iOS
categories:
  - 技术
date: 2025-06-27 09:45:21
---

UIActionSheet简单的应用

```objectivec
UIActionSheet *actionSheet = [[UIActionSheet alloc] initWithTitle:@"请选择背景图片的来源"
                                                         delegate:self
                                                cancelButtonTitle:@"取消"
                                           destructiveButtonTitle:nil
                                                otherButtonTitles:@"拍照",@"相册",@"图片库",nil];

actionSheet.actionSheetStyle = UIActionSheetStyleDefault;
[actionSheet showInView: self.view];
```

