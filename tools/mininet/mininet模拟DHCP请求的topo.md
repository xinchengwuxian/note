### mininet模拟DHCP请求的topo
    以下代码是通过mininet创建的一个topo，其中switch是直接于控制器连接的，h1和h2是
    通过switch的openflow通道向控制器发送DHCP请求，实现ip请求并且建立openflow连接

```python
#!/usr/bin/env python
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info

def ToRealnet():

    c0 = RemoteController( 'c0', ip='10.190.23.112', port=6653 )  
    net = Mininet( topo=None, build=False)

    info( '*** Adding controller\n' )
    net.addController(c0)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='0.0.0.0')
    h2 = net.addHost('h2', ip='0.0.0.0')

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info( '*** Starting network\n')
    net.start()
    os.popen('ovs-vsctl add-port s1 eth0')       
    h1.cmdPrint('dhclient '+h1.defaultIntf().name)      
    h2.cmdPrint('dhclient '+h2.defaultIntf().name)      
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    ToRealnet()
```
