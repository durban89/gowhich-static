---
title: iOS NSDictionary操作简介
tags:
  - iOS
categories:
  - 技术
date: 2025-06-06 18:01:44
---
iOS NSDictionary 操作代码如下：

```c
- (void)loopThrough
   {
        NSArray * keys=[NSArray arrayWithObjects:@"key1“，@"key2",@"key3",nill];
        NSArray *objects=[NSArray arrayWithOjbects:@"how",@"are",@"you",nill];
 
        NSDictionary *dic=[NSDictionary dictionaryWithObjects:objects,forKeys:keys];

        //loop 1
        for(id key in dic)
        {
            NSLog(@"key:%@,value:%@"，key,[dic objectForKey:key]);
        }

        //loop 2
        NSEnumerator *enumerator;
        id key;
        enumerator=[dic keyEnumerator];
        while((key=[enumerator nextObject]))
          {
            NSLog(@"key:%@,value:%@",key,objectForKey:key]);
          }
   }

-(void)testNsMutableDictionary
   {
      NSMutableDictionary *dic=[NSMutableDictionary dictionaryWithCapacity:30];
      //dictionaryWithObjectsAndKeys:[NSMuble numberWithInt:1] @"math1",[NSMuble numberWithInt:2] @"math2"];

      [dic setObject:@"one" forKey:@"dog"];
      [dic setObject:@"two" forKey:@"cat"];
      [dic setValue:[NSString stringWithFormat:@"three"] forKey:@"pig"];


      [dic removeObjectForkey:@"cat"];
      [dic removeAllObjects];

      NSMutableArray arraylist=[[NSMutableArray alloc] init];
      [arrarlist addObject:dic];
      [dic release];
   }
 ```
