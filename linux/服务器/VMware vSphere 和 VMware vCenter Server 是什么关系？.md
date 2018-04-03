### VMware vSphere 和 VMware vCenter Server 是什么关系？
> VMware vSphere 是VMware 的一个虚拟化产品。它包括vCenter，ESX Server，ESXi Server等等。举个列子 如果你需要组建一套VMware 虚拟化平台，你有3台服务器，2台用于业务，1台用于管理，那么你这2台业务主机就可以安装ESX Server或者ESXi Server，然后安装 vCenter Server到剩下的一台管理主机上，你就可以通过vCenter Server 将2台ESX 主机或者ESXi主机管理起来。这样你才能使用VMware的一些很好的比如vMotion（在线迁移），DRS（分布式资源调度），HA（高可用性），FT（容错）等功能。如果配置分布式虚拟交换机也需要vCenter。请采纳。
