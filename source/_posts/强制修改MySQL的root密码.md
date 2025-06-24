---
title: 强制修改MySQL的root密码
tags:
  - MySQL
categories:
  - 技术
date: 2025-06-24 15:04:32
---

遇到了一个问题，就是我的Mysql的root密码忘记了，怎么办呢，赶快去google哇，哈

根据参考找到了一个

### [方法1：用SET PASSWORD命令](#1)

```bash
mysql -u root
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass');
```

### [方法2：用mysqladmin](#2)

```bash
mysqladmin -u root password "newpass"
```

如果root已经设置过密码，采用如下方法

```bash
mysqladmin -u root password oldpass "newpass"
```

### [方法3：用UPDATE直接编辑user表](#3)

```bash
mysql> use mysql;
mysql> UPDATE user SET Password = PASSWORD('newpass') WHERE user = 'root';
mysql> FLUSH PRIVILEGES;
```

### [方法4：在丢失root密码的时候，可以这样](#4)

```bash
mysql -u root mysql
mysql> UPDATE user SET password=PASSWORD("new password") WHERE user='root';
mysql> FLUSH PRIVILEGES;
```

在另外一个文章里面找到了上面第四个方法类似的，如下：

#### [第一：首先要把mysqld停止](#4-1)

```bash
service mysqld stop
```

这里我在ubuntu上测试失败,如果没有用，可是试试下面的方法

```bash
/etc/init.d/mysql stop
```

#### [第二：启动mysql，但是要跳过权限表](#4-2)

```bash
/usr/local/mysql/bin/mysqld_safe --skip-grant-tables &
```

我直接使用的是

```bash
mysqld_safe --skip-grant-tables &
```

#### [第三：进去mysql，并修改密码](#4-3)

```bash
mysql -u root 
mysql>use mysql; 
mysql>update user set password=password("new_pass") where user="root"; 
mysql>flush privileges; 
mysql>\q
```

#### [第四：重新启动mysql，正常进入](#4-4)

```bash
/etc/init.d/mysql start
```

---

参考文章：

<http://www.linuxidc.com/Linux/2008-02/11137.htm>

<http://itindex.net/detail/36040-mysql-%E6%95%B0%E6%8D%AE%E5%BA%93-root>

<http://blog.csdn.net/phpandjava/article/details/4636610>

