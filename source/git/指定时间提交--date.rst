==============================
指定时间提交--date
==============================

我在之前修改了一个文件，但是没有commit，现在我想要commit，日期为那天的日期

git 修改日期的方法很简单，因为有一个命令\ ``--date`` 可以设置 git
提交时间

默认的 git
的提交时间会受到系统的时间的影响，如果想要系统的时间不会影响到 git
的提交时间，请使用本文的方式，自己指定提交的时间

使用git自定义时间的提交格式：

.. code:: csharp

   git commit --date="月 日 时间 年 +0800" -am "提交"

如果我要把日期修改为 2016.5.7 那么我可以使用下面代码

.. code:: csharp

   git commit --date="May 7 9:05:20 2016 +0800" -am "提交"

其中我希望大家知道的：

各个月份的缩写，不然每次都需要去百度一下

.. code:: csharp

   January, Jan.
   February, Feb.
   March, Mar.
   April, Apr.
   May, May.
   June, Jun.
   July, Jul.
   August, Aug.
   September, Sep.
   October, Oct.
   November, Nov.
   December, Dec.

当然，如果你想写为程序，那么我还可以送你一点代码

.. code:: csharp

               new List<string>()
               {
                   "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug",
                   "Sep","Oct","Nov","Dec"
               };

如果修改过程需要修改上一次提交的日期，可以添加 ``--amend``
的参数，如果要修改不是上一次的提交，而是很久的提交，我暂时没找到如何做，如果你知道怎么做，请告诉我
