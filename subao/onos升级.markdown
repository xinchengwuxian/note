# onos 升级

### 编译打包方式
onos 不支持maven打包，新版本没有pom文件

### 安装编译工具

```shell
sudo apt-get install bazel
```

### 编译onos

```shell
设置环境变量：ONOS_ROOT
cd $ONOS_ROOT
bazel build onos

注：
- 由于网络问题，可能会编译失败，多编译几次就成功了，或者挂代理，也可以修改$ONOS_ROOT/tools/build/bazel/generate_workspace.bzl文件，将“https://repo1.maven.org/maven2”修改为“http://maven.aliyun.com/nexus/content/groups/public”
- 可以将自己下载好的文件放到http://192.168.0.8:9900/libs下面通过内网下载
```

### 导入的模块变更情况

- onos-api

| uranus                   | 1.14.1 -  2.2.4 |
| ------------------------ | --------------- |
| AprPaCriterion           | 无变更          |
| Criteria                 | 无变更          |
| DefaultTrafficSelector   | 无变更          |
| TrafficSelector          | 无变更          |
| ClusterMetadataEventTest | 无变更          |
| IntentServiceTest        | 无变更          |
| WallClockTimestampTest   | 无变更          |

- onos-providers-openflow-flow

| uranus              | 1.14.1 - 2.2.4 |
| ------------------- | -------------- |
| FlowModBuilder      | 无变更         |
| FlowModBuilderVer10 | 无变更         |
| FlowModBuilderVer13 | 无变更         |
| FlowMonBuilderVer15 | 无变更         |
| FlowEntryBuilder    | 无变更         |

- onos-protocols-netconf-api

| uranus                  | 1.14.1-2.2.4                |
| ----------------------- | --------------------------- |
| CallHomeSession         | 新加文件                    |
| CallHomeSessionDelegate | 新加文件                    |
| NetconfController       | 有新接口添加                |
| NetconfDevice           | 添加ismaster接口            |
| NetconfDeviceFactory    | 添加createNetconfDevice方法 |
| NetconfDeviceInfo       | 添加path字段                |
| NetconfDeviceConfig     | 2.2.3 有新加path字段        |
| NetconfSession          | 接口修改                    |
| NetconfSessionAdapter   | 无变更                      |

- onos-netconf-provider-device

| uranus                | 1.14.1 - 2.2.4 |
| --------------------- | -------------- |
| NetconfDeviceProvider | 变更较多       |

- onos-protocols-netconf-ctl

| uranus                  | 1.14.1 - 2.2.4   |
| ----------------------- | ---------------- |
| AiwanNetconfDevice      | 新加文件         |
| NetconfSessionNettyImpl | 新加文件         |
| DefaultNetconfDevice    | 有master相关变更 |
| NetconfControllerImpl   | 变更较大         |
| NetconfSessionMianImpl  | 变更较大         |
| NetconfStreamHandler    | 无变更           |
| NetconfStreamThread     | 有变更           |

### uranus升级流程

1. merge代码，从1.14.1到2.2.4版本没有变更过的文件，以我们修改后的版本为准，所以`onos-api`,`onos-providers-openflow-flow`两个模块不需要升级，合代码的时候以uranus的代码为准，其他模块根据diff工具进行merge

2. 修改uranus的pom文件，将依赖的版本从1.14.1变更为2.2.4，然后编译onos，解决编译问题

   遇到问题：

   - 2.2.4版本删除了`org.apache.felix.scr.annotations`的注解，使用了osgi原生的注解

   - osgi 组件在使用`maven-bundle-plugin`打包的时候默认不会处理有继承关系的组件依赖(eg: AiwanSwitchDriverLoader)，需要添加`maven-bundle-plugin`的配置

     ```xml
     <configuration>
         <instructions>
             <_dsannotations-options>inherit</_dsannotations-options>
         </instructions>
     </configuration>
     ```

   - 通过osgi原生注解标注的组件，如果有property，需要生成一个cfgdef的文件，该文件可以使用`onos-maven-plugin`插件使用如下配置生成

     ```xml
     <executions>
         <execution>
             <id>cfgdef</id>
             <phase>generate-resources</phase>
             <goals>
                 <goal>cfg</goal>
             </goals>
         </execution>
     </executions>
     ```

   - jdk版本从java8升级到java11，使用的gc不再支持CMS,所以编译脚本中关于CMS的jvm参数需要删除，不然会报虚拟机启动的错误(需要添加到release-notes)
   - java8使用的maven插件大多不能在java11使用，使用最新版本即可，其中`findbugs`插件不支持java11,该插件被删除

   - `import sun.security.x509.X500Name;` jdk11中这个包对外不导出，目前还不知道osgi怎样引用jdk11中的模块，所以现在对于通过x500Name取CommonName的流程由自己编码处理

     ```java
     //before
     X500Name subjectDN = (X500Name) ((X509Certificate) engine.getSession().getPeerCertificates()[0]).getSubjectDN();
     String commonName = subjectDN.getCommonName();
     
     //after
     Principal subjectDN = ((X509Certificate) engine.getSession().getPeerCertificates()[0]).getSubjectDN();
     String commonName = getCommonName(subjectDN.getName());
     
     private String getCommonName(String subjectDN) {
         String[] subjects = subjectDN.split(",");
         for (String subject: subjects) {
             String[] pair = subject.split("=");
             if (pair[0].equals(" CN") || pair[0].equals("CN")) {
                 return pair[1];
             }
         }
         return null;
     }
     ```

   - idea 导入2.2.4代码，需要安装bazel插件，可以方便查看代码