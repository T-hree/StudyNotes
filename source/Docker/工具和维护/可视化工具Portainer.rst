==================================
可视化工具Portainer
==================================


安装
===================

访问 `官网 <https://www.portainer.io/>`_ , 可以搜索更多
访问 `官网文档 <https://docs.portainer.io/start/install/server/docker/linux>`_ , 可以搜索更多

::

    docker volume create portainer_data
    docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
    https://localhost:9443

    --restart=always  # 如果docker重启 容器也会跟着docker重启
