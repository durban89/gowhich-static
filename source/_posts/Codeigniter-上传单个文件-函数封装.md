---
title: Codeigniter 上传单个文件 函数封装
tags:
  - PHP
  - Codeigniter
categories:
  - 技术
date: 2025-06-27 14:15:09
---

Codeigniter 上传单个文件 函数封装，记录下，方便以后使用

```php
if(!function_exists('upload_file')){
  
    function upload_file($field,$filetype,$maxsize){
        $CI = & get_instance();
        $CI->load->library('upload');
        $CI->upload->initialize(array('encrypt_name'=>TRUE,'overwrite'=>TRUE));
        $CI->upload->set_upload_path('static/attachments');
        $CI->upload->set_allowed_types($filetype);
        $CI->upload->set_max_filesize($maxsize);
        $CI->upload->do_upload($field);
        $info = $CI->upload->data();
        if($info['client_name']){
            return '/static/attachments/'.$info['client_name'];
        }else{
            return '';
        }
    }
}
```

