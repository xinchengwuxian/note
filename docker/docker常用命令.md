### docker常用命令
<<<<<<< HEAD
- **查看镜像：** `sudo docker images`
- **删除镜像：** `sudo docker rmi  +镜像`
- **查看启动的容器：** `sudo docker ps`
- **查看所有容器（包括启动的容器）：** `sudo docker ps -a`
- **删除容器：** `sudo docker rm +容器`
- **储存镜像到本地：** `sudo docker save +镜像 | gzip > 本地文件名.tar.gz`
- **加载本地镜像：** `sudo docker load -i +本地镜像文件`
- **添加数据卷：** `sudo docker run -d -P --name web -v /src/webapp:/opt/webapp training/webapp python app.py` (将本机的/src/webapp目录挂载到容器的/opt/webapp目录，主要注意参数 -v 是添加 数据卷的意思)
- **添加数据卷读写权限：** `sudo docker run -d -P --name web -v /src/webapp:/opt/webapp:ro training/webapp python app.py` (ro为只读，Dockerfile中不支持数据卷的挂载，因为不同操作系统的目录结构不同)
- **查看指定容器的信息：** `sudo docker inspect + 容器名`
- **进入指定容器：** `sudo doccker exec -it +容器id /bin/bash`
- **容器启动出错，查看出错信息：** `sudo docker logs + 容器id`
- **镜像只做命令：** `sudo docker build -t +镜像名称 . (当前目录下有Dockerfile和制作镜像所需要的其他文件)`
- **docker-compose命令：** `docker-compose up -d;docker-compose down`
- **将容器中的文件拷贝出来：** `sudo docker cp containerID:container_path host_path`
=======
- **查看镜像：**sudo docker images
- **删除镜像：**sudo docker rmi  +镜像
- **查看启动的容器：**sudo docker ps
- **查看所有容器（包括启动的容器）：**sudo docker ps -a
- **删除容器：**sudo docker rm +容器
- **储存镜像到本地：**sudo docker save +镜像 | gzip > 本地文件名.tar.gz
- **加载本地镜像：**sudo docker load -i +本地镜像文件
- **添加数据卷：**sudo docker run -d -P --name web -v /src/webapp:/opt/webapp training/webapp python app.py(将本机的/src/webapp目录挂载到容器的/opt/webapp目录，主要注意参数 -v 是添加 数据卷的意思)
- **添加数据卷读写权限：**sudo docker run -d -P --name web -v /src/webapp:/opt/webapp:ro training/webapp python app.py(ro为只读，Dockerfile中不支持数据卷的挂载，因为不同操作系统的目录结构不同)
- **查看指定容器的信息：**sudo docker inspect + 容器名
>>>>>>> e9a91d381fafe7792015210182167b109754676e
