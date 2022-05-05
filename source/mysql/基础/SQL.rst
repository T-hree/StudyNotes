===========
SQL通用语法
===========

.. code:: 

   1 sql 语句可以单行或者多行书写  以分号结尾
   2 sql语句可以使用空格 缩进来增强语句可读性
   3 mysql数据库的sql不区分大小写， 关键字建议使用大写
   4 注释：
   	单行注释： -- 或 #（mysql特有）
   	多行注释： /* */

SQL分类
=======

DDL
---

数据定义语言 用来定于数据库对象（数据库， 表， 字段）

数据库操作
~~~~~~~~~~

.. _查询-1:

查询
^^^^

1 查询所有数据库

.. code:: mysql

   	show databases; 

2 查询当前数据库

.. code:: mysql

   	select database();

.. _创建-1:

创建
^^^^

.. code:: mysql

   Create database [if not exists] 数据库名 [default charset 字符集] [collate 排序规则]；
   ps: exists 是否存在
       字符集推荐使用 utf8mb4 (utf8的汉字占3个字节， 但是有些字符占4个字节，utf8mb4就支持4个字节)

.. _删除-1:

删除
^^^^

.. code:: mysql

   drop database [if exists] 数据库名;

使用
^^^^

.. code:: mysql

   use 数据库名;

表操作
~~~~~~

.. _查询-2:

查询
^^^^

1 查询所有表

.. code:: mysql

   show tables;

2 查询表结构

.. code:: mysql

   desc 表名;

3 查询指定表的建表语句

.. code:: mysql

   show create table 表名;

.. _创建-2:

创建
^^^^

.. code:: mysql

   create tabel 表名（
   	字段1 字段1类型[comment 字段1注释],
   	字段2 字段2类型[comment 字段2注释],
   	字段3 字段3类型[comment 字段3注释],
   	......
   	字段n 字段n类型[comment 字段n注释]
   )[comment 表注释];
   ps: [...]为可选参数, 最后一个字段没有 , 
   		UNSIGNED 指定数值类型的字段无符号

数据类型
^^^^^^^^

主要分为三类：

数值类型， 字符串类型， 日期时间类型

修改
^^^^

1 添加字段

.. code:: mysql

   alter table 表名 add 字段名 类型(长度) [comment 注释] [约束];

2 修改字段

.. code:: mysql

   修改数据类型
   	alter table 表名 modify 字段名 新数据类型(长度);
   修改字段名和字段类型
   	alter table 表名 change 旧字段名 新字段名 类型(长度) [comment 注释] [约束];

3 删除字段

.. code:: mysql

   alter table 表名 drop 字段名;

4 修改表名

.. code:: mysql

   alter table 表名 rename to 新表名;

.. _删除-2:

删除
^^^^

1 删除表

.. code:: mysql

   drop table [if exists] 表名;

2 删除指定表 并重新创建该表

.. code:: mysql

   truncate table 表名; 
   可以看做清空表

DML
---

数据操作语言 用来对数据表中的数据进行增删改查

增加数据 insert
~~~~~~~~~~~~~~~

.. code:: mysql

   1 给指定的字段添加数据
     insert into 表名(字段1, 字段2,...) values (值1, 值2,...);
   2 给全部字段添加数据
     insert into 表名 values(值1, 值2,....);
   3 批量添加数据
   	insert into 表名(字段1, 字段2,...) values (值1, 值2,...), (值1, 值2,...),(值1, 值2,...),...(值1, 值2,...);
   	insert into 表名 
     (值1, 值2,...), (值1, 值2,...),....(值1, 值2,...);
   ps: 插入数据时， 指定的字段顺序与值的顺序是一一对应的
   		字符串和日期类型数据因该包含在引号中，
   		插入的数据大小，因该在字段的规定范围内。

修改数据 update
~~~~~~~~~~~~~~~

.. code:: mysql

   update 表名 ser 字段1=值1, 字段2=值2, .... [where 条件];

删除数据 delete
~~~~~~~~~~~~~~~

