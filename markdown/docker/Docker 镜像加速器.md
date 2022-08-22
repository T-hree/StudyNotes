# Docker 镜像加速器

## Ubuntu14.04、Debian7Wheezy

对于使用 upstart 的系统而言，编辑 /etc/default/docker 文件，在其中的 DOCKER_OPTS 中配置加速器地址：

```
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
```

重新启动服务:

```shell
$ sudo service docker restart
```

## Ubuntu16.04+、Debian8+、CentOS7

对于使用 systemd 的系统，请在 /etc/docker/daemon.json 中写入如下内容（如果文件不存在请新建该文件）：

```json
{"registry-mirrors":["https://reg-mirror.qiniu.com/"]}
```

之后重新启动服务：

```shell
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```



## Windows 10 or 11

对于使用 Windows 10 的系统，在系统右下角托盘 Docker 图标内右键菜单选择 Settings，打开配置窗口后左侧导航菜单选择 Daemon。在 Registrymirrors 一栏中填写加速器地址 **https://docker.mirrors.ustc.edu.cn/** ，之后点击 Apply 保存后 Docker 就会重启并应用配置的镜像地址了。

![img](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/38507F68-E30F-4CCA-AE9D-9E9EEF60EC83.jpg?token=AQBJNL6DTJHGMQDULOPUUKTC42LAI)

## Mac OS X

对于使用 Mac OS X 的用户，在任务栏点击 Docker for mac 应用图标-> Perferences...-> Daemon-> Registrymirrors。在列表中填写加速器地址 **https://reg-mirror.qiniu.com** 。修改完成之后，点击 Apply&Restart 按钮，Docker 就会重启并应用配置的镜像地址了。

![img](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/D26C96AF-8EFF-46E5-8618-4C67E72ACBAF.jpg?token=AQBJNL5QY7IOEYCKZAG5CXDC42LAE)

## 检查加速器是否生效

检查加速器是否生效配置加速器之后，如果拉取镜像仍然十分缓慢，请手动检查加速器配置是否生效，在命令行执行 **docker info**，如果从结果中看到了如下内容，说明配置成功。

```
$ docker info
Registry Mirrors:
    https://reg-mirror.qiniu.com
```



## 镜像加速器地址

```json
{
  "registry-mirrors": [
    "https://6txzqw99.mirror.aliyuncs.com", 
    "https://hub-mirror.c.163.com/",
    "https://reg-mirror.qiniu.com",
    "https://docker.mirrors.ustc.edu.cn/",
    "https://mirror.baidubce.com"
  ]
}

```

