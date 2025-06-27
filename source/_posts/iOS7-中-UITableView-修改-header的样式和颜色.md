---
title: IOS7 中 UITableView 修改 header的样式和颜色
tags:
  - iOS
categories:
  - 技术
date: 2025-06-27 09:45:49
---

IOS7 中 UITableView 如何 修改 header的样式和颜色，只需要使用下面的方法就好了

```objectivec
-(UIView *) tableView:(UITableView *)tableView viewForHeaderInSection:(NSInteger)section
{
    NSString *sectionTitle = [[self.list objectAtIndex:section] valueForKey:@"title"];
    
    // Create header view and add label as a subview
    UIView *view = [[UIView alloc] initWithFrame:CGRectMake(10.0,
                                                            0.0,
                                                            320.0,
                                                            100.0)];
    view.backgroundColor = [UIColor lightGrayColor];
    
    
    // Create label with section title
    UILabel *label = [[UILabel alloc] init];
    label.frame = CGRectMake(5.0,
                             12.0,
                             284.0,
                             24.0);
    label.textColor = [UIColor blackColor];
    label.font = [UIFont systemFontOfSize:16.0];
    label.text = sectionTitle;
    label.backgroundColor = [UIColor clearColor];
    
    [view addSubview:label];
    
    return view;
    
}
```

