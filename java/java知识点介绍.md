### java中的一些基本知识总结
+ [WeakReference java中对象的虚引用](http://blog.csdn.net/matrix_xu/article/details/8424038)

+ java新特性
接口的另一种使用方式
```java
 Interface A {
   C test(B b);
 }
```
如果在一个方法中需要传入A,例如：
```java
  void test2(A a){
    ...
  }
```
可以像下面这种写法
```java
  A a = b -> {
    C c = new C();
    return c;
  }

  test2(a);
```
