循环打印线程名到文件

```shell
#!/bin/bash
filelist=`ls /proc/890/task/`
for file in $filelist
do 
 cat /proc/890/task/$file/comm
done
```

