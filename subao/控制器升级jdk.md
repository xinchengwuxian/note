下载jdk文件：`http://192.168.0.8:9900/libs/OpenJDK11U-jdk_x64_linux_hotspot_11.0.8_10.tar.gz`

```shell
#!/bin/sh
set -ex

JDK_FILE=$1
rm -rf /opt/aiwan/jdk11
mkdir -p /opt/aiwan/jdk11/
tar -zxvf $JDK_FILE --strip-components 1 -C /opt/aiwan/jdk11
echo "export JAVA_HOME=/opt/aiwan/jdk11" >> /etc/profile
echo "export JRE_HOME=\${JAVA_HOME}/jre" >> /etc/profile
echo "export CLASSPATH=.:\${JAVA_HOME}/lib:\${JRE_HOME}/lib" >> /etc/profile
echo "export PATH=\${JAVA_HOME}/bin:\$PATH" >> /etc/profile
source /etc/profile
```



