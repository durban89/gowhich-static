---
title: Objective-C 文件分块写入 NSFileHandle NSFileManager
tags:
  - PHP
categories:
  - 技术
date: 2025-06-25 10:10:08
---

Objective-C文件的分块写入，实现大文件的copy，嘿嘿，实现起来是很简单的，终于知道，系统里面copy大文件是啥样子的啦，来看个代码

```objectivec
//读取大文件，并写入大文件中
NSFileManager *fileManager = [NSFileManager defaultManager];
NSString *homePath = NSHomeDirectory();
NSString *srcPath = [homePath stringByAppendingPathComponent:@"android学习路线图介绍.avi"];
NSString *targetPath = [homePath stringByAppendingPathComponent:@"android学习路线图介绍1.avi"];

BOOL success = [fileManager createFileAtPath:targetPath
                                    contents:nil
                                  attributes:nil];
if(success)
{
    NSLog(@"成功创建文件 ：%@",targetPath);
}

NSFileHandle *infile = [NSFileHandle fileHandleForWritingAtPath:targetPath];
NSFileHandle *outfile = [NSFileHandle fileHandleForReadingAtPath:srcPath];

//获取文件的尺寸
NSDictionary *fileAttr = [fileManager attributesOfItemAtPath:srcPath
                                                       error:nil];
NSNumber *fileSizeNum = [fileAttr objectForKey:NSFileSize];

BOOL isEnd = NO;
NSInteger readSize = 0;
NSInteger fileSie = [fileSizeNum longLongValue];

while (!isEnd) {
    NSData *data = nil;
    NSInteger subleng = fileSie - readSize;
    if(subleng < 500)
    {
        isEnd = YES;
        data = [outfile readDataToEndOfFile];
    }
    else
    {
        data = [outfile readDataOfLength:500];
        readSize += 500;
        [outfile seekToFileOffset:readSize];
    }
    [infile writeData:data];
}
[infile closeFile];
[outfile closeFile];
```

自己在根目录下面设置一个文件，我的这个文件有44.6M哦，虽然copy比较慢，但是文件是完整的，哈哈

