---
title: 如何使用Property Wrappers - State和Binding
tags:
  - Swift
categories:
  - 技术
date: 2025-07-15 09:50:57
---

### State Property Wrappers 的用法

示例如下

```cs
struct MyView: View {
    @State var myString: String = "Hello"
    var body: some View {
        OtherView(shareText: $myString)
    }
}
```

### Binding Property Wrappers 的用法

示例如下

```cpp
struct OtherView: View {
    @Binding var shareText: String

    var body: some View {
        Text(shareText)
    }
}
```

最后调用下MyView，如下（建议Playground中运行）

```cs
MyView(myString: "Hello world")
```
