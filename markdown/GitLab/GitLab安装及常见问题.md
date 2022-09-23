# GitLab安装及常见问题

## 通过Docker 安装

```shell
export GITLAB_HOME=$HOME/gitlab

sudo docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 22:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  --shm-size 256m \
  gitlab/gitlab-ee:latest
  
# hostname 为gitlab clone pull  push 等操作的地址
# 宿主机至少为 2核4G 否则 在部署时  会因为内存空间不足而出问题
```

## 安装部署成功后获取 默认root用户密码

```shell
sudo docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```


## 遇到的一些问题

### gitlab 项目clone pull push 的地址 问题

当我们在启动gitlab时 如果没有指定 hostname 那么他会随机生成一段序列码 作为你的 项目操作的 id(域名)

![image-20220823100153397](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220823100153397.png)

git@ 后面所跟的就是 我们在部署gitlab 时 指定的 hostname参数

将他改为自己的ip地址 即可



### ssh 和http 端口的问题



当我们部署gitlab时  可能默认的22 端口 和 80端口 都被 占用了  

这个时候 就需要去修改 gitlab仓库 这两种  请求方法的 默认端口了

#### gitlab修改ssh端口配置

修改了`/etc/gitlab/gitlab.rb`中的`gitlab_rails['gitlab_shell_ssh_port']= 23456`
[![img](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/1580998-20200508170553071-900150854-20220823100740872.png)](https://img2020.cnblogs.com/blog/1580998/202005/1580998-20200508170553071-900150854.png)

```undefined
sudo gitlab-ctl reconfigure
sudo gitlab-ctl restart
```

[![img](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/1580998-20200508170721328-410837491-20220823100737334.png)](https://img2020.cnblogs.com/blog/1580998/202005/1580998-20200508170721328-410837491.png)

等`gitlab`重新启动完毕后,此时新建仓库会发现ssh 地址已经添加自定义端口
[![img](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/1580998-20200508171138385-861708171-20220823100733298.png)](https://img2020.cnblogs.com/blog/1580998/202005/1580998-20200508171138385-861708171.png)
这时在配置完`ssh秘钥`后，便可将代码推送到`gitlab`仓库
[![img](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/1580998-20200508171419837-1408660059-20220823100746686.png)](https://img2020.cnblogs.com/blog/1580998/202005/1580998-20200508171419837-1408660059.png)

HTTP端口同理





