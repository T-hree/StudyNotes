# GitLabRunner 安装注册



## 通过Docker安装

```shell
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```



## Runner注册

- GItLabRunner类型
  -  shared ：运行整个平台项目的作业(gitlab)
  -  group : 运行特定group下的所有项目的作业(group)
  -  specific : 运行指定的项目作业(project)
  -  locked : 无法运行项目作业
  -  paused : 不会运行作业



### 获取 runner token 的三个位置

shared 整个平台的:

![image-20220823102246812](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220823102246812.png)



group 项目组的：

![image-20220823102344168](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220823102344168.png)



Specific 单个项目的：

![image-20220823102438483](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220823102438483.png)



### 交互式注册

```shell
gitlab-runner register
```

![image-20220823103133923](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220823103133923.png)



### 非交互式(命令行注册)

#### shell执行器 参数

```shell
sudo gitlab-runner register --non-interactive --url "http://1.117.65.97:8080/" --registration-token "tJkVLAXzoGaK-fi-9mpi" --executor "shell" --description "global_test" --tag-list "deploy" --run-untagged="true" --locked="false"  --access-level="not_protected"  
  
 # 非交互运行
 # gitlab项目地址
 # token
 # 执行器
 # runner描述
 # 标签
 # 运行 没有指定tag的任务
 # 是否默认为被锁状态
 # 访问级别
```



![image-20220823112515875](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220823112515875.png)







 