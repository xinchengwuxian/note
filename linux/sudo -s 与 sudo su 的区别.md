### sudo -s 与 sudo su 的区别
    sudo -s 其实和sudo su -是一个意思，就是切换到root用户，但是使用的是当前用户的环境  
    变量，但是sudo su只是切换用户，将当前用户切换到root用户，对应的环境变量也是root用  
    户中的环境变量
