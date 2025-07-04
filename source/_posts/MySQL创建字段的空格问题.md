---
title: MySQL创建字段的空格问题
tags:
  - MySQL
categories:
  - 技术
date: 2025-06-09 18:10:19
---
下面举例子中空格我用【X】来表示

请看这条sql语句

```sql
INSERT INTO teleplay_tieba_daily
        (`t_t_id`,`sum`,`post_sum`,`subject_sum`,`member_sum`,`check_sum`,`yesterday_fans_num`, `yesterday_post_num`, `yesterday_subject_num`,`yesterday_member_num`, `yesterday_check_num`,`spider_date`)
        VALUES (236,1790,24728,1837,1790,17,0,0,0,0,0,'2013-04-22'),(240,239,6824,1082,239,5,0,0,0,0,0,'2013-04-22'),(5109,171,300,90,171,4,0,0,0,0,0,'2013-04-22'), (5139,97,2462,294,97,1,0,0,0,0,0,'2013-04-22'),(5153,36,1215,181,36,0,0,0,0,0,0,'2013-04-22'),(5276,26,759,115,26,0,0,0,0,0,0,'2013-04-22'),(5358,53,320,93,53,0,0,0,0,0,0,'2013-04-22'),(5387,3156,85687,4389,3156,54,0,0,0,0,0,'2013-04-22'),(5429,1181,13811,2430,1181,14,0,0,0,0,0,'2013-04-22'),(5480,46,749,117,46,0,0,0,0,0,0,'2013-04-22')
```
按道理说是没有问题的，但是给出的错误是：

Unknown column 'yesterday_check_num' in 'field list'
注意，是字段没有

反复看了一下，通过借助phpmyadmin的选择字段的方式添加数据，执行后，居然成功了

```sql
INSERT INTO teleplay_tieba_daily
        (`t_t_id`,`sum`,`post_sum`,`subject_sum`,`member_sum`,`check_sum`,`yesterday_fans_num`, `yesterday_post_num`,`yesterday_subject_num`, `yesterday_member_num`,`【x】yesterday_check_num`,`spider_date`)
        VALUES (236,1790,24728,1837,1790,17,0,0,0,0,0,'2013-04-22'),(240,239,6824,1082,239,5,0,0,0,0,0,'2013-04-22'),(5109,171,300,90,171,4,0,0,0,0,0,'2013-04-22'),(5139,97,2462,294,97,1,0,0,0,0,0,'2013-04-22'), (5153,36,1215,181,36,0,0,0,0,0,0,'2013-04-22'),(5276,26,759,115,26,0,0,0,0,0,0,'2013-04-22'),(5358,53,320,93,53,0,0,0,0,0,0,'2013-04-22'),(5387,3156,85687,4389,3156,54,0,0,0,0,0,'2013-04-22'),(5429,1181,13811,2430,1181,14,0,0,0,0,0,'2013-04-22'),(5480,46,749,117,46,0,0,0,0,0,0,'2013-04-22')
```
发现字段的真相是'【x】yesterday_check_num'，但是我想，我最初在创建字段的时候，为什么mysql没有把左右两边的空格过滤掉，这是漏洞还是mysql故意要这样设计的呢？如果有一天一个像我一样的程序员，也做了类似的事情，后面的程序员做sql插入的时候，估计会很困惑。因为这个问题，不去仔仔细细的查找，根本找不出原因。

另外程序员在处理输入的字符的时候都会将两边的空格去掉才对
