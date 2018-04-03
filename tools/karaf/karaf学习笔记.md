### karaf一些基本知识  
> 1.Pressing Ctrl + D will shut down Karaf when you are on the shell; however, if you are connected remotely (using SSH), this action will just log off the SSH session, it won't shut down Karaf.  

> 2.Karaf's interactive shell provides a powerful interface to administer the container runtime; however, most users require their application server to operate on a remote host—this is where Karaf's built in SSH daemon steps in. By default, when a Karaf instance is started, it will bind upon port 8101 a SSHD service, which can be connected to using the provided Karaf client utility (in the Karaf's bin folder)—its embedded SSH client, or a third-party SSH client. The default credentials are username karaf, password karaf. The default port can be edited in etc/org.apache.karaf.shell. cfg, and the credentials edited in etc/users.properties. Once connected to an instance, you may type exit to log out of the system.  

> 3.bin# client [–a port] [–h hostname] [–u username] [–p password] [–r retries] [–d retry-delay] [commands]  

> 4.To deploy the project into your Karaf container, issue the following command:
karaf@root> install –s mvn:com.your.organization/com.your.organization. command/1.0.0-SNAPSHOT

> 5.webconsole：https://ipaddress:8181/system/console
