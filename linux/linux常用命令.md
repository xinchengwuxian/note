### linux常用命令
+ 查看系统的发布版本 `cat /etc/issue`
+ 循环执行某条命令 `watch -n 1 ls`
+ 循环执行多条命令 `watch -n 1 'ls;echo "test"'`
+ 打印输出到指定文件 `ls 1>test.txt`
+ 打印追加到指定文件 `ls >>test.txt`
+ sftp中执行的命令  
**操作server端：**  常用文件操作命令都可以执行，例如`ls`,`cd`  
**操作本地：** 需要在常用操作命令前面添加 **l** (小写的L) 即可，例如`lls`,`lcd`
<<<<<<< HEAD

+ 查看内存 `free -mh`
=======
>>>>>>> e9a91d381fafe7792015210182167b109754676e
