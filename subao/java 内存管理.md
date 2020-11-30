# java 内存管理

### jvm 内存模型

![](http://www.bo56.com/wp-content/uploads/2016/03/jvm_m_l.png)

-Xms设置堆的最小空间大小。

-Xmx设置堆的最大空间大小。

-XX:NewSize设置新生代最小空间大小。

-XX:MaxNewSize设置新生代最大空间大小。

-XX:PermSize设置永久代最小空间大小。

-XX:MaxPermSize设置永久代最大空间大小。

老年代：2/3的堆空间
年轻代：1/3的堆空间
eden区：8/10 的年轻代
survivor0: 1/10 的年轻代
survivor1:1/10的年轻代

**程序计数器(线程私有)：**
是当前线程锁执行字节码的行号治时期，每条线程都有一个独立的程序计数器，这类内存也称为“线程私有”的内存。正在执行java方法的话，计数器记录的是虚拟机字节码指令的地址(当前指令的地址)。如果是Natice方法，则为空。

**java 虚拟机栈**
也是线程私有的。
每个方法在执行的时候也会创建一个栈帧，存储了局部变量，操作数，动态链接，方法返回地址。
每个方法从调用到执行完毕，对应一个栈帧在虚拟机栈中的入栈和出栈。
通常所说的栈，一般是指在虚拟机栈中的局部变量部分。
局部变量所需内存在编译期间完成分配，
如果线程请求的栈深度大于虚拟机所允许的深度，则StackOverflowError。
如果虚拟机栈可以动态扩展，扩展到无法申请足够的内存，则OutOfMemoryError。
**本地方法栈（线程私有）**
和虚拟机栈类似，主要为虚拟机使用到的Native方法服务。也会抛出StackOverflowError 和OutOfMemoryError。

**Java堆（线程共享）**
被所有线程共享的一块内存区域，在虚拟机启动的时候创建，用于存放对象实例。
对可以按照可扩展来实现（通过-Xmx 和-Xms 来控制）
当队中没有内存可分配给实例，也无法再扩展时，则抛出OutOfMemoryError异常。
**方法区（线程共享）**
被所有方法线程共享的一块内存区域。
用于存储已经被虚拟机加载的类信息，常量，静态变量等。
这个区域的内存回收目标主要针对常量池的回收和堆类型的卸载

### jvm 垃圾判断方式:

**1. 引用计数法（基本不用）**

- 给对象中添加一个引用计数器，每当有一个地方引用它时，计数器值加1
- 当引用失效时，计数器减1
- 当计数器值为 0 时代表该对象不可能再被使用，将会被当作垃圾回收

**2. 可达性分析法（常用）**

 通过一系列”GC Roots”对象作为起始点，从这些节点开始向下搜索，搜索所走过和路径称为引用链（Reference Chain），当一个对象到GC Roots没有任何引用链相连时（从GC Roots到这个对象不可达），则证明该对象是不可用的，可以作为 GC Roots 的有：

- 虚拟机栈中本地变量表中引用的对象

- 方法区中静态属性引用的对象

- 方法区中常量引用的对象

- 本地方法栈中 JNI（Native 方法）引用的对象

  ![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9waWN0dXJlcy5odWF6YWkuZnVuL3VQaWMvaW1hZ2UtMjAyMDA4MTcxMTE3MDI5NjQucG5n?x-oss-process=image/format,png)

### jvm 垃圾收集算法

- 标记清除
- 复制
- 标记整理


<table>
	<tr>
		<td>
			<img src="http://files.jb51.net/file_images/article/201605/201605151037404.jpg" border=0>
		</td>
		<td>
			<img src="http://files.jb51.net/file_images/article/201605/201605151037405.jpg"  border=0>
		</td>
	</tr>
</table>


### jvm 垃圾回收器

![](https://img-blog.csdnimg.cn/20190222222328910.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l2YV9icm90aGVy,size_16,color_FFFFFF,t_70)

1. **Serial**：单线程串行收集器，使用复制算法回收年轻代
2. **ParNew**：多线程并行收集器，使用复制算法回收年轻代
3. **Parallel Scavenge**：多线程并行收集器，使用复制算法回收年轻代
4. **Serial Old**：类似Serial，单线程串行收集器，使用标记整理算法回收老年代
5. **CMS**：并发标记整理的收集器，使用标记清除算法回收老年代
6. **Parallel Old**：类似ParNew和Parallel Scavenge，使用标记整理算法回收老年代
7. **zgc**:jdk11

### cms介绍

**CMS(并发GC)收集器**

CMS(Concurrent Mark Sweep)收集器是一种以获取最短回收停顿时间为目标的收集器。CMS收集器是基于“标记-清除”算法实现的，整个收集过程大致分为4个步骤：

①.初始标记(CMS initial mark)

②.并发标记(CMS concurrenr mark)

③.重新标记(CMS remark)

④.并发清除(CMS concurrent sweep)

其中初始标记、重新标记这两个步骤任然需要停顿其他用户线程。初始标记仅仅只是标记出GC ROOTS能直接关联到的对象，速度很快，并发标记阶段是进行GC ROOTS 根搜索算法阶段，会判定对象是否存活。而重新标记阶段则是为了修正并发标记期间，因用户程序继续运行而导致标记产生变动的那一部分对象的标记记录，这个阶段的停顿时间会被初始标记阶段稍长，但比并发标记阶段要短。
由于整个过程中耗时最长的并发标记和并发清除过程中，收集器线程都可以与用户线程一起工作，所以整体来说，CMS收集器的内存回收过程是与用户线程一起并发执行的。
**CMS收集器的优点：**并发收集、低停顿

**CMS收集器主要有三个显著缺点：**
**1. CMS收集器对CPU资源非常敏感**。在并发阶段，虽然不会导致用户线程停顿，但是会占用CPU资源而导致引用程序变慢，总吞吐量下降。CMS默认启动的回收线程数是：(CPU数量+3) / 4。虚拟机提供了一种称为“增量式并发收集器”的CMS收集器变种，可以在并发标记、清理的时候让GC线程、用户线程交替运行，尽量减少GC线程的独占资源的时间。
**2. CMS收集器无法处理浮动垃圾**，可能出现“Concurrent Mode Failure“，失败后而导致另一次Full GC的产生。由于CMS并发清理阶段用户线程还在运行，伴随程序的运行自热会有新的垃圾不断产生，这一部分垃圾出现在标记过程之后，CMS无法在本次收集中处理它们，只好留待下一次GC时将其清理掉。这一部分垃圾称为“浮动垃圾”。也是由于在垃圾收集阶段用户线程还需要运行，即需要预留足够的内存空间给用户线程使用，因此CMS收集器不能像其他收集器那样等到老年代几乎完全被填满了再进行收集，需要预留一部分内存空间提供并发收集时的程序运作使用。在默认设置下，CMS收集器在老年代使用了68%的空间时就会被激活，也可以通过参数-XX:CMSInitiatingOccupancyFraction的值来提供触发百分比，以降低内存回收次数提高性能。要是CMS运行期间预留的内存无法满足程序其他线程需要，就会出现“Concurrent Mode Failure”失败，这时候虚拟机将启动后备预案：临时启用Serial Old收集器来重新进行老年代的垃圾收集，这样停顿时间就很长了。所以说参数-XX:CMSInitiatingOccupancyFraction设置的过高将会很容易致“Concurrent Mode Failure”失败，性能反而降低。
**3. 碎片化，**最后一个缺点，CMS是基于“标记-清除”算法实现的收集器，使用“标记-清除”算法收集后，会产生大量碎片。空间碎片太多时，将会给对象分配带来很多麻烦，比如说大对象，内存空间找不到连续的空间来分配不得不提前触发一次Full GC。为了解决这个问题，CMS收集器提供了一个-XX:UseCMSCompactAtFullCollection开关参数，用于在Full GC之后增加一个碎片整理过程，还可通过-XX:CMSFullGCBeforeCompaction参数设置执行多少次不压缩的Full GC之后，跟着来一次碎片整理过程。

### 常用jvm参数

| 参数                                   | 描述                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| -XX:+UseSerialGC                       | Jvm运行在Client模式下的默认值，打开此开关后，使用Serial + Serial Old的收集器组合进行内存回收 |
| -XX:+UseParNewGC                       | 打开此开关后，使用ParNew + Serial Old的收集器进行垃圾回收    |
| -XX:+UseConcMarkSweepGC                | 使用ParNew + CMS + Serial Old的收集器组合进行内存回收，Serial Old作为CMS出现“Concurrent Mode Failure”失败后的后备收集器使用。 |
| -XX:+UseParallelGC                     | Jvm运行在Server模式下的默认值，打开此开关后，使用Parallel Scavenge + Serial Old的收集器组合进行回收 |
| -XX:+UseParallelOldGC                  | 使用Parallel Scavenge + Parallel Old的收集器组合进行回收     |
| -XX:SurvivorRatio                      | 新生代中Eden区域与Survivor区域的容量比值，默认为8，代表Eden:Subrvivor = 8:1 |
| -XX:PretenureSizeThreshold             | 直接晋升到老年代对象的大小，设置这个参数后，大于这个参数的对象将直接在老年代分配 |
| -XX:MaxTenuringThreshold               | 晋升到老年代的对象年龄，每次Minor GC之后，年龄就加1，当超过这个参数的值时进入老年代 |
| -XX:UseAdaptiveSizePolicy              | 动态调整java堆中各个区域的大小以及进入老年代的年龄           |
| -XX:+HandlePromotionFailure            | 是否允许新生代收集担保，进行一次minor gc后, 另一块Survivor空间不足时，将直接会在老年代中保留 |
| -XX:ParallelGCThreads                  | 设置并行GC进行内存回收的线程数                               |
| -XX:GCTimeRatio                        | GC时间占总时间的比列，默认值为99，即允许1%的GC时间，仅在使用Parallel Scavenge 收集器时有效 |
| -XX:MaxGCPauseMillis                   | 设置GC的最大停顿时间，在Parallel Scavenge 收集器下有效       |
| **-XX:CMSInitiatingOccupancyFraction** | 设置CMS收集器在老年代空间被使用多少后出发垃圾收集，默认值为68%，仅在CMS收集器时有效，-XX:CMSInitiatingOccupancyFraction=70, 配置XX:+UseCMSInitiatingOccupancyOnly后有效，默认92% |
| -XX:+UseCMSCompactAtFullCollection     | 由于CMS收集器会产生碎片，此参数设置在垃圾收集器后是否需要一次内存碎片整理过程，仅在CMS收集器时有效 |
| -XX:+CMSFullGCBeforeCompaction         | 设置CMS收集器在进行若干次垃圾收集后再进行一次内存碎片整理过程，通常与UseCMSCompactAtFullCollection参数一起使用 |
| -XX:+UseFastAccessorMethods            | 原始类型优化                                                 |
| -XX:+DisableExplicitGC                 | 是否关闭手动System.gc                                        |
| -XX:+CMSParallelRemarkEnabled          | 降低标记停顿                                                 |
| -XX:LargePageSizeInBytes               | 内存页的大小不可设置过大，会影响Perm的大小，-XX:LargePageSizeInBytes=128m |

XX:MinHeapFreeRatio=30  XX:MaxHeapFreeRatio=70

#### 1.开启GC日志

- **-verbose:gc**：打印GC日志
- **-XX:+PrintGCDateStamps**：打印GC日志时间戳
- **-XX:PrintGCDetails**：打印GC日志详情
- **-XX:+PrintGCTimeStamps**：打印此次GC距离JVM开始运行的时间
- **-XX:+PrintGCApplicationStopedTime**：打印GC造成的应用暂停时间
- **-XX:+PrintTenuringDistribution**：打印对象晋升日志

#### 2.通用参数

- **-XX:+HeapDumpOnOutOfMemoryError**：内存溢出时，产生heap dump文件
- **-Xloggc:**：将GC日志输出到指定文件
- **-XX:-+DisableExplicitGC**：禁用System.gc()，该方法默认会触发FGC
- **-XX:MaxTenuringThreshold**： 新生代 to 区的对象在经过多次 GC 后，如果还没有死亡，则认为他是一个老对象，则可以晋升到老年代，默认是15。但该参数不是唯一决定对象晋升的条件，当 to区不够或者该对象年龄已经达到了平均晋升值或者大对象等等条件
- **-XX:TargetSurvivorRatio** 决定对何时晋升的不仅只有 XX:MaxTenuringThreshold 参数，如果在Survivor空间中相同年龄所有对象大小的总和大于Survivor空间的一半（默认50%）
- **-XX:+UseTLAB**：启用线程本地分配缓存，默认开启
- **-XX:+PrintTLAB**：打印TLAB的使用情况

### 常见问题

- cpu高
  - 查看线程数，确定是部分线程一直占用cpu,还是线程数太多导致cpu一直在运行
  
    ```she
    cat /proc/3979/status | grep Threads
    Threads:        672
    ```
  
    
  
  - 如果部分线程一直占用cpu，打印这部分线程堆栈，查看对应堆栈代码，确定问题
  
  - 如果线程数太多，查看线程id（编程中给线程指定有意义的id，方便定位问题）,看是否有规律，找到生成线程的地方
  
  - 一般线程太多，都是一类的线程很多，容易确定生成线程的位置
  
- oom
  
  - 通过jcmd设置内存基础先，查看内存变化，确定内存溢出区域
  
    ```shell
    sudo jcmd 7342 VM.native_memory baseline
    7342:
    Baseline succeeded
    
    
    //以下增加的内存都是基于上一步设置的参考线
    sudo jcmd 7342 VM.native_memory summary.diff scale=MB
    7342:
    
    Native Memory Tracking:
    
    Total: reserved=8989MB +18MB, committed=3955MB +18MB
    
    -                 Java Heap (reserved=6144MB, committed=2048MB)
                                (mmap: reserved=6144MB, committed=2048MB)
     
    -                     Class (reserved=1536MB +17MB, committed=763MB +17MB)
                                (classes #95356 +3280)
                                (malloc=36MB +1MB #365123 +13128)
                                (mmap: reserved=1500MB +16MB, committed=727MB +16MB)
     
    -                    Thread (reserved=501MB, committed=501MB)
                                (thread #498)
                                (stack: reserved=499MB, committed=499MB)
                                (malloc=2MB #2498)
                                (arena=1MB #990)
     
    -                      Code (reserved=264MB, committed=116MB)
                                (malloc=20MB #26062)
                                (mmap: reserved=244MB, committed=95MB)
     
    -                        GC (reserved=44MB, committed=28MB)
                                (malloc=22MB #77679 +3280)
                                (mmap: reserved=23MB, committed=7MB)
     
    -                  Compiler (reserved=2MB, committed=2MB)
                                (malloc=1MB #3019)
     
    -                  Internal (reserved=307MB +1MB, committed=307MB +1MB)
                                (malloc=307MB +1MB #185414 +6569)
     
    -                    Symbol (reserved=53MB, committed=53MB)
                                (malloc=51MB #511849 +3280)
                                (arena=3MB #1)
     
    -    Native Memory Tracking (reserved=18MB, committed=18MB)
                                (tracking overhead=18MB)
     
    -                   Unknown (reserved=119MB, committed=119MB)
                                (mmap: reserved=119MB, committed=119MB)
    
    ```
  
    
  
  - 通过jmap(与 jcmd 7342 GC.class_histogram 功能类似，可以查看已经加载的对象)查看内存变化（可以dump内存，但是dump会触发fullGc）
  
    ```shell
    sudo jmap -histo 7342 | head -n 20
    
     num     #instances         #bytes  class name
    ----------------------------------------------
       1:        688417       86779336  [C
       2:        296765       51910432  [I
       3:        670201       49187576  [Ljava.lang.Object;
       4:        464886       41947112  [Ljava.lang.Class;
       5:         45828       25364608  [B
       6:        247230       19777256  [S
       7:        192389       15391120  java.lang.reflect.Constructor
       8:        107286       11281880  java.lang.Class
       9:        228291       10957968  java.util.HashMap
      10:        106180        9343840  java.lang.reflect.Method
      11:        317866        7628784  java.lang.String
      12:         87903        6329016  sun.reflect.DelegatingClassLoader
      13:         95503        6268792  [Ljava.util.Hashtable$Entry;
      14:        176634        5652288  java.util.Vector
      15:         87870        4920720  java.lang.Class$ReflectionData
      16:         94871        4553808  java.util.Hashtable
      17:        111911        4476440  java.lang.ref.SoftReference
    
    
    sudo jcmd 7342 GC.class_histogram | head -n 20
    7342:
    
     num     #instances         #bytes  class name
    ----------------------------------------------
       1:        167725       13775344  [C
       2:         11815       11623240  [B
       3:         50801        7531224  [Ljava.lang.Object;
       4:        151431        3634344  java.lang.String
       5:         13670        2405520  [I
       6:         24422        2387912  [Ljava.util.HashMap$Node;
       7:         19837        2187184  java.lang.Class
       8:         66185        2117920  java.util.HashMap$Node
       9:         33320        1332800  java.util.LinkedHashMap$Entry
      10:          2028        1330368  io.netty.util.internal.shaded.org.jctools.queues.MpscArrayQueue
      11:         17314        1246608  java.lang.reflect.Field
      12:         37804        1209728  java.util.concurrent.ConcurrentHashMap$Node
      13:         25150        1207200  java.util.HashMap
      14:         13672        1203136  java.lang.reflect.Method
      15:         14961         957504  java.util.concurrent.ConcurrentHashMap
      16:         38458         922992  java.util.ArrayList
    
    ```
  
    
  
  - 如果dump了内存，可以使用mat查看内存数据
  
  - 确定内存溢出的对象
  
  - reviewer代码,查找内存溢出位置
  
  - 确定问题

### 常用工具

-  jmap(主要用于打印指定Java进程(或核心文件、远程调试服务器)的共享对象内存映射或堆内存细节)
-  jstat(对Java应用程序的资源和性能进行实时的命令行的监控,包括了对Heap size和垃圾回收状况的监控)
-  jinfo(查看jvm参数)
-  jcmd(jcmd是jdk自带的一个神器，能够很方便的对java程序进行profiling。jcmd其实可以替代很多常用的工具，比如jstak，jmap)

- arthas

- gc-viewer

- mat 



https://www.jianshu.com/p/76959115d486

`jcmd`: http://www.manongjc.com/article/7558.html

`jstat`: https://www.cnblogs.com/bbox/p/9750361.html

`jmap`: https://www.cnblogs.com/huanglog/p/10302901.html

`cms`: https://blog.csdn.net/insomsia/article/details/91802923 https://www.jianshu.com/p/61bf0e9011c4

`垃圾回收算法`: https://www.cnblogs.com/aspirant/p/8662690.html

`对象分配`：https://blog.csdn.net/qq_34337272/article/details/82177383

`垃圾判断`：https://blog.csdn.net/LAf_HUAZAI/article/details/108108856

`jvm参数`：https://www.cnblogs.com/sjxbg/p/9388615.html

`gc收集器`：https://www.cnblogs.com/lxyit/p/10374183.html

`内存模型`：https://www.jianshu.com/p/76959115d486







