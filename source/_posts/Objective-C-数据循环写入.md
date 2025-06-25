---
title: Objective-C 数据循环写入
tags:
  - Objective-C
categories:
  - 技术
date: 2025-06-25 10:09:51
---

gowhich最近手痒写了一个小练习，关于object－c的小练习。

将日期按照制定的格式，循环写入文件中

写入的实现方法：

```objectivec
-(void) writeRun
{
    NSFileManager *fileManager = [NSFileManager defaultManager];
    NSString *homePath = NSHomeDirectory();
    NSString *filePath = [homePath stringByAppendingPathComponent:@"data_date.txt"];
    
    BOOL success = [fileManager createFileAtPath:filePath
                                        contents:nil
                                      attributes:nil];
    
    if(success)
    {
        NSLog(@"创建文件 %@ 成功",filePath);
    }
    
    NSFileHandle *fileHandle = [NSFileHandle fileHandleForWritingAtPath:filePath];
    [NSTimer scheduledTimerWithTimeInterval:1
                                     target:self
                                   selector:@selector(timerAction:)
                                   userInfo:fileHandle
                                    repeats:YES];
}

-(void) timerAction:(NSTimer *)timer
{
    static int n = 0;
    NSFileHandle *filehandle = timer.userInfo;
    [filehandle seekToEndOfFile];
    
    NSDate *nowDate = [NSDate date];
    NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
    [formatter setDateFormat:@"yyyy/MM/dd HH:mm:ss"];
    NSString *dateString = [formatter stringFromDate:nowDate];
    dateString = [dateString stringByAppendingString:@"\n"];
    NSData *dateData = [dateString dataUsingEncoding:NSUTF8StringEncoding];
    [filehandle writeData:dateData];
    
    if(n == 10)
    {
        [timer invalidate];
        [filehandle closeFile];
    }
    n++;
}
```

实现运行，进行调用

```objectivec
#import "WriteDate.h"

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        WriteDate *write = [[WriteDate alloc] init];

        [write writeRun];
        
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    [[NSRunLoop currentRunLoop] run];
    return 0;
}
```

文件中的数据结果是，如下：

```bash
2013/11/13 09:22:03
2013/11/13 09:22:04
2013/11/13 09:22:05
2013/11/13 09:22:06
2013/11/13 09:22:07
2013/11/13 09:22:08
2013/11/13 09:22:09
2013/11/13 09:22:10
2013/11/13 09:22:11
2013/11/13 09:22:12
2013/11/13 09:22:13
```
