### maven中snapshot和release的作用和区别
> maven中的仓库分为两种，snapshot快照仓库和release发布仓库。snapshot快照仓库用于保存开发过程中的不稳定版本，release正式仓库则是用来保存稳定的发行版本。定义一个组件/模块为快照版本，只需要在pom文件中在该模块的版本号后加上-SNAPSHOT即可(注意这里必须是大写).maven2会根据模块的版本号(pom文件中的version)中是否带有-SNAPSHOT来判断是快照版本还是正式版本。如果是快照版本，那么在mvn deploy时会自动发布到快照版本库中，而使用快照版本的模块，在不更改版本号的情况下，直接编译打包时，maven会自动从镜像服务器上下载最新的快照版本。如果是正式发布版本，那么在mvn deploy时会自动发布到正式版本库中，而使用正式版本的模块，在不更改版本号的情况下，编译打包时如果本地已经存在该版本的模块则不会主动去镜像服务器上下载。

### maven打包上传到私服

**注：** 以下使用的仓库地址和用户名密码为公司内私服的实际地址和用户名密码。


    搭建好私服后，需要在~/.m2/settings.xml中配置私服仓库用户名密码，在工程  
    的pom.xml中配置仓库地址

+ ~/.m2/settings.xml配置修改
```xml
<servers>
      <server>
          <id>nexus-snapshot</id>
          <username>admin</username>
          <password>admin123</password>
      </server>
      <server>
          <id>nexus-release</id>
          <username>admin</username>
          <password>admin123</password>
      </server>
  </servers>
```
+ 工程pom.xml中
```xml
<distributionManagement>
  <!-- 注: distributionManagement标签中的id要与servers中的id对应-->
        <snapshotRepository>
            <id>nexus-snapshot</id>
            <name>Snapshots</name>
            <url>http://10.190.23.246:8081/nexus/content/repositories/snapshots/</url>
        </snapshotRepository>
        <repository>
            <id>nexus-release</id>
            <name>Releases</name>
            <url>http://10.190.23.246:8081/nexus/content/repositories/releases/</url>
        </repository>
</distributionManagement>
```
+ 一般来说，我们上传都可以省略Test这一步，所以可以使用这个命令
```shell
mvn deploy -DskipTests
```

+ 也可以
```shell
mvn deploy -Dmaven.test.skip=true
```
-Dmaven.test.skip=true，既跳过测试代码编译，也跳过测试代码执行。而-DskipTests只跳过测试代码执行。

### 项目中使用snapshots版本的jar包  

+ 首先需要在pom.xml中配置如下的snapshots仓库
```xml
<repositories>
    <repository>
        <id>nexus-snapshot</id>
        <url>http://10.190.23.246:8081/nexus/content/repositories/snapshots/</url>
        <releases>
            <enabled>false</enabled>
        </releases>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
</repositories>
```
+  然后加入snapshots依赖  
```xml
<dependency>
    <groupId>com.test</groupId>
    <artifactId>deploy-test</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```


+ 参考文章：  
[maven打包上传到私服](http://blog.csdn.net/wangjun5159/article/details/58649523)  
[项目中使用snapshots版本的jar包](https://my.oschina.net/sub/blog/292172)
