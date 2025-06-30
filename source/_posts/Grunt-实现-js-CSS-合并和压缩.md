---
title: Grunt 实现 js、CSS 合并和压缩
tags:
  - Grunt
  - JavaScript
categories:
  - 技术
date: 2025-06-30 14:08:52
---

前提条件，知道如何安装nodejs、grunt，这里不做介绍，可以自行google

实现此功能需要安装的Grunt工具有如下

grunt-contrib-concat

grunt-contrib-uglify

grunt-css

1、实现js的合并和压缩

```js
module.exports = function(grunt) {
    // 配置
    grunt.initConfig({
        pkg : grunt.file.readJSON('package.json'),
        concat : {   //合并文件
            domop : {
                src: ['assets/test1.js', 'assets/test2.js'],  //源文件目录
                dest: 'dest/result.js'   //目标文件目录，自动创建dest目录
            }
        },
        uglify : {   //压缩文件
            options : {
                banner : '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
            },
            build : {
                src : 'dest/result.js',
                dest : 'dest/result.min.js'
            }
        }
    });
    // 载入concat和uglify插件，分别对于合并和压缩
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    // 注册任务
    grunt.registerTask('default', ['concat', 'uglify']);
};
```

2、实现css的合并和压缩

```js
module.exports = function(grunt){
    grunt.initConfig({
        pkg:grunt.file.readJSON('package.json'),
        concat:{
            css:{
                src:['assets/*.css'],
                dest:'dest/all.css',
            }
        },
        cssmin:{
            css: {
                src: 'dest/asset/all.css',
                dest: 'dest/asset/all-min.css'
            }
        }
  
    });
    // 载入concat和css插件
    grunt.loadNpmTasks('grunt-contrib-concat');//用于合并
    grunt.loadNpmTasks('grunt-css');//用于压缩
    grunt.registerTask('default',['concat','cssmin']);//任务
};
```


