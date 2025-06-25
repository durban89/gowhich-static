---
title: Objective-C 归档和解归档 NSKeyedArchiver NSKeyedUnarchiver
tags:
  - Objective-C
categories:
  - 技术
date: 2025-06-25 10:26:31
---

关于object-c中的归档和解归档的使用，gowhich列出了两个比较的简单的联系的例子

第一个练习：

```objectivec
//数据归档
NSString *homeDirectory = NSHomeDirectory();
NSArray *array = [NSArray arrayWithObjects:@"One",@"Two",@999,@"Three",@"Four", nil];
NSString *filePath = [homeDirectory stringByAppendingPathComponent:@"data.archive"];
BOOL success = [NSKeyedArchiver archiveRootObject:array
                                           toFile:filePath];
if(success)
{
    NSLog(@"archive success");
}

//数据解归档
NSString *homeDir = NSHomeDirectory();
NSString *dataFilePath = [homeDir stringByAppendingPathComponent:@"data.archive"];
NSArray *dataArray = [NSKeyedUnarchiver unarchiveObjectWithFile:dataFilePath];

NSLog(@"dataArray = %@",dataArray);
```

第二个练习：

```objectivec
//数据归档
NSString *homeDir = NSHomeDirectory();
NSString *filePath = [homeDir stringByAppendingPathComponent:@"customData.archive"];
NSMutableData *data = [NSMutableData data];
NSKeyedArchiver *archiver = [[NSKeyedArchiver alloc] initForWritingWithMutableData:data];
NSArray *array = [NSArray arrayWithObjects:@"One",@"Two",@"Three", nil];
[archiver encodeObject:array
                forKey:@"number"];
[archiver encodeInt:999
             forKey:@"num"];
[archiver finishEncoding];

BOOL success = [data writeToFile:filePath
       atomically:YES];
if(success)
{
    NSLog(@"archive success");
}

//数据解归档
NSString *homeDirectory = NSHomeDirectory();
NSString *dataFilePath = [homeDirectory stringByAppendingPathComponent:@"customData.archive"];
NSData *unarchiveData = [NSData dataWithContentsOfFile:dataFilePath];
NSKeyedUnarchiver *unarchive = [[NSKeyedUnarchiver alloc] initForReadingWithData:unarchiveData];
int num = [unarchive decodeIntForKey:@"num"];
NSArray *unarchiveArray = [unarchive decodeObjectForKey:@"number"];
NSLog(@"num = %d , unarchiveArray = %@",num,unarchiveArray);
```

