### linux中执行sudo
> 修改/etc下面的sudoers文件，将其中的Defaults    env_reset 修改为
  Defaults    ！env_reset ,然后在普通用户的 .bashrc中添加
  alias sudo='sudo env PATH=$PATH' 就可以直接使用sudo执行命令
  （例如我要在普通用户下面监听67端口是需要root权限的，但是我又不想
  切换到root用户下面，因为可能存在在root权限下对系统的威胁，这个时候就可
  以通过这个方法来在普通用户下通过sudo执行命令，实现端口的监听）  

> **注：**linux在监听1024以下的端口的时候需要root权限才行
