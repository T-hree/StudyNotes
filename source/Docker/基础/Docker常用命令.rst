========================
Docker常用命令
========================

帮助启动类命令
=======================

- 启动docker： systemctl start docker
- 停止docker： systemctl stop docker
- 重启docker： systemctl restart docker
- 查看docker状态： systemctl status docker
- 开机启动： systemctl enable docker
- 查看docker概要信息： docker info
- 查看docker总体帮助文档： docker --help
- 查看docker命令帮助文档： docker 命令 --help

镜像类命令
========================

docker images
----------------------

列出本地主机上的镜像

.. code-block:: shell

    xiaoyan@xiaoyan app % docker images
    REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
    getting-started          latest    9f9b0954e25d   21 hours ago   404MB
    docker/getting-started   latest    cb90f98fd791   4 weeks ago    28.8MB

各个参数说明：
    - REPOSITORY : 表示镜像的仓库源
    - TAG: 镜像的标签 版本号
    - IMAGE ID： 镜像ID
    - CREATED： 镜像创建时间
    - SIZE： 镜像大小

| 同一个仓库源可以有多个TAG版本， 代表这个仓库源的不同个版本， 我们使用`REPOSITORY:TAG`来定义不同的镜像
| 如果你不指定一个镜像的版本标签， 例如你使用 ubuntu， docker默认使用 ubuntu:latest 机箱

常用OPTIONS说明
^^^^^^^^^^^^^^^^^^^^^

- -a：列出本地所有的镜像（含历史映像层）
- -q: 只显示镜像ID

docker search
-----------------------

查找镜像

