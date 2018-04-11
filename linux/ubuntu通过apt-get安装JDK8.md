### 安装JDK8
> ##### 安装python-software-properties
    $sudo apt-get install python-software-properties
    $sudo apt-get install software-properties-common
> ##### 首先添加ppa
    $sudo add-apt-repository ppa:webupd8team/java
> ##### 然后更新系统
    $sudo apt-get update
> ##### 最后开始安装
    $sudo apt-get install oracle-java8-installer
    $java -version
    java version "1.8.0_05"
    Java(TM) SE Runtime Environment (build 1.8.0_05-b13)
    Java HotSpot(TM) Server VM (build 25.5-b02, mixed mode)
> ##### java版本切换
    sudo update-java-alternatives -s java-8-oracle
