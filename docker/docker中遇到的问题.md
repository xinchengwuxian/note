# docker中遇到的问题

### 自定义容器启动脚本报错：exec user process caused "no such file or directory"

+ 报错信息
> standard_init_linux.go:178: exec user process caused "no such file or directory"  
standard_init_linux.go:178: exec user process caused "no such file or directory"  
standard_init_linux.go:178: exec user process caused "no such file or directory"  

+ 原因（注，在windows下编辑的文件在linux中用来制作镜像）
> 镜像的entrypoint设置的启动脚本格式是dos，在linux系统上用vi修改成unix格式即可

+ 解决方法
> `vi filename`  
`:set ff`  回车后看到当前文件的fileformat格式  
`:set ff=unix` 回车后输入:wq保存文件，重新build镜像即可。  