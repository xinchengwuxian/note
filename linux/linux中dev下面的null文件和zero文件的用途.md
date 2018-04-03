### linux中dev下面的null文件和zero文件的用途
- 概论 -- 来自维基的解释  

> **/dev/null**： 在类Unix系统中，/dev/null，或称空设备，是一个特殊的设备文件，它丢弃一切写入其中的数据（但报告写入操作成功），读取它则会立即得到一个EOF。
在程序员行话，尤其是Unix行话中，/dev/null 被称为位桶(bit bucket)或者黑洞(black hole)。空设备通常被用于丢弃不需要的输出流，或作为用于输入流的空文件。这些操作通常由重定向完成。


> **/dev/zero**： 在类UNIX 操作系统中, /dev/zero 是一个特殊的文件，当你读它的时候，它会提供无限的空字符(NULL, ASCII NUL, 0x00)。
其中的一个典型用法是用它提供的字符流来覆盖信息，另一个常见用法是产生一个特定大小的空白文件。BSD就是通过mmap把/dev/zero映射到虚地址空间实现共享内存的。可以使用mmap将/dev/zero映射到一个虚拟的内存空间，这个操作的效果等同于使用一段匿名的内存（没有和任何文件相关）。

- /dev/null 的日常使用  

> 把/dev/null看作"黑洞"。它等价于一个只写文件，并且所有写入它的内容都会永远丢失，而尝试从它那儿读取内容则什么也读不到。然而, /dev/null对命令行和脚本都非常的有用。

>我们都知道  cat $filename  会输出filename对应的文件内容（输出到标准输出）
而使用         cat $filename >/dev/null 则不会得到任何信息，因为我们将本来该通过标准输出显示的文件信息重定向到了 /dev/null 中，so what will you get ?
使用  cat $filename 1>/dev/null 也会得到同样的效果，因为默认重定向的 1 就是标准输出。  如果你对 shell 脚本或者重定向比较熟悉的话，应该会联想到 2 ，也即标准错误输出。
我们使用 cat $filename  时如果filename对应的文件不存在，系统肯定会报错： “ cat: filename: 没有那个文件或目录 ” 。
如果我们不想看到错误输出呢？我们可以禁止标准错误:   cat $badname 2>/dev/null
我们可以通过下面这个测试来更加深刻的理解/dev/null ：
```shell
<span style="font-size:18px">$cat test.txt   
just for test  
$cat test.txt >/dev/null   
$cat test.txt 1>/dev/null   
$cat test2.txt   
cat: test2.txt: 没有那个文件或目录  
$cat test2.txt >/dev/null   
cat: test2.txt: 没有那个文件或目录  
$cat test2.txt 2>/dev/null   
$  
</span>  
```

- /dev/zero 的日常使用

> 像/dev/null一样，/dev/zero也是一个伪文件，但它实际上产生连续不断的null的流（二进制的零流，而不是ASCII型的）。写入它的输出会丢失不见，/dev/zero主要的用处是用来创建一个指定长度用于初始化的空文件，像临时交换文件。

> 比如说，在我的前一篇博客中（《尝试安装Chrome OS的新版本 Vanilla & 安装之后U盘遇到的问题解决》），提到我使用dd 制作的U盘系统，而我的U盘有16G，而制作好后，系统盘只占了2.5G，而其他的空间（将近12G）都无发使用。我只能使用  dd if=/dev/zero of=/dev/sdb bs=4M 来重新给我整个U盘清零。

> 脚本实例 1. 用/dev/zero创建一个交换临时文件  

```shell
<span style="font-size:18px">#!/bin/bash  

# 创建一个交换文件，参数为创建的块数量（不带参数则为默认），一块为1024B（1K）  

ROOT_UID=0         # Root 用户的 $UID 是 0.  
E_WRONG_USER=65    # 不是 root?  

FILE=/swap  
BLOCKSIZE=1024  
MINBLOCKS=40  
SUCCESS=0  

# 这个脚本必须用root来运行,如果不是root作出提示并退出  
if [ "$UID" -ne "$ROOT_UID" ]  
then  
  echo; echo "You must be root to run this script."; echo  
  exit $E_WRONG_USER  
fi   


blocks=${1:-$MINBLOCKS}          # 如果命令行没有指定，则设置为默认的40块.  
# 上面这句等同如：  
# --------------------------------------------------  
# if [ -n "$1" ]  
# then  
#   blocks=$1  
# else  
#   blocks=$MINBLOCKS  
# fi  
# --------------------------------------------------  

if [ "$blocks" -lt $MINBLOCKS ]  
then  
  blocks=$MINBLOCKS              # 最少要有 40 个块长，如果带入参数比40小，将块数仍设置成40  
fi   

echo "Creating swap file of size $blocks blocks (KB)."  
dd if=/dev/zero of=$FILE bs=$BLOCKSIZE count=$blocks # 把零写入文件.  

mkswap $FILE $blocks             # 将此文件建为交换文件（或称交换分区）.  
swapon $FILE                     # 激活交换文件.  

echo "Swap file created and activated."  
exit $SUCCESS  
</span>  
```

>运行效果我们可以看到:

```shell
<span style="font-size:18px">long@Raring:/tmp$ vim testswap.sh  
long@Raring:/tmp$ chmod +x testswap.sh             
long@Raring:/tmp$ sudo ./testswap.sh             
[sudo] password for long:    
long@Raring:/tmp$ ./testswap.sh             

You must be root to run this script.  

long@Raring:/tmp$ sudo ./testswap.sh             
[sudo] password for long:       
Creating swap file of size 40 blocks (KB).  
记录了40+0 的读入  
记录了40+0 的写出  
40960字节(41 kB)已复制，0.000904021 秒，45.3 MB/秒  
正在设置交换空间版本 1，大小 = 36 KiB  
无标签， UUID=3e59eddf-098f-454d-9507-aba55f434a8c  
Swap file created and activated.  
</span>  
```
- 参考文章  
 [Linux 下的两个特殊的文件 -- /dev/null 和 /dev/zero 简介及对比](http://blog.csdn.net/pi9nc/article/details/18257593)
