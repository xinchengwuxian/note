### anaconda的使用

### MongoDB安裝
mongod 配置成服务
mongod --bind_ip 0.0.0.0 --logpath c:、 --logappend --dbpath .. --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install

### redis安装
sudo apt-get install redis-server

配置文件（/etc/redis/redis.conf）
bind 127.0.0.1 (需要注释，不然只能在本地访问，其他设备不能远程连接)

requirepass 后面是连接的密码 (启动redis的时候需要添加 -a + 后面的密码启动)

重启 sudo service redis restart

### MySql安装
sudo apt-get install mysql-server mysql-client
/etc/mysql/mysql.conf.d/mysql.dnf(mysql的配置文件)
bind-address(只能本地访问，注释之后可以远程访问)
重启服务sudo service mysql restart

### DataGrap 数据库管理工具
