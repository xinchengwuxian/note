# maven项目中常见问题
**注：** 文中的报错信息都是通过回忆编写的，差距不大但不一定完全正确（是报错信息可能不对，解决方法是没错的）
+ 模块中有使用到@component注解，需要配置maven-scr-plugin插件
+ 配置了maven-scr-plugin插件需要添加org.apache.felix.scr.annotation插件，不然编译报错
+ 编译的时候报unknow.version,unknow.artifact等，是.m2仓库中对应的pom文件有问题，可能是在没有网的时候下载的文件，可打开查看是否有问题
+ 编译出现opening jar is failed,是仓库中的jar包有问题，打不开，删除对应jar包即可
+ 在将onos作为项目的parent的时候，可能修改了自己项目的版本号后出现依赖的onos的bundle的版本号也出现变化，主要是因为parent中的artifact是onos，改为onos-dependency即可，因为onos的pom中将依赖的bundle的版本号写成了{projec.version}，所以修改自己项目的版本号会出现这种情况
+ onos项目启动报错请首先查看日志中的报错信息
+ 出现包找不到的问题，可以定位到具体的包，看这个包有没有加入到karaf容器中，即有没有feature中配置过该bundle，如果配置了，配置的feature有没有安装，或者有没有安装成功
+ 在查看scr:list的时候，有没有启动的组件可以查看这个组件依赖的其他组件是否启动正常，要是依赖的其他组件任何一个组件有问题，都会出现组件启动不成功的情况
+ 在组件服务的编写过程中注意不要出现循环依赖，这种循环依赖在编译的时候可能检测不出来，但是启动的时候循环依赖相关的所有组件都不能正常启动
+ 在编写命令行的时候，在resource中会有一个OSGI-INF.blueprint的包，注意这是两个文件夹，一个OSGI-INF,一个buleprint，不要命名成一个文件夹，不然在写命令行的时候会出现找不到命令的问题
