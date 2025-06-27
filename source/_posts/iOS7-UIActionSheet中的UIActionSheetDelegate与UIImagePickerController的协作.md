---
title: iOS7 UIActionSheet中的UIActionSheetDelegate与UIImagePickerController的协作
tags:
  - iOS
categories:
  - 技术
date: 2025-06-27 09:45:23
---

UIActionSheet中的UIActionSheetDelegate与UIImagePickerController的协作，实现图片来源的选择，代码如下：

```objectivec
-(void) actionSheet:(UIActionSheet *)actionSheet clickedButtonAtIndex:(NSInteger)buttonIndex{
    UIImagePickerController *picker=[[UIImagePickerController alloc]init];
    picker.delegate=self;
    picker.allowsEditing=YES;
    
    switch (buttonIndex){
        case 0:
        {
            //拍照
            if ([UIImagePickerController isSourceTypeAvailable: UIImagePickerControllerSourceTypeCamera])
            {
                picker.sourceType=UIImagePickerControllerSourceTypeCamera;
            }
            else
            {
                return;
            }
        }
            break;
        case 1:
        {
            //相册
            if ([UIImagePickerController isSourceTypeAvailable: UIImagePickerControllerSourceTypePhotoLibrary])
            {
                picker.sourceType=UIImagePickerControllerSourceTypePhotoLibrary;
            }
        }
            break;
        case 2:
        {
            //图片库
            if ([UIImagePickerController isSourceTypeAvailable: UIImagePickerControllerSourceTypeSavedPhotosAlbum])
            {
                picker.sourceType=UIImagePickerControllerSourceTypeSavedPhotosAlbum;
            }
        }
            break;
        default:{
            return;
        }
            break;
    }
    
    if([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPhone){
        [self presentViewController:picker animated:YES completion:nil];
    }else{
        UIPopoverController * popOver = [[UIPopoverController alloc] initWithContentViewController: picker];
        popOver.delegate = self;
        _popOverController = popOver;
        [_popOverController presentPopoverFromRect:CGRectMake(0,100, 0, 0)
                                            inView:self.view
                              permittedArrowDirections:UIPopoverArrowDirectionUp
                                          animated:YES];
    }
}
```

这里加了一个UIPopoverController，但是UIPopoverController只能在ipad设备上面使用。

