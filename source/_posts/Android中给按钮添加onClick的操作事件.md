---
title: Android中给按钮添加onClick的操作事件
tags:
  - Android
categories:
  - 技术
date: 2025-07-03 11:58:34
---

```java
//第一步：声明一个button
private Button button;
//实例化这个button
button = (Button) this.findViewById(R.id.button);
//给这个button添加onclick事件
button.setOnclickListener(new View.OnClickListener(){
	@Override
	public void onClick(View view){
		Intent intent = new Intent(MainActivity.this, OtherActivity.class);
		intent.putExtra("key","value");
		startActivity(intent);
	}
})
```


