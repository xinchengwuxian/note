### virtualenv创建虚拟python环境

```shell
virtualenv   --no-site-packages -p  /usr/bin/python3 venv
```

**说明：**（-p指定python的版本， --no-site-packages表示不安装第三方的python包到虚拟环境）

```shell
source ./bin/activate

deactivate
```
