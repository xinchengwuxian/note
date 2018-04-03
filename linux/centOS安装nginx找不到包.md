### centOS安装nginx找不到包
+ 原因
> nginx位于第三方的yum源里面，而不在centos官方yum源里面
+ 解决方法
> epel它是RHEL 的 Fedora 软件仓库，为 RHEL 及衍生发行版如 CentOS、Scientific Linux 等提供高质量软件包的项目。装上了 EPEL，就像在 Fedora 上一样，可以通过 yum install package-name，随意安装软件。
```shell
sudo yum install epel-release
yum update
yum install nginx
```
