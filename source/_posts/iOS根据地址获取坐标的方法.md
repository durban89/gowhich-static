---
title: iOS根据地址获取坐标的方法
tags:
  - iOS
categories:
  - 技术
date: 2025-06-17 14:43:45
---

只要地址，中文也可以，英文也可以的

在使用之前要引入包**CoreLocation**

代码实例如下：

```objectivec
NSString *oreillyAddress = @"上海";  //测试使用中文也可以找到经纬度具体的可以多尝试看看~

CLGeocoder *myGeocoder = [[CLGeocoder alloc] init];
[myGeocoder geocodeAddressString:oreillyAddress completionHandler:^(NSArray *placemarks, NSError *error) {
    if ([placemarks count] > 0 && error == nil) {
        NSLog(@"Found %lu placemark(s).", (unsigned long)[placemarks count]);
        CLPlacemark *firstPlacemark = [placemarks objectAtIndex:0];
        NSLog(@"Longitude = %f", firstPlacemark.location.coordinate.longitude);
        NSLog(@"Latitude = %f", firstPlacemark.location.coordinate.latitude);
    }
    else if ([placemarks count] == 0 && error == nil) {
        NSLog(@"Found no placemarks.");
    }
    else if (error != nil) {
        NSLog(@"An error occurred = %@", error); }
}];
```

参看文章：

http://blog.csdn.net/bihailantian1988/article/details/7618980

