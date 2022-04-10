==========================================
git撤销、还原、放弃本地文件修改
==========================================


今天在写代码的时候，修改了一些内容，忽然要切换分支，但是修改的不是很好，只能临时放弃，这时候又不知道修改了哪些内容了，接下来就需要git的一些骚操作了，下面来总结一下：

1. 未使用git add 缓存代码
=================================

- 使用 ``git checkout -- filepathname``，注意中间有--( 不要忘记中间的 “- -” ，不写就成了切换分支了！！):
::

    git checkout -- filepathname

- 放弃所有文件修改 ``git checkout .`` :
::

    git checkout .

- 此命令用来放弃掉所有还没有加入到缓存区（就是 git add 命令）的修改：内容修改与整个文件删除
- 不会删除掉刚新建的文件。因为刚新建的文件还没已有加入到 git 的管理系统中。所以对于git是未知的。自己手动删除就好了。

2. 已使用git add 缓存代码，未使用git commit
==================================================================

- 使用 ``git reset HEAD filepathname``:
::

    git reset HEAD filepathname

- 放弃所有文件修改 ``git reset HEAD``:
::

    git reset HEAD

- 此命令用来清除 git 对于文件修改的缓存。相当于撤销 git add 命令所在的工作。
- 使用本命令后，本地的修改并不会消失，而是回到了第一步1. 未使用git add 缓存代码，继续使用git checkout -- filepathname，就可以放弃本地修改


3.已经用 git commit 提交了代码
=================================
使用 ``git reset --hard HEAD^`` 来回退到上一次commit的状态:
::

    git reset --hard HEAD^

或者回退到任意版本 ``git reset --hard commitid``，使用 ``git log`` 命令查看git提交历史和commitid