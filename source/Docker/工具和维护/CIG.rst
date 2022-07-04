=======================================
CAdvisor + InfluxDB + Granfana
=======================================

原生命令
========================

docker stats

通过docker stats命令可以很方便的看到当前宿主机上所有容器的CPU， 内存以及网络流量等数据

但是 docker stats统计结果只能是当前宿主机的全部容器， 数据资料是实时的， 没有地方存储、没有监控指标过线预警等功能

监控三剑客
====================

CAdvisor监控收集
------------------------

CAdvisor是一个容器资源监控工具，包括容器的内存，CPU，网络IO，磁盘IO等监控， 同时提供了一个WEB页面用于查看容器的实时运行状态。
CAdvisor默认存储2分钟的数据，而且只是针对单物理机。不过，CAdvisor提供了很多数据继承接口， 支持InfluxDB，Redis，Kafka等集成
可以加上对应配置将监控数据发往这些数据库存储起来

主要功能：
    - 展示Host和容器两个层次的监控数据
    - 展示历史变化数据


InfluxDB存储数据
----------------------------

InfluxDB是Go语言编写的一个开源分布式时序、事件和指标数据库， 无需外部依赖

CAdvisor默认只在本机保存最近2分钟的数据， 为了持久化存储数据和统一收集展示监控数据，
需要将数据存储到InfluxDB中。InfluxDB是一个时序数据库，专门用于存储时序相关数据
很适合CAdvisor的数据， 而且CAdvisor本身已经提供了Influx的集成方法， 丰启动容器时指定配置即可。

主要功能：
    - 基于时间序列， 支持与时间有关的相关函数
    - 可度量性， 你可以实时对大量数据进行计算
    - 基于时间， 他支持任意的时间数据


Granfana展示图表
-----------------------------

Granfana是一个开源的数据监控分析可视化平台， 支持多种数据源配置（支持的数据源包括 InfluxDB，MySQL，Graphite等）
和丰富的插件及模板功能，支持图表权限控制和报警

主要特殊：
    - 灵活丰富的图形化选项
    - 可以混合多种风格
    - 支持多个数据源

通过compose一键部署
=======================

::

    version: "3"

    volumes:
      grafana_data: {}

    services:
      influxdb:
        image: tutum/influxdb
        restart:  always
        environment:
          - PRE_CREATE_DB=cadvisor
        ports:
          - "8083:8083"
          - "8086:8086"
        volumes:
          - ./data/influxdb:/data

      cadvisor:
        image: google/cadvisor
        links:
          - influxdb:influxsrv
        command: -storage_driver=influxdb -storage_driver_db=cadvisor -storage_driver_host=influxsrv:8086
        restart: always
        ports:
          - "8080:8080"
        volumes:
          - /:/rootfs:ro
          - /var/run:/var/run:ro
          - /sys:/sys:ro
          - /var/lib/docker:/var/lib/docker:ro

      grafana:
        user: "104"
        image: grafana/grafana
        restart: always
        links:
          - influxdb:influxsrv
        ports:
          - "3000:3000"
        volumes:
          - grafana_data:/var/lib/grafana
        environment:
          - HTTP_USER=xiaoyan
          - HTTP_PASS=nolover..
          - INFLUXDB_HOST=influxsrv
          - INFLUXDB_PORT=8086
          - INFLUXDB_NAME=cadvisor
          - INFLUXDB_USER=xiaoyan
          - INFLUXDB_PASS=nolover..

