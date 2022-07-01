====================================
Docker-compose容器编排
====================================


是什么
=================

Docker-Compose是Docker官方的开源项目， 负责实现对Docker容器集群的快速编排

Compose是Docker公司推出的一个工具软件， 可以管理多个Docker容器组成一个应用。
你需要定义一个YAML格式的配置文件docker-compose.yml. 写好多个容器之间的调用关系
然后， 只需要一个命令，就能同时启动容器

能干嘛
=================

docker建议我们每一个容器中只运行一个服务， 因为docker容器本身占用资源极少， 所以最好是将每个服务单独的分割开来
但是这样我们有面临一个问题，  如果我们需要同时部署多个服务，难道要每个服务单独写Dockerfile然后在构建镜像，构建容器
这样累都累死了， 所以docker官方给我们提供了docker-compose多服务部署的工具

如果要实现一个Web微服务项目， 出了Web服务容器本身， 往往还需要再加上后端  数据库， redis， nginx 等等

Compose允许用户通过一个单独的docker-compose.yml模板文件(YAML格式） 来定义一组相关联的应用容器为一个项目

可以很容易的 用一个配置文件定义一个多容器的应用， 然后使用一条指令安装这个应用的所有依赖
完成构建， Docker-Compose 解决了容器与容器之间如何管理编排的问题。

Compose 核心概念
==========================

一文件
---------------

*docker-compose.yml*

两要素
------------------

服务：
    一个个应用容器实例，如果web微服务，mysql，redis， nginx
工程：
    由一组关联的应用容器组成一个*完整业务员单元*， 在docker-compose.yml文件中定义



Compose使用的三个步骤
===============================

1. 编写Dockerfile定义各个微服务应用并构建出对应的镜像文件
2. 使用docker-compose.yml 定义一个完整业务单元，安排好整体应用中的各个容器服务
3. 最后执行docker-compose up 命令 来启动并运行整个应用程序， 完成一键部署上线


Compose常用命令
=================================

::

    docker-compose up       # 启动所有docker-compose服务
    docker-compose up -d    # 启动所有docker-compose服务并后台运行
    docker-compose down     # 停止并删除容器，网络，卷，镜像
    docker-compose exec 服务id    # 进入容器实例内部
    docker-compose ps       # 展示当前docker-compose编排过的运行的所有容器
    docker-compose top      # 展示当前docker-compose 编排过的容器进程

    docker-compose logs 服务id    # 查看容器输出日志
    docker-compose config # 检查配置
    docker-compose config -q # 检查配置， 有问题才输出
    docker-compose restart # 重启服务
    docker-compose start # 启动服务
    docker-compose stop # 停止服务


docker-compose 示例
===========================

::

    version: "3"
    services:
      DjangoServer:
        image: django_test
    #     build:
    #       context: ./
    #       dockerfile: Dockerfile
        container_name: django_test
        ports:
          - "8000:8000"
        networks:
          - django_test
        depends_on:
          - redis
          - mysql

      redis:
        image: redis
        container_name: django_test_redis
        ports:
          - "6379:6379"
        volumes:
          - ./redis/redis.conf:/etc/redis/redis.conf
          - ./redis/data:/data
        networks:
          - django_test
        command: redis-server /etc/redis/redis.conf

      mysql:
        image: mysql
        container_name: django_test_mysql
        environment:
          MYSQL_ROOT_PASSWORD: '1234'
          MYSQL_ALLOW_EMPTY_PASSWORD: 'no'
          MYSQL_DATABASE: 'django_test'
        ports:
          - "3306:3306"
        volumes:
          - ./mysql/db:/var/lib/mysql
        networks:
          - django_test
    networks:
      django_test:
    # 注意 redis 需要 更改配置文件的bind_ip
    # mysql 需要设置默认的root密码
