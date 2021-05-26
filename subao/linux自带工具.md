### perf 安装

```shell
apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`
```

### 使用命令

```shell
sudo perf record -F 99 -p 15703 -g --sleep 60
sudo perf report -i perf.data
```