.. code:: mysql

   delete from 表名 [where 条件]
   delete 语句的条件可以有， 也可以没有， 如果没有条件， 则会删除整张表的所有数据
   delete 语句不能删除某一个字段的值， 如果需要（使用updata set xx=null）

DQL
---

数据查询语言， 用来查询数据库中的表记录

.. code:: mysql

   select 字段列表 from 表名列表 where 条件列表 group by 分组字段列表 having 分组后得条件列表 order by 排序字段列表 limit 分页参数

基本查询
~~~~~~~~

.. code:: sql

   # 1 查询多个字段
     select 字段1, 字段2, 字段3,... from 表名;
     select * from 表名;
   # 2 设置别名
   	select 字段1 [as 别名1], 字段2 [as 别名2],.... from 表名;
   # 3 去除重复记录
   	select distinct 字段列表 from 表名;

条件查询
~~~~~~~~

.. code:: sql

   select 字段列表 from 表名 where 条件列表;
   比较运算符：
   	> , >= , < , <= , = , <>或!= , between ... and ...(在某个范围内， 含最大最小值) , in(...) 在in之后的列表中
   	like 占位符 , is null 是null
   逻辑运算符:
   	and 或 &&
   	or 或 || 
   	not 或 !

聚合查询
~~~~~~~~

介绍
^^^^

将一列数据作为一个整体， 进行纵向计算。

===== ========
函数  功能
===== ========
count 统计数据
max   最大值
min   最小值
avg   平均值
sum   求和
===== ========

.. _语法-1:

语法
^^^^

.. code:: sql

   select 聚合函数(字段列表) from 表名;

注意：null值不参与所有聚合函数运算

分组查询
~~~~~~~~

.. _语法-2:

语法
^^^^

.. code:: sql

   select 字段列表 from 表名 [where 条件] group by 分组字段名[having 分组后过滤条件];

where 和 having 区别
^^^^^^^^^^^^^^^^^^^^

1 执行时机不同： where是分组之前进行过滤， 不满足where条件，
不参与分组， 而having是分组之后对结果进行过滤。

2 判断条件不同： where 不能对聚合函数进行判断， 而 having可以

注意：

1 执行顺序： where > 聚合函数 > having

2 分组之后， 查询的字段一般为聚合函数和分组字段， 查询其他字段无任何意义

排序查询
~~~~~~~~

.. _语法-3:

语法
^^^^

.. code:: sql

   select 字段列表 from order by 字段1 排序方式1, 字段2 排序方式2,.....;
   # 排序方式
   # ASC 升序 （默认）
   # DESC 降序 
   # 注意： 如果是多字段排序， 当第一个字段相同时， 才会根据第二个字段进行排序

分页查询
~~~~~~~~

.. _语法-4:

语法
^^^^

.. code:: sql

   select 字段列表 from 表名 limit 起始索引,查询记录数; 

DQL执行顺序
~~~~~~~~~~~

from > where > group by > having > select > order by > limit

DCL
---

数据控制语言， 用来创建数据库用户， 控制数据库的访问权限

管理用户
~~~~~~~~

查询用户
^^^^^^^^

.. code:: sql

   use mysql
   select * from user;

创建用户
^^^^^^^^

.. code:: sql

   create user 'user'@'host' identified by 'password';

修改用户密码
^^^^^^^^^^^^

.. code:: sql

   alter user 'user'@'host' identified with mysql_native_password by 'new password';

删除用户
^^^^^^^^

.. code:: sql

   drop user 'user'@'host';

权限控制
~~~~~~~~

常用权限如下：

=================== ==================
权限                说明
=================== ==================
all, all privileges 所有权限
select              查询数据
insert              插入数据
update              修改数据
delete              删除数据
alter               修改表
drop                删除数据库/表/视图
create              创建数据库/表
=================== ==================

查询权限
^^^^^^^^

.. code:: sql

   show grants for 'user'@'host';

授予权限
^^^^^^^^

.. code:: sql

   grant 权限列表 on 数据库名.表名 to 'user'@'host';

撤销权限
^^^^^^^^

.. code:: sql

   revoke 权限列表 on 数据库名.表名 from 'user'@'host';
