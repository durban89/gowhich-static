---
title: Fixing the htmlspecialchars UTF-8 Error
tags:
  - PHP
categories:
  - 技术
date: 2025-06-20 14:33:42
---

If you’ve ever come across the infuriating error

```bash
htmlspecialchars(): Invalid multibyte sequence in argument
```

I have a simple solution for you: Turn `display_errors` on in your php.ini file!  
It turns out there’s a weird bug that doesn’t appear to be getting fixed any time soon that causes `htmlspecialchars()` to display this error only when `display_errors` is set to Off.

