==========================
MongoDB开发最佳实践
==========================

连接到MongoDB
====================

- 关于驱动程序：总是选择与所用之MongoDB相兼容的驱动程序， 这可以很容易的从驱动兼容对照表中查找到
    - 如使用第三方框架， 则还需要考虑框架版本与驱动的兼容性；
- 关于连接独享MongoClient： 使用MongoClient对象连接到MongoDB实例时总是因该保证他单例， 并且在整个生命周期中都从他获取其他操作对象
- 关于连接字符串： 连接字符串中可以配置大部分连接选项， 建议总是在连接字符串中配置这些选项：
::

    # 连接到复制集
    mongodb:节点1，节点2，节点3.../database?[options]
    # 连接到分片集
    mongodb://mongos1, mongos2, mongos3.../database?[options]


常见连接字符串参数
--------------------------

- maxPoolSize
    - 连接池大小
- MaxWaitTime
    - 建议设置， 自动杀掉太慢的查询
- WriteConcern
    - 建议 majority 保证数据安全
- Read Concern
    - 对于数据一致性要求高的场景适当使用

连接字符串节点和地址
--------------------

- 无论对于复制集或分片集， 连接字符串中都应尽可能多地提供节点地址，建议全部列出；
    - 复制集利用这些地址可以更有效的发现集群成员
    - 分片集利用这些地址可以更有效的分散负载
- 连接字符串中尽可能使用与复制集内部配置相同的域名或IP


使用域名连接集群
------------------------

在配置集群时使用域名可以为集群变更时提供一层额外的保护，例如需要将集群整体迁移到新网段，直接修改域名解析即可。

另外，MongoDB提供mongodb+srv://协议可以提供额外一层的保护。该协议允许通过域名解析得到所有的mongos或节点地址，而不是写在连接字符串中


不要在mongos前面使用负载均衡
--------------------------------

基于前面提到的原因，驱动已经知晓在不同的mongos之间实现负载均衡，而复制集则需要根据节点的角色来选择发送请求的目标，如果在mongos或复制集上层部署负载均衡：

- 驱动会无法探测具体那个节点存活，从而无法完成自动故障恢复；
- 驱动会无法判断游标是在那个节点创建的，从而遍历游标时出错

结论：不要在mongos或复制集上层放置负载均衡器，让驱动处理负载均衡和自动故障恢复

游标使用
================

如果一个游标已经遍历完，则会自动关闭； 如果没有遍历完，则需要手动调用close()方法，否则该游标将在服务器上存活10分钟（默认值）后超时释放，造成不必要的资源浪费

但是，如果不能遍历完一个游标， 通常意味着查询条件太宽泛， 更因该考虑的问题是如何将条件收紧

关于查询及索引
===================

- 每一个查询都必须要有对应的索引
- 尽量使用覆盖索引 Covered Indexes （可以避免读数据文件）
- 使用 projection （投影 指定返回字段） 来减少返回到客户端的文档的内容

关于写入
==================

- 在update语句里只包括需要更新的字段
- 尽可能使用批量插入来提升写入性能
- 使用TTL自动过期日志类型的数据

关于文档结构
=================

- 防止使用太长的字段名（浪费空间）
- 防止使用太深的数组嵌套（超过2层操作比较复杂）
- 不适用中文，标点符号等非拉丁字母作为字段名

处理分页问题
==================================

避免使用count
----------------------

尽可能不要计算总页数， 特别是数据量大和查询条件不能完全命中索引时。

考虑以下场景：假设集合总共有1000W条数据， 在没有索引的情况下查询：
::

    db.coll.find({x:100}).limit(50)
    db.coll.count({x:100})

- 前者只需要遍历n条， 直到找到50条队伍 x = 100 的文档即可结束
- 后者需要遍历完1000W 条找到所有符合要求的文档才能得到结构

为了计算总页数而进行count() 往往是拖慢页面整体加载速度的原因

巧分页
------------------

避免使用skip/limit形式的分页， 特别是数据量大的时候

替代方案： 使用查询条件 + 唯一排序条件

例如：
::

    第一页：db.posts.find({}).sort({_id:1}).limit(20)
    第二页：db.posts.find({_id:{$gt:<第一页的最后一个_id>}}).sort({_id:1}).limit(20)
    第三页：db.posts.find({_id:{$gt:<第二页的最后一个_id>}}).sort({_id:1}).limit(20)
    ........

关于事务
==================

使用事务的原则：

- 无论何时， 事务的使用总是能避免则避免
- 模型设计先于事务， 尽可能用模型设计规避事务
- 不要使用过大的事务（尽量控制在1000个文档更新以内）
- 当必须使用事务是， 尽可能让涉及事务的文档分布在同一个分片上，这将有效的提高效率

