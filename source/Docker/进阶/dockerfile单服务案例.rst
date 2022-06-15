===========================
dockerfile单服务案例
===========================

在本地编写好需要部署的服务
===================================

这里那简单的flask来作为示例:
::

    import uuid

    from flask import Flask
    class Config(object):
        HOST = "0.0.0.0"
        PORT = 5002


    app = Flask(__name__)
    app.config.from_object(Config)


    @app.route('/')
    def hello_world():
        return 'hello_world'


    @app.route('/docker')
    def docker():
        return f'docker{app.config["PORT"]}， {uuid.uuid1().hex}'


    if __name__ == '__main__':
        app.run(host=app.config["HOST"],port=app.config["PORT"])

编写Dockerfile文件
===========================

这里用python3.8为基础镜像:
::

    # 基础镜像
    FROM python:3.8
    # 设置编译时的环境变量
    ENV WORK_DIR /home/docker
    # 在build时执行的 shell 指令
    RUN pip install flask
    # 将刚才写好的项目文件夹 复制到镜像中
    ADD docker_test /home/docker
    # 设置工作目录  就是 进入容器时的默认路径
    WORKDIR $WORK_DIR
    # 暴露的端口
    EXPOSE 5002
    # docker run 时 执行的命令
    ENTRYPOINT ["python", "app.py"]

进行编译 `docker build -t 镜像名:标签 .` ：
::

    xiaoyan@xiaoyan pythonProject % docker build -t test .
    [+] Building 0.3s (9/9) FINISHED
     => [internal] load build definition from Dockerfile                                                                                                              0.0s
     => => transferring dockerfile: 37B                                                                                                                               0.0s
     => [internal] load .dockerignore                                                                                                                                 0.0s
     => => transferring context: 2B                                                                                                                                   0.0s
     => [internal] load metadata for docker.io/library/python:3.8                                                                                                     0.0s
     => [1/4] FROM docker.io/library/python:3.8                                                                                                                       0.0s
     => [internal] load build context                                                                                                                                 0.0s
     => => transferring context: 5.51kB                                                                                                                               0.0s
     => CACHED [2/4] RUN pip install flask                                                                                                                            0.0s
     => [3/4] ADD docker_test /home/docker                                                                                                                            0.0s
     => [4/4] WORKDIR /home/docker                                                                                                                                    0.0s
     => exporting to image                                                                                                                                            0.0s
     => => exporting layers                                                                                                                                           0.0s
     => => writing image sha256:02d38c5c4ab9f5fbe196c094b5c6d8ba6c7a8a330bb2a84bea9fe6878a9f7e33                                                                      0.0s
     => => naming to docker.io/library/test

编译成功后查看镜像并测试
=============================

`docker images` :
::

    xiaoyan@xiaoyan pythonProject % docker images
    REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
    test         latest    02d38c5c4ab9   5 seconds ago   920MB

`docker run -dp 5000:5002 test ` ：
::

    xiaoyan@xiaoyan pythonProject % docker run -dp 5000:5002 test
    decc8fa2ff56a181b225c6a35923696408c48d6df77edb3bee9d0af748142997

    xiaoyan@xiaoyan pythonProject % docker ps
    CONTAINER ID   IMAGE     COMMAND           CREATED         STATUS         PORTS                    NAMES
    decc8fa2ff56   test      "python app.py"   7 minutes ago   Up 7 minutes   0.0.0.0:5000->5002/tcp   wizardly_pascal

在本地浏览器输入 127.0.0.1:5000 访问成功