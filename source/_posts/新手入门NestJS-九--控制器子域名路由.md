---
title: 新手入门NestJS（九）- 控制器子域名路由
tags:
  - NestJS
categories:
  - 技术
date: 2025-07-14 16:21:28
---

子域路由

@Controller装饰器提供了一个host选项可用，主要用来判断这个控制器在被访问的时候，限制具体的域名来访问

代码如下

```javascript
@Controller('cats')
@Controller({ host: 'api.gowhich.com' })
export class CatsController {
  @Get()
  findAll(@Req() request: Request): string {
    return 'This action will returns all cats';
  }
}
```

再举个例子

```javascript
@Controller('cats')
@Controller({ host: 'api.gowhich.com' })
export class CatsController {
  @Get()
  getInfo(@HostParam('account') account) {
    return account;
  }
}
```
