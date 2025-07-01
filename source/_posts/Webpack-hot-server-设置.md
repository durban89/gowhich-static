---
title: webpack hot server 设置
tags:
  - Webpack
categories:
  - 技术
date: 2025-07-01 15:25:10
---

使用webpack时间越久，越觉得js越好玩，之前也写过一篇文章，但是太简陋啦。

最近在配置使用webpack hot server,整了很长时间，终于还是被我整的差不多了，而且还是正常使用啦。

我的项目不是那种静态的，我使用node做server去运行项目，然后调试js的。

主要的有一下几点

我把主要的几个文件列出来一下：

```bash
app.js
webpack.dev.server.js
webpack.config.js
```

以上几个是主要文件

在app.js里面我们要加入的配置如下

```js
if(process.env.NODE_ENV == 'dev') {
  require('./webpack.dev.server')(app)
}
webpack.dev.server.js的配置如下：
var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server');
var config = require('./webpack.config');
var proxy = require('proxy-middleware');
var url = require('url');
module.exports = function(app) {
  // 使用3000端口
  app.use('/js/out', proxy(url.parse('http://127.0.0.1:3000/js/out')));
  var server = new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    noInfo: false,
    historyApiFallback: true,
    stats: { colors: true },
  }).listen(3000, '127.0.0.1', function(err,result) {
    if (err) {
    console.log(err);
  }
  console.log('Listening at localhost:3000');
  });
}
```

这里的端口号是用来做异步操作的，当启动的时候会启动一个socket，并且会一直监听这个端口，这个端口号一定要理解好，因为我自己就有点被他搞晕了。

下面是webpack.config.js的配置

```js
entry: {
  'main':[
    'webpack-dev-server/client?http://127.0.0.1:3000', // WebpackDevServer host and port
    'webpack/hot/only-dev-server',
    './app/js/index.js'
  ] //演示单入口文件
},
output: {
  path: path.join(__dirname, 'app/js/out'),  //打包输出的路径
  filename: '[name].js',              //打包后的名字
  publicPath: "http://localhost:3000/js/out/" //html引用路径，在这里是本地地址。
},
```

最主要也是最需要担心的就是entry里面的

```js
'webpack-dev-server/client?http://127.0.0.1:3000', // WebpackDevServer host and port
'webpack/hot/only-dev-server',
```

还有output里面的

```js
publicPath: "http://localhost:3000/js/out/"
```

这里面的地址一定要使用一个具体的url地址，不然你会晕头，搞不清楚是为啥不起作用，这样做了就起作用了，而且要注意这里的端口号

好吧，可以启动开始开发测试了。

```js
NODE_ENV=dev app node.js
```

因为我们在app里面做了dev的判断，只有在开发的模式下才能做此动作，production模式就别这样做了。

你也可以把它加入到package的scripts里面

```js
"scripts": {
    "build": "webpack",
    "dev": "NODE_ENV=dev node app.js",
    "production": "webpack -p --config webpack.config.production.js"
  }
```

