### LQRWeChat分析
#### 依赖包分析  
+ SDK中的一些方法：  
  1. TextUtils.isEmpty()
  2. TextWatcher  
      TextWatcher是一个文本变化监听接口，定义了三个接口，分别是beforeTextChanged,onTextChanged,afterTextCahnged.TextWatcher通常与TextView结合使用，以便在文本变化的不同时机做响应的处理。TextWatcher中三个回调接口都是使用了InputFilter过滤器过滤之后的文字字符作为新的字符对象。


+ com.jaeger.statusbaruitl:library:1.3.5  
      这是一个为Android App 设置状态栏的工具类， 可以在4.4及其以上系统中实现
      沉浸式状态栏/状态栏变色，支持设置状态栏透明度。

+ com.jakewharton:butterknife:7.0.1
      通过注解获取对应的资源id

+ compile 'com.zhy:autolayout:1.4.5'

+ PersistentCookieJar介绍使用
http://blog.csdn.net/pengguichu/article/details/73339329

+ me.tatarka:gradle-retrolambda:3.2.5
http://blog.csdn.net/nicolelili1/article/details/52275263

#### build.gradle中的一些配置
+ [AndroidStudio常见依赖格式](http://blog.csdn.net/csdn_lqr/article/details/51778316)
