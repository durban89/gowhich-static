---
title: Codeigniter 缓存文件的使用 函数封装
tags:
  - PHP
  - Codeigniter
categories:
  - 技术
date: 2025-06-27 14:15:12
---

Codeigniter 缓存文件的使用 函数封装

```php
if(!function_exists('cache_read')){
    function cache_read($file, $dir = '', $mode = '') {
        $file = _get_cache_file($file, $dir);
        if(!is_file($file)) return NULL;
        return $mode ? read_file($file) : include $file;
    }
}
  
if(!function_exists('cache_write')){
    function cache_write($file, $string, $dir = '') {
        if(is_array($string)) {
            $string = "<?php return ".var_export($string, true)."; ?>";
            $string =  str_replace(array(chr(13), chr(10), "\n", "\r", "\t", '  '),array('', '', '', '', '', ''), $string);
        }
        $file = _get_cache_file($file, $dir);
        return write_file($file, $string);
    }
}
  
  
if(!function_exists('cache_delete')){
    function cache_delete($file, $dir = '') {
        $file = _get_cache_file($file, $dir);
        return unlink($file);
    }
}
  
  
if(!function_exists('_get_cache_file')){
    function _get_cache_file($file, $dir) {
        $path = config_item('cache_path') ? config_item('cache_path') : APPPATH . 'cache/';
        return ($dir ? $path.$dir.'/'.$file : $path.$file);
    }
}
```

