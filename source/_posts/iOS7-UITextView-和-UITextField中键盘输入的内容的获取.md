---
title: iOS7 UITextView 和 UITextField中键盘输入的内容的获取
tags:
  - iOS
categories:
  - 技术
date: 2025-06-26 11:37:31
---

UITextField中的内容的获取方式：

```objectivec
-(void) textFieldDidEndEditing:(UITextField *)textField
{
    //获取输入的内容
    NSString *content = [textField text];
}
```

UITextView中的内容的获取方式：

```objectivec
-(BOOL)textView:(UITextView *)textView shouldChangeTextInRange:(NSRange)range replacementText:(NSString *)text      
{      
    
    if ([text isEqualToString:@"\n"]) {      
        
        [textView resignFirstResponder];
        return NO;      
        
    }
    else if(range.location >= 500)//如果输入超过规定的字数20，就不再让输入  
    {
        return  NO;
    }
    NSString *content = text;
    return YES;   
}
```