.. code-block:: shell

    xiaoyan@xiaoyan app %  docker search hello-world
    NAME                                       DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
    hello-world                                Hello World! (an example of minimal Dockeriz…   1730      [OK]
    kitematic/hello-world-nginx                A light-weight nginx container that demonstr…   151
    tutum/hello-world                          Image to test docker deployments. Has Apache…   88                   [OK]
    dockercloud/hello-world                    Hello World!                                    19                   [OK]
    crccheck/hello-world                       Hello World web server in under 2.5 MB          15                   [OK]

各个参数说明：
    - NAME : 镜像名称
    - DESCRIPTION: 镜像说明
    - STARS： 点赞数量
    - OFFICIAL： 是否官方认证
    - AUTOMATED： 是否是自动构建的

常用OPTIONS说明
^^^^^^^^^^^^^^^^^^^^^

- --limit: 只列出N个镜像， 默认25个
    - docker search --limit 5 redis

docker pull
-----------------------

下载镜像

`docker pull img:tag` or `docker pull img`

没有 tag 就是最新版  等价于  img:latest


docker system df
------------------------

查询镜像/容器/数据卷所占的空间

.. code-block:: shell

    xiaoyan@xiaoyan app % docker system df
    TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
    Images          2         1         427.4MB   404.2MB (94%)
    Containers      1         0         1.093kB   1.093kB (100%)
    Local Volumes   0         0         0B        0B
    Build Cache     17        0         95.23MB   95.23MB

各个参数说明：
    - TYPE : 统计类型
    - TOTAL: 总数
    - ACTIVE： 正在运行的数量
    - SIZE： 对应类型所占的大小
    - RECLAIMABLE： 正在运行的占总大小的百分百

docker rmi
-------------------------

删除镜像

- 删除单个：`docker rmi img` or `docker rmi img:tag` or `docker rmi img_id`
- 删除多个：`docker rmi img1 img2...`
- 删除全部：`docker rmi -f $(docker images -qa)`

常用OPTIONS说明
^^^^^^^^^^^^^^^^^^^^^

- -f: 强制删除（先删除运行中和停止的容器）

虚悬镜像？
-------------------------

仓库名、标签都是<none>的镜像， 俗称虚悬镜像 dangling image

.. code-block:: shell

    xiaoyan@xiaoyan app % docker images
    REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
    getting-started          latest    9f9b0954e25d   21 hours ago   404MB
    <none>                   <none>    cb90f98fd791   4 weeks ago    28.8MB


容器类命令
=========================

新建+启动容器
----------------------

`docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`

常用OPTIONS说明
^^^^^^^^^^^^^^^^^^^^^

- --name='容器名称'  为容器指定一个名称
- -d: 后台运行容器并返回容器id ， 也即启动守护式容器（后台运行）
- -i: 以交互模式预先容器， 通常与-t同时使用，
- -t: 为容器重新分配一个伪输入终端， 通常与-i同时使用
- -P: *随机*映射端口，
- -p: *指定*映射端口
    -

启动交互式容器（前台命令行）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`docker run -it ubuntu /bin/bash`

使用镜像 Ubuntu 以*交互模式* 启动一个容器， 在容器内执行/bin/bash 命令。

参数说明：
    - -i: 交互式操作
    - -t: tty终端
    - ubuntu: 镜像名称
    - /bin/bash: 放在镜像名后的是命令， 这里我们希望有个交互式shell，因此用的是/bin/bash.

后台式容器
^^^^^^^^^^^^^^^^^^^

使用镜像ubuntu以后台模式启动一个容器`docker run -d ubuntu`， 然后`docker ps -a` 进行查看 发现容易已经退出

原因： *Docker 容器后台运行， 就必须有一个前台进程* 容器运行的命令如果不是`一直挂起的命令（如top，tail), 就是会自动退出

这个是docker的机制问题， 所以，最佳的解决方案是：
::

    将你要运行的程序以前台进程的形式运行，
    常见就是命令行模式，
    表示还有交互操作




列出所有正在运行的容器
-------------------------------

`docker ps [OPTIONS]`

.. code-block:: shell

    [root@sanye ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS         PORTS     NAMES
    2f047eb3d4a5   ubuntu    "/bin/bash"       6 minutes ago   Up 6 minutes             zealous_albattani
    容器id          镜像名     启动时 执行的命令   创建时间          状态           端口映射    容器名称

常用OPTIONS说明
^^^^^^^^^^^^^^^^^^^^^

- -a: 列出当前所有正在运行的容器+ 历史上运行过的容器
- -l: 显示最近创建的容器
- -n: 显示最近n个创建的容器
- -q: 静默模式，只显示容器id


退出容器
-----------------------

- exit
    - exit退出， 容器停止
- ctrl+p+q
    - 容器不停止


启动已经停止的容器
--------------------------

`docker start 容器id或容器名`

重启，停止， 强制定制容器
-----------------------------

- 重启
    - `docker restart 容器id或者容器名`
- 停止
    - `docker stop 容器id或者容器名`
- 强制停止
    - `docker kill 容器id或者容器名`

删除已经停止的容器
---------------------------

`docker rm 容器id或者容器名`

常用OPTIONS说明
^^^^^^^^^^^^^^^^^^^^^

- -f: 强制删除

一次性删除多个容器实例
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- `docker rm -f $(docker ps -aq)`
- `docker ps -aq | xargs docker rm -f`


查看容器日志
-------------------

`docker logs 容器id或者容器名称`

查看容器内运行的进程
---------------------------

`docker top 容器id或者容器名称`

查看容器内部细节
--------------------------

`docker inspect 容器id或者容器名称`

进入正在运行的容器并以命令行交互
--------------------------------------------

- `docker exec -it 容器id或者容器名称 bashShell`
- `docker attach 容器id或者容器名称`

区别：
    - attach 直接进入容器启动命令的终端， 不会启动新的进程 用exit退出， 会导致容器的停止
    - exec 是在容器中打开新的终端， 并且可以启动新的进程，用exit退出，不会导致容器的停止

从容器内拷贝文件到主机中
---------------------------------

`docker cp 容器ID:容器内路径 主机路径`

::

    xiaoyan@xiaoyan Desktop % docker ps
    CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                    NAMES
    0a0a94ce1368   ubuntu    "/bin/bash"              14 minutes ago   Up 3 minutes                             vigorous_hamilton
    xiaoyan@xiaoyan Desktop % docker cp 0a0a94ce1368:/tmp/a.txt ./test.txt


导入和导出容器
-----------------------

export
^^^^^^^^^^^^^^^^^

导出容器的内容留作为一个tar归档文件[对应import命令]

import
^^^^^^^^^^^^^^^^^

从tar包中的内容创建一个新的文件系统再导入为镜像[对应export命令]


示例
^^^^^^^^^^^^^^^^^

- `docker export 容器ID > file.tar`
    - `docker export a1c9f766c202 > redis.tar`
- `cat file.tar | docker import - 镜像用户/镜像名:镜像版本号`
    - `cat redis.tar | docker import - test/redis:v1`



