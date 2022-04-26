第13关 stash
============

   You've made some changes and want to work on them later. You should
   save them, but don't commit them.

   你修改了一个文件，但还没改完，这时你要保存它，而不是提交它。

设想这样的场景：你正为一个类文件写一个新方法，写到一半了但还没写完，这时来了一个紧急任务，需要修改这个类的另一个方法，然后提交。现在你面临的问题是，手头的活儿还没干完，就又来新活儿了，而且是处理同一个文件！好吧，让我们思考一下操作系统是怎么处理这种情况的：外部中断到来时，系统会挂起当前进程，然后处理中断事件，处理完中断事件以后再恢复之前挂起的进程。\ ``git stash``
命令就是类似这样的一种处理方式，它会把当前环境“藏”到一个临时区域，然后把工作环境恢复为最后一次提交的状态，这时你可以从刚才的工作状态跳出来在一个干净的工作环境处理紧急任务，之后再用
``git stash pop`` 命令恢复此前“藏”的工作环境。

相关命令如下：

.. code:: 

   $ git stash
   $ git stash list
   $ git stash pop

第1条命令把当前环境“藏”起来；第2条命令列出被“藏”的环境；第3条命令恢复被“藏”的环境。

第13关过关画面如下：\ |image1|

第14关 rename
=============

   We have a file called 'oldfile.txt'. We want to rename it to
   'newfile.txt' and stage this change.

   有一个名为 'oldfile.txt' 的文件，要把它改名为
   'newfile.txt'，并且把这个改动记录到暂存区。

在第11关时我们曾用 ``git rm``
来删除仓库里的文件，同样地，如果要对仓库里的文件改名，也不要直接用
``mv`` 命令，而要用 ``git mv`` 命令，该命令会自动把改动记录到暂存区。

第22关 reset --soft
===================

这又是一个撤销操作，撤销的是最后一次 ``git commit`` 命令，语法如下：

.. code:: 

   $ git reset --soft HEAD^

``git reset`` 命令有很多复杂的参数，这里暂不细说，其中 ``--soft HEAD^``
表示取消最后一次提交操作，并且暂存区和工作目录的文件均不受影响。

**作用：用于版本的回退，只进行对commit操作的回退，不影响工作区的文件。**

第19关的 ``git commit --amend`` 命令就相当于是先 ``git reset --soft`` 再
``git commit``\ 。

在执行此命令之后，查看日志时会发现最后一次提交的日志消失了。

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/截屏2022-03-14 上午10.40.38.png
   :alt: 

.. _第23关-checkoutfile:

第23关 checkout_file
====================

   A file has been modified, but you don't want to keep the
   modification. Checkout the 'config.rb' file from the last commit.

   一个文件已被修改过，但你不想保留修改过的内容。从最后一次提交中
   checkout 出 'config.rb' 文件。

这还是一个撤销操作。如果你想放弃工作目录中已经修改过的内容，就用这个命令：

.. code:: 

   $ git checkout your-file

Git
会用最后一次提交的文件覆盖掉工作目录中的同名文件。但做这个操作一定要谨慎，因为这个操作是不可以被撤销的，执行之后你修改过的内容就找不回来了。

第24关 remote
=============

   This project has a remote repository. Identify it.

   这个项目有一个远程仓库，找出它。

我们大部分时间都是在操作本地仓库，与远程仓库相关的命令也不多，比如前面的23关中，也只有第5、第6、第18关这3关涉及到了远程仓库。接下来的5关将集中学习有关远程仓库的知识。

我们先来描述一下应用场景。你和其他人同时开发一个项目，大家都从中心仓库
clone
了文件到本地，然后分头工作，此时你只连接了一个远程仓库——中心仓库。如果你的同伴写了一个函数，正好你可以用到它，那么你可以把这个函数
pull
到你的仓库里，这时你就连接了第二个远程仓库——同伴的仓库，你们俩绕过了中心仓库，直接实现了私下交流，这也下是
Git 被称为分布式版本管理系统的原因。

每一个开发者都可以连接多个远程仓库，但是 URL 很长不好记，所以 Git
允许你为每个远程仓库命名，提高效率。

要查看你的项目连接了哪些远程仓库，用下面的命令：

.. code:: 

   $ git remote

第24关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/截屏2022-03-14 上午10.51.43.png
   :alt: 

.. _第25关-remoteurl:

第25关 remote_url
=================

   The remote repositories have a url associated to them. Please enter
   the url of remote_location.

   这个远程仓库有一个与它相关的 URL，请输入远程仓库 remote_location 的
   URL 地址。

承上关，在 ``git remote`` 命令后面加一个 ``-v`` 参数就可以查询远程仓库的
URL 了。

.. code:: 

   $ git remote -v

在查询结果中，每个远程仓库分别列出了 fetch 和 push
的地址，这是因为在有些情况下 fetch 和 push 的地址是不一样的。

第25关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314105326745-20220314105528866.png
   :alt: 

第26关 pull
===========

   You need to pull changes from your origin repository.

   你需要从远程仓库 origin 拉取更新。

当有多人合作一起开发一个项目时，就不止是你一个人向远程仓库提交代码了，你的伙伴也会向远程仓库提交代码。为了得到远程仓库的最新内容，要用下面的命令把内容抓下来：

.. code:: 

   $ git pull remote-name branch-name

其中，remote-name 是远程仓库的名字，branch-name
是远程仓库的分支名字，如果是主干，那就是
master。该命令执行之后，远程仓库的代码会自动合并到本地项目中。

第26关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314110603740.png
   :alt: 

.. _第27关-remoteadd:

第27关 remote_add
=================

   Add a remote repository called 'origin' with the url
   https://github.com/githug/githug

   添加一个远程仓库，名为 'origin'，url 是
   https://github.com/githug/githug

在第25关，我们用 ``git remote -v``
列出了多个远程仓库的地址，那这些地址是怎么添加的呢？

如果你的项目是 clone 来的，那么 Git 会并把 clone
命令的仓库地址保存下来。如果要手工添加远程仓库，请用下面的命令：

.. code:: 

   git remote add remote-name remote-url

第27关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314111038989.png
   :alt: 

第28关 push
===========

   Your local master branch has diverged from the remote origin/master
   branch. Rebase your commit onto origin/master and push it to remote.

   你本地仓库的代码是由远程仓库的 origin/master 分支创建的。rebase
   你的更新到 origin/master，然后提交到远程仓库。

当你和其他伙伴一起开发时，你们都从远程仓库把文件 clone
到本地，然后分头开发，再分头推送到远程仓库中，推送命令如下：

.. code:: 

   $ git push remote-name branch-name
   $ git push -u remote-name branch-name
   $ git push

第1条命令是把本地的文件推送到远程仓库，remote-name是远程仓库名，branch-name是分支名，如果你没有重命名过它们，那它们默认的名称分别是
origin 和 master；第2条命令加了一个 ``-u`` 参数，目的是让 Git 把
remote-name 和 branch-name
记住，下次就不用再写这2个参数了；第3条命令就是使用过 ``-u``
参数以后的推送命令，不需要任何参数了。

多人开发时，推送是有先有后的，按照 Git
的规则，在你推送时如果已经有人比你早推送了，你若再推送就会收到一个
"non-fast forward"
的提示，直译就是“不能快进”。那么此时你至少有2种办法来解决：

方法一，先用 ``git pull``
命令把远程仓库的最新代码合并到本地，然后再提交。这时本地的提交和远程的提交按时间顺序混合排列。

方法二，用 ``git rebase``
命令把本地仓库的更新排到远程仓库更新之后，那这时候本地仓库的所有提交都排在远程仓库的最后一次提交之后。

本关考核的就是用 ``git rebase`` 方法来解决问题。

本关的场景是本地仓库有3次更新（分别名为 First commit, Second commit,
Third commit），远程仓库有1次更新（名为 Fourth commit），在 rebase 并且
push 之后，远程仓库就会有4次更新了。

.. code:: 

   当远程仓库和本地仓库出现不同的更新时:
   	git pull --rebase == git fetch + git rebase 
   这里表示把你的本地当前分支里的每个提交(commit)取消掉，并且把它们临时 保存为补丁(patch)(这些补丁放到".git/rebase"目录中),然后把本地当前分支更新 为最新的"origin"分支，最后把保存的这些补丁应用到本地当前分支上。

第28关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314113135279.png
   :alt: 

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314113225665.png
   :alt: 

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314113307922.png
   :alt: 

第29关 diff
===========

   There have been modifications to the 'app.rb' file since your last
   commit. Find out whick line has changed.

   最后一次提交之后，你又修改了 'app.rb' 这个文件。找到哪一行被修改过。

其中 ``@@ -23,7 +23,7 @@``
表示修改的内容是从第23行往后7行，接下来列出第23行往后7行的内容（其实只修改了第26行这1行，但会列出这1行的前3行和后3行）。其中红色的
``-`` 和绿色的 ``+`` 表示把 '-' 改为了 '+'。

第29关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314114632228.png
   :alt: 

第30关 blame
============

   Someone has put a password inside the file 'config.rb' find out who
   it was.

   有人在 'config.rb' 中植入了一个密码，请找出这是谁干的。

当系统曝出 bug
或者漏洞，要查清问题的来源时，首先定位问题代码，其次定位是谁引入了错误。Git
记录了详细的更新日志，所以通过 Git
提供的一个专门的命令就可以定位开发者：

.. code:: 

   $ git blame your-file

在结果中会列出指定文件的所有代码，每行代码的左侧会列出它最后一次被更新时的
HASH
值、开发者和时间，通过这些信息，你就可以分析每一行代码被谁编辑过了。

第30关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314115027232.png
   :alt: 

第31关 branch
=============

   You want to work on a piece of code that has the potential to break
   things, create the branch test_code.

   你想要修改一处代码，在修改过程中可能会引起一些问题，所以要创建一个分支
   test_code 来修改。

接下来的10关都和分支有关。
如果你想在不影响主线的情况下进行安全的开发，就要以主线为基础创建一个分支，然后在分支上修改，最后再把分支合并到主线上。实际上，一般情况下都是在分支上工作的，因为在一个团队中，你和你的伙伴共享主线，直接在主线下工作会影响其他人，所以每个人都分别在各自的分支上工作。

分支的常用命令如下：

.. code:: 

   $ git branch branch-name
   $ git branch

第1条语句用于创建分支，branch-name
就是你要创建的分支名称；第2条语句用于列出全部分支。

第31关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314143702592.png
   :alt: 

第32关 checkout
===============

   Create and switch to a new branch called my_branch. You will need to
   create a branch like you did in the previous level.

   创建并切换到新分支 my_branch。你要像上一关那样先创建一个分支。

上一关我们创建了分支，但是还没有切换到新分支上。如果你仔细观察，会发现
``git branch`` 语句的结果中，在 ``master`` 前面有一个 ``*``
号，它表示当前你所在的分支。

切换分支的语句是：

.. code:: 

   $ git checkout branch-name
   $ git checkout -b branch-name
   $ git checkout -

第1条语句用于切换到指定的分支；第2条语句加了 ``-b``
参数，表示创建一个分支并且切换到这个新建的分支，相当于连续执行
``git branch branch-name`` 和
``git checkout branch-name``\ ；第3条语句用于切换到上次所在的分支，当你经常在2个分支间来回切换时，用这个命令会比较方便。

不知你是否还记得，第23关我们用到了这样的命令：

.. code:: 

   $ git checkout your-file

它的作用是撤销对一个文件的修改。虽然从形式上看这个命令和本关的命令很相似，但因为参数的含义不一样，一个是文件名，一个是分支名，所以功能是完全不一样的。

第32关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314143856180.png
   :alt: 

.. _第33关-checkouttag:

第33关 checkout_tag
===================

   You need to fix a bug in the version 1.2 of your app. Checkout the
   tag ``v1.2``.

   你要在 1.2 版本中修复一个 bug，切换到 tag 'v1.2'。

在第17关我们学习了如何创建 tag，tag
是一个有语义的标签，便于记忆，我们可以把版本号或其他有特定含义的词语作为
tag。当我们要切换到指定的 tag 时，采用以下命令：

.. code:: 

   $ git checkout tag-name

你一定发现了，这个命令也和切换到分支的命令形式是一样的啊！第17关、第32关、第33关这三关的命令形式都一样，只因参数的含义不同，一个是文件名，一个是分支名，一个是标签名，结局就各不相同。

第33关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314144532140.png
   :alt: 

.. _第34关-checkouttagoverbranch:

第34关 checkout_tag_over_branch
===============================

   You need to fix a bug in the version 1.2 of your app. Checkout the
   tag ``v1.2`` (Note: There is also a branch named ``v1.2``).

   你要在 1.2 版本中修复一个 bug，切换到 tag
   'v1.2'（注意：现在有一个分支也叫 'v1.2'）。

如果存在一个和分支同名的 tag，比如都叫 'v1.2'，那么当执行
``git checkout v1.2`` 命令时，是该切换到分支，还是该切换到 tag
呢？答案是切换到分支。

如果要切换到 tag，就需要按下面这样给出明确的说明：

.. code:: 

   $ git checkout tags/tag-name

第34关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314144657663.png
   :alt: 

.. _第35关-branchat:

第35关 branch_at
================

   You forgot to branch at the previous commit and made a commit on top
   of it. Create branch test_branch at the commit before the last.

   你忘记了在上一个提交之间先创建一个分支就提交了。创建一个分支
   test_branch 在最后一次提交之前。

默认情况下，你使用 ``git branch branch-name``
语句创建分支时，创建出的分支与当前主线的内容是一样的，但是你也可以指定以主线的某一次提交为基础来创建分支，命令格式如下：

.. code:: 

   $ git branch branch-name hash-code

上面命令的最后一个参数表示 ``git commit`` 命令为某次提交生成的 HASH 值。

第35关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314144918069.png
   :alt: 

.. _第36关-deletebranch:

第36关 delete_branch
====================

   You have created too many branches for your project. There is an old
   branch in your repo called 'delete_me', you should delete it.

   你为这个项目创建了太多的分支。有一个旧分支名为
   'delete_me'，删除掉它。

删除分支的命令如下：

.. code:: 

   $ git branch -d branch-name

和创建分支的区别在于增加了一个 ``-d`` 参数。

第36关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314145103198.png
   :alt: 

.. _第37关-pushbranch:

第37关 push_branch
==================

   You've made some changes to a local branch and want to share it, but
   aren't yet ready to merge it with the 'master' branch. Push only
   'test_branch' to the remote repository.

   你的一个本地分支有一些修改，你想把它分享出去，但又不想合并到 master
   分支上。仅把 'test_branch' 推送到远程仓库。

我们曾在第28关学习过推送命令，语法如下：

.. code:: 

   $ git push remote-name branch-name

其中 remote-name 是远程仓库名，branch-name 是分支名。

第37关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314145355774.png
   :alt: 

第38关 merge
============

   We have a file in the branch 'feature'; Let's merge it to the master
   branch.

   你有一个文件在分支 'feature'，把它合并到 master 分支。

当我们在分支完成修改和测试之后，就可以把分支合并到主线上了，它的命令是：

.. code:: 

   $ git merge branch-name

执行这条命令之前，要先切换到主线（一般是 master
分支），然后把待合并的分支名作为参数。

合并之后，在分支上修改过的文件的内容就会体现在主线上，而且日志中也加入了分支的修改日志。

如果遇到主线和分支修改了同一行代码，就会发生冲突，后面的关卡中我们还会学习如何解决冲突。

第38关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314145735740.png
   :alt: 

第39关 fetch
============

   Looks like a new branch was pushed into our remote repository. Get
   the changes without merging them with the local repository

   看起来好像有新的分支推送到了远程仓库。得到新的修改而不要合并到本地仓库。

在第26关我们曾用 ``git pull``
把远程仓库的更新拉到本地仓库，这个命令其实隐含了2个连续的动作，即
``git fetch`` 和 ``git merge``\ 。如果只是抓取数据而不合并，那就不能用
``git pull`` ，而只用前一个动作 ``git fetch`` 就可以了，语法如下：

.. code:: 

   $ git fetch
   $ git branch -r
   $ git log remote-name/branch-name

第1条语句是把远程仓库的数据抓取到本地，但不合并到本地分支；第2条语句是查看远程分支列表，如果远程仓库有了新分支，在
``git fetch`` 之后用 ``git branch -r``
查看时会发现新分支的名称，在本关中新分支名为
'new_branch'；第3条语句用于查看远程分支的日志，比查看本地日志的
``git log`` 语句多了远程仓库名和远程分支名这2个参数。

第39关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314145946728.png
   :alt: 

第40关 rebase
=============

   We are using a git rebase workflow and the feature branch is ready to
   go into master. Let's rebase the feature branch onto our master
   branch.

   我们使用了 git rebase 工作流，feature 分支准备合并到 master。rebase
   这个 feature 分支到我们的 master 分支之上。

在第28关我们曾经使用过一次 ``git rebase`` 命令，现在我们再详细讲解一下。

``git rebase`` 和 ``git merge``
都是用来合并，各有优缺点，所以有些团队会约定合并时只能用 ``git merge``
或只能用 ``git rebase``\ ，如果约定只能用 ``git rebase``
来合并，这种工作方式就被称为 'git rebase 工作流'。在用 ``git rebase``
合并分支时，合并后的日志并非按各分支的提交时间排列，而是把一个分支的日志全部排列在另一个分支的日志之上，即使它们是并行开发的，在开发过程中交错提交，但看起来也好像是按先后顺序开发的一样。

以本题为例，master 是主线，从 master 创建出 feature 分支，此后，master
提交了一次，提交说明是 “add content”，feature 也提交了一次，提交说明是
“add feature”，这时在 master 上执行以下命令：

.. code:: 

   $ git rebase feature

那么 master 的日志就会变成 "add content" 在 "add feature" 之上。

而反过来，如果是在 feature 上执行以下命令：

.. code:: 

   $ git rebase master

那么 feature 的日志就会变成 "add feature" 在 "add content" 之上。

第40关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314150820452.png
   :alt: 

.. _第41关--git-rebase---onto:

第41关 git rebase --onto
========================

   You have created your branch from ``wrong_branch`` and already made
   some commits, and you realise that you needed to create your branch
   from ``master``. Rebase your commits onto ``master`` branch so that
   you don't have ``wrong_branch`` commits.

   你已经从 ``wrong_branch``
   创建了你的分支并且已经做了一些提交，你意识到你需要从 ``master``
   创建你的分支。 将你的提交重新定位到 ``master`` 分支，这样你就没有
   ``wrong_branch`` 提交。

更多git rebase --onto的资料：\ `git rebase
--onto </Users/xiaoyan/Desktop/笔记/git/git rebase --onto>`__

这里考察的是对 git rebase --onto 的理解

题意解释：

master分支：

.. code:: 

   xiaoyan@xiaoyan git_hug % git log master --pretty=oneline
   615c20d5fd3c7bea81a457b5f51596a1955b16a2 (master) Create authors file

wrong_branch分支：

.. code:: 

   xiaoyan@xiaoyan git_hug % git log wrong_branch --pretty=oneline
   a716279bb9535c0531dd8038068ffc95d1173065 (wrong_branch) Wrong changes
   615c20d5fd3c7bea81a457b5f51596a1955b16a2 (master) Create authors file

现在开发的分支：

.. code:: 

   xiaoyan@xiaoyan git_hug % git log --pretty=oneline 
   cb2b42b3280e9e483b3373b411039db4d8189071 (HEAD -> readme-update) Add `Install` header in readme
   7d8e163f3965d22f0ced596615efa41ddb170855 Add `About` header in readme
   59835798b6a9616524b57c55bcb32ca8cd89cbe4 Add app name in readme
   a716279bb9535c0531dd8038068ffc95d1173065 (wrong_branch) Wrong changes  # 不应该有这一条
   615c20d5fd3c7bea81a457b5f51596a1955b16a2 (master) Create authors file

其中现在开发的分支是 基于wrong_branch分支创建的 我们现在发现 该分支
因该直接从master进行创建 ， 变为下面的样子

.. code:: 

   xiaoyan@xiaoyan git_hug % git log --pretty=oneline 
   cb2b42b3280e9e483b3373b411039db4d8189071 (HEAD -> readme-update) Add `Install` header in readme
   7d8e163f3965d22f0ced596615efa41ddb170855 Add `About` header in readme
   59835798b6a9616524b57c55bcb32ca8cd89cbe4 Add app name in readme

   615c20d5fd3c7bea81a457b5f51596a1955b16a2 (master) Create authors file

使用的命令：

.. code:: shell

   git rebase --onto <new-parent> <old-parent> <branch>

第41关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220315155112986.png
   :alt: 

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220315155135190-20220315155309361-20220315155316670.png
   :alt: 

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220315155206113.png
   :alt: 

第41关 repack
=============

   Optimise how your repository is packaged ensuring that redundant
   packs are removed.

   优化你的仓库，重新打包，并清除多余的包。

在第1关里我们提到，当 Git 项目初始化时，会创建一个隐藏的名为 .git
的子目录，用于存放 Git 管理仓库要用到的文件。在 Git
的世界里，一个文件是一个 Git 对象，一次提交也是一个 Git
对象，它们被存储在 .git/objects/ 目录下：

.. code:: 

   $ ls .git/objects/
   4d    a0    e6    info    pack

其中前3个目录的目录名长为2个数字字母，分别各存放1个对象。在 Git
的操作越多，产生的对象就越多，为了优化仓库的效率，你可以手工把对象打包：

.. code:: 

   $ git repack
   $ git repack -d

第1条命令是把对象打包到一起，第2条命令是在打包后删除已作废的对象。执行完打包命令之后，.git/objects/pack/
目录下会生成2个文件：

.. code:: 

   $ ls .git/objects/pack/
   pack-b7b37f445a40715c249bf8c0df9631e9fd6c8f4b.idx
   pack-b7b37f445a40715c249bf8c0df9631e9fd6c8f4b.pack

.pack 是包文件，.idx 是包的索引文件。

第41关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314152422553.png
   :alt: 

第42关 cherry-pick
==================

   Your new feature isn't worth the time and you're going to delete it.
   But it has one commit that fills in ``README`` file, and you want
   this commit to be on the master as well.

   你在新功能上的努力白废了，准备删除掉它，但是往 'README'
   文件里填充内容的那次提交还有用，你要把这次提交合并到主线上。

如果你创建了一个分支，在其中进行了多次提交，而在合并时不想把分支上所有的提交都合并到主线，只想选取其中的1个提交合并到主线，那么你可以用下面的命令：

.. code:: 

   $ git cherry-pick hash-code

其中 hash-code 是某次提交生成的 HASH 值。cherry-pick
直译就是摘樱桃，把一个分支想象成一棵树，多次提交就让树上结满了果实，那么
cherry-pick 命令就是摘下其中的一个果实。

第42关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314153058653.png
   :alt: 

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314153112319.png
   :alt: 

第43关 grep
===========

   Your project's deadline approaches, you should evaluate how many
   TODOs are left in your code.

   项目的交付时间快到了，你要评估一下代码里还遗留了多少待办事项。

和 Linux 的 grep 命令类似，Git 也提供了一个用于搜索文本的 grep 命令：

.. code:: 

   $ git grep keyword
   $ git grep keyword file-name

第1条命令在当前项目下查找指定的关键词；第2条命令在指定的文件中查找关键词。

第43关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314153332586.png
   :alt: 

.. _第44关-renamecommit:

第44关 rename_commit
====================

   Correct the typo in the message of your first (non-root) commit.

   在第一次提交时有一个拼写错误，修正它。

在使用 Git 的过程中，难免会出现要改写提交内容的情况，Git
提供了非常强大的修改历史的工具，我们就以本关为例，详细说明如何修改历史，并在接下来的第45关和第47关再做另外2个练习。

先看一下提交日志：

.. code:: 

   $ git log --pretty=oneline
   771b71dca888e80d2bf716672b1475e85a27d695 Second commit
   06973a37415e520eff0bace38181f131698cd888 First coommit
   37d84aed48418346c4567bb863a0eba4617ba5b1 Initial commit

一共有过3次提交，注意其中哈希值为 "06973a37415e520eff"
的这次提交，提交说明 "First coommit" 中的第2个单词拼错了。

修改提交历史的命令格式是：

.. code:: 

   $ git rebase -i hash-code

我们已经在第40关接触过 ``git rebase``
命令，当时是用它来合并分支。但是加了 ``-i``
参数之后，用途就变为修改提交历史了。其后再跟一个某一条提交日志的哈希值，表示要修改这条日志之前的提交历史。

现在，找到 "First coommit" 下面一条日志的哈希值
"37d84aed48418346c4"，然后输入下面的命令：

.. code:: 

   $ git rebase -i 37d84aed48418346c4

这时，会启动文本编辑器，显示如下内容：

.. code:: 

   pick 06973a3 First coommit
   pick 771b71d Second commit

这2行是历史日志，但和 ``git log`` 的区别在于 ``git log``
是按更新时间从后到前显示日志，而这里是按从前到后显示。每一行的前面有一个命令词，表示对此次更新执行什么操作，有以下几种命令：

-  "pick"，表示执行此次提交；

-  "reword"，表示执行此次提交，但要修改备注内容；

-  "edit"，表示可以修改此次提交，比如再追加文件或修改文件；

-  "squash"，表示把此次提交的内容合并到上次提交中，备注内容也合并到上次提交中；

-  "fixup"，和 "squash" 类似，但会丢弃掉此次备注内容；

-  "exec"，执行命令行下的命令；

-  "drop"，删除此次提交。

本关就使用 "reword" 命令来完成任务。把第1行前面的 "pick" 改为
"reword"（注意，不用改哈希值后面的备注内容），如下：

.. code:: 

   reword 06973a3 First coommit
   pick 771b71d Second commit

接下来保存并退出，马上系统会再次打开编辑器，显示以下内容：

.. code:: 

   First coommit

   # Please enter the commit message for your changes.

这时，你把 "coommit" 改为
"commit"，保存并退出，再查看日志，就会发现历史日志的备注内容已经改变了。

第44关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314154244695.png
   :alt: 

第45关 squash
=============

   You have committed several times but would like all those changes to
   be one commit.

   你提交过几次，但是现在想把这些提交合并成一次提交。

承上关，如果要把多次合并合并成一次提交，可以用 ``git rebase -i`` 的
``squash`` 命令。

先查一下提交日志：

.. code:: 

   $ git log --pretty=oneline
   55d9ec9d216767dd1e080c32f5bcff1b3c62ab5b Updating README (squash this commit into Adding README)
   749b65067db05a02515c580ad8e791306ff02305 Updating README (squash this commit into Adding README)
   1ac3ed61a0ae302cf76dc6f3a37e56e2b5f750f9 Updating README (squash this commit into Adding README)
   606be40cc9e5c684cab87c22c37a9d0225308761 Adding README
   994f2b3a2df48ef4a406a5c62b4b6f6c8c1fac03 Initial Commit

从查询结果看出，添加了 README 之后来又对它做了3次修改。

找到 "Adding README" 下面一条日志的哈希值 "994f2b3a2df48ef4a4"，执行
``reabse`` 命令：

.. code:: 

   $ git rebase -i 994f2b3a2df48ef4a4

系统自动打开文本编辑器，显示历史日志：

.. code:: 

   pick 606be40 Adding README
   pick 1ac3ed6 Updating README (squash this commit into Adding README)
   pick 749b650 Updating README (squash this commit into Adding README)
   pick 55d9ec9 Updating README (squash this commit into Adding README)

把后3条日志前面的 "pick" 命令都改成 "squash"：

.. code:: 

   pick 606be40 Adding README
   squash 1ac3ed6 Updating README (squash this commit into Adding README)
   squash 749b650 Updating README (squash this commit into Adding README)
   squash 55d9ec9 Updating README (squash this commit into Adding README)

保存退出，系统再次自动打开编辑器，内容是合并过的更新说明：

.. code:: 

   # This is a combination of 4 commits.
   # The first commit's message is:
   Adding README

   # This is the 2nd commit message:

   Updating README (squash this commit into Adding README)

   # This is the 3rd commit message:

   Updating README (squash this commit into Adding README)

   # This is the 4th commit message:

   Updating README (squash this commit into Adding README)

你可以在此编辑合并之后的更新说明，然后保存退出。再查日志，就会发现3次
"Updating README" 的提交都合并到 "Adding README" 中了。

.. code:: 

   $ git log --pretty=oneline
   3e8c0e3a729a9d5f959214a2267c481ff0197722 Adding README
   994f2b3a2df48ef4a406a5c62b4b6f6c8c1fac03 Initial Commit

第45关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314154904394.png
   :alt: 

.. _第46关-mergesquash:

第46关 merge_squash
===================

   Merge all commits from the long-feature-branch as a single commit.

   把名为 long-feature-branch
   的分支合并到主干，把分支中的多次提交合并为主干上的一次提交。

在第38关我们曾学习过 ``merge`` 合并，它的语法是：

.. code:: 

   $ git merge branch-name

如果分支曾经提交过多次，那么用上面的语句合并之后，主干的日志也会出现多次提交记录。为了符合本关题意，把分支的多次提交合并为主干上的一次提交，要加一个
``squash`` 参数，如下：

.. code:: 

   $ git merge branch-name --squash

如果不加 ``squash`` 参数，在合并之后系统会默默地做一个 ``commit``
操作，而加了 ``squash`` 参数之后，不会自动
``commit``\ ，这时你还需要手动执行 ``commit`` 命令，并且写上提交说明。

第46关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314155511456.png
   :alt: 

第47关 reorder
==============

   You have committed several times but in the wrong order. Please
   reorder your commits.

   你提交过几次，但是提交的顺序错了，请调整提交顺序。

在第44关和第45关我们使用 ``git rebase -i``
命令修改了历史日志的提交说明、把多次提交合并成了一次，在本关，我们要用这个命令来调整提交顺序。

先查一下提交日志：

.. code:: 

   $ git log --pretty=oneline
   3baec3ba260f841e097675e4ae6661a86e3dba50 Second commit
   a5f696b57d524c83b9fbb094b013590e4ff3d43d Third commit
   19f3b096c2765ab79d9b07a5bed3a4ebb83ebf6a First commit
   f0c159847ae93dabc8fd23766b40cf0cc21b315d Initial Setup

从上面的查询结果看出，"Second commit" 和 "Third commit"
的次序颠倒了。我们找到最后一条日志的哈希值
"f0c159847ae93"，然后输入下面的命令：

.. code:: 

   $ git rebase -i f0c159847ae93

系统自动打开文本编辑器，显示出了历史日志：

.. code:: 

   pick 19f3b09 First commit
   pick a5f696b Third commit
   pick 3baec3b Second commit

把第2行和第3行的内容调整一下顺序，即这样：

.. code:: 

   pick 19f3b09 First commit
   pick 3baec3b Second commit
   pick a5f696b Third commit

然后保存退出，系统就会按照调整过的顺序重新执行一遍提交操作。再查看日志，发现顺序已经调整好了。

.. code:: 

   $ git log --pretty=oneline
   58fe3005755a19d18c017973517dfaca1b1ae648 Third commit
   e0e8d4428578fb7b1284b1c7902e435e9bd571c4 Second commit
   19f3b096c2765ab79d9b07a5bed3a4ebb83ebf6a First commit
   f0c159847ae93dabc8fd23766b40cf0cc21b315d Initial Setup

第47关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314155705317.png
   :alt: 

第48关 bisect
=============

   A bug was introduced somewhere along the way. You know that running
   "ruby prog.rb 5" should output 15. You can also run "make test". What
   are the first 7 chars of the hash of the commit that introduced the
   bug.

   在开发过程中引入了一个 bug。已知运行 "ruby prog.rb 5" 应该输入
   15，你也可以运行 "make test" 进行测试。你需要确定引入 bug
   的那次提交的哈希值的前7位。

在程序持续迭代的过程中不免会引入 bug，除了定位 bug
的代码片断，我们还想知道 bug 是在什么时间被引入的，这时就可以借助 Git
提供的 ``bisect`` 工具来查找是哪次提交引入了 bug。\ ``bisect``
是用二分法来查找的，就像用二分查找法查找数组元素那样。

运行 ``make test`` 可以测试程序是否正确执行，它会先执行 "ruby prog.rb 5"
语句，然后再分析输出结果是否等于15，如果不等于15，就会显示
``make: *** [test] Error 1``\ 。

我们先看一下提交历史，一共20次提交：

.. code:: 

   $ git log --pretty=oneline
   12628f463f4c722695bf0e9d603c9411287885db Another Commit
   979576184c5ec9667cf7593cf550c420378e960f Another Commit
   028763b396121e035f672ef5af75d2dcb1cc8146 Another Commit
   888386c77c957dc52f3113f2483663e3132559d4 Another Commit
   bb736ddd9b83d6296d23444a2ab3b0d2fa6dfb81 Another Commit
   18ed2ac1522a014412d4303ce7c8db39becab076 Another Commit
   5db7a7cb90e745e2c9dbdd84810ccc7d91d92e72 Another Commit
   7c03a99ba384572c216769f0273b5baf3ba83694 Another Commit
   9f54462abbb991b167532929b34118113aa6c52e Another Commit
   5d1eb75377072c5c6e5a1b0ac4159181ecc4edff Another Commit
   fdbfc0d403e5ac0b2659cbfa2cbb061fcca0dc2a Another Commit
   a530e7ed25173d0800cfe33cc8915e5929209b8e Another Commit
   ccddb96f824a0e929f5fecf55c0f4479552246f3 Another Commit
   2e1735d5bef6db0f3e325051a179af280f05573a Another Commit
   ffb097e3edfa828afa565eeceee6b506b3f2a131 Another Commit
   e060c0d789288fda946f91254672295230b2de9d Another Commit
   49774ea84ae3723cc4fac75521435cc04d56b657 Another Commit
   8c992afff5e16c97f4ef82d58671a3403d734086 Another Commit
   80a9b3d94237f982b6c9052e6d56b930f18a4ef5 Another Commit
   f608824888b83bbedc1f658be7496ffea467a8fb First commit

首先启动 ``bisect`` 查找流程：

.. code:: 

   $ git bisect start
   $ git bisect good f608824888b
   $ git bisect bad 12628f463f4
   Bisecting: 9 revisions left to test after this (roughly 3 steps)
   [fdbfc0d403e5ac0b2659cbfa2cbb061fcca0dc2a] Another Commit

第2行和第3行是定义 ``bisect`` 的查找范围，\ ``git bisect good`` 和
``git bisect bad``
表示当前程序通过或没有通过测试，在第2行后面以第一次提交的哈希值为参数，在第3行后面以最后一次提交的哈希值为参数，说明查找范围是全部20次提交。接着
Git 定位了位于中间那个提交，它的哈希值是
"fdbfc0d403e5a"，并计算出剩余的提交还有9次，大约还需要3次二分查找。

这时，我们对程序进行测试，测试通过，所以我们反馈 ``good``\ ：

.. code:: 

   $ make test
   ruby prog.rb 5 | ruby test.rb
   $ git bisect good
   Bisecting: 4 revisions left to test after this (roughly 2 steps)
   [18ed2ac1522a014412d4303ce7c8db39becab076] Another Commit

Git 继续进行二分查找，这次定位的哈希值是
"18ed2ac1522a01"，我们再对程序测试，测试没有通过，所以我们反馈
``bad``\ ：

.. code:: 

   $ make test
   ruby prog.rb 5 | ruby test.rb
   make: *** [test] Error 1
   $ git bisect bad
   Bisecting: 2 revisions left to test after this (roughly 1 step)
   [9f54462abbb991b167532929b34118113aa6c52e] Another Commit

就这样，经过几轮测试，当 Git 给出下面的消息时，表示找到了：

.. code:: 

   18ed2ac1522a014412d4303ce7c8db39becab076 is the first bad commit

下面是对查找过程的回顾：

.. code:: 

   12628f463f4c72 Another Commit
   979576184c5ec9 Another Commit
   028763b396121e Another Commit
   888386c77c957d Another Commit
   bb736ddd9b83d6 Another Commit
   18ed2ac1522a01 Another Commit 第2次 bad
   5db7a7cb90e745 Another Commit 第4次 good
   7c03a99ba38457 Another Commit
   9f54462abbb991 Another Commit 第3次 good
   5d1eb75377072c Another Commit
   fdbfc0d403e5ac Another Commit 第1次 good
   a530e7ed25173d Another Commit
   ccddb96f824a0e Another Commit
   2e1735d5bef6db Another Commit
   ffb097e3edfa82 Another Commit
   e060c0d789288f Another Commit
   49774ea84ae372 Another Commit
   8c992afff5e16c Another Commit
   80a9b3d94237f9 Another Commit
   f608824888b83b First commit

第48关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314161331138.png
   :alt: 

.. _第49关-stagelines:

第49关 stage_lines
==================

   You've made changes within a single file that belong to two different
   features, but neither of the changes are yet staged. Stage only the
   changes belonging to the first feature.

   你修改了一个文件的多处代码，这些代码分属于2个不同的功能，代码还没有提交到暂存区。仅提交第1个功能相关的代码到暂存区。

用 ``git add``
命令可以把文件添加到暂存区，但如果你不想把文件中的全部修改都提交到暂存区，或者说你只想把文件中的部分修改提交到缓存区，那么你需要加上
``edit`` 参数：

.. code:: 

   $ git add your-file --edit

这时 Git 会自动打开文本编辑器，编辑的内容就是 ``git diff``
命令的结果，这时你就可以编辑2个文件之间的差异，只保留要提交到暂存区的差异，而删除不需要提交到暂存区的差异，然后保存退出，Git
就会按你编辑过的差异把相应的内容提交到暂存区。

比如本关，文件的差异为：

.. code:: 

   $ git diff feature.rb
   diff --git a/feature.rb b/feature.rb
   index 1a271e9..4a80dda 100644
   --- a/feature.rb
   +++ b/feature.rb
   @@ -1 +1,3 @@
    this is the class of my feature
   +This change belongs to the first feature
   +This change belongs to the second feature

从最后2行可以看出，新增的代码分别对应2个不同的功能，如果我们只想提交第1个功能的代码，删除掉最后一行即可。

第49关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314161647763.png
   :alt: 

.. _第50关-findoldbranch:

第50关 find_old_branch
======================

   You have been working on a branch but got distracted by a major issue
   and forgot the name of it. Switch back to that branch.

   你在一个分支上工作时，被分派处理一个重要的问题，可是处理完这个问题之后，你忘了刚才是在哪个分支上工作了。切换回那个分支。

这种情况确实经常发生，笨办法就是逐个进入各个分支查看日志，再回忆一下刚才的工作情景。而
Git 提供了一个工具，可以用来查看你在 Git 上的历史操作：

.. code:: 

   $ git reflog
   894a16d HEAD@{0}: commit: commit another todo
   6876e5b HEAD@{1}: checkout: moving from solve_world_hunger to kill_the_batman
   324336a HEAD@{2}: commit: commit todo
   6876e5b HEAD@{3}: checkout: moving from blowup_sun_for_ransom to solve_world_hunger
   6876e5b HEAD@{4}: checkout: moving from kill_the_batman to blowup_sun_for_ransom
   6876e5b HEAD@{5}: checkout: moving from cure_common_cold to kill_the_batman
   6876e5b HEAD@{6}: commit (initial): initial commit

你看，不仅与文件相关的 ``git commit`` 操作被记录了，连你
``git checkout``
操作也都记下来了，现在，你就知道此前是怎么在各个分支之间跳转的了。

第50关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314162031818.png
   :alt: 

第51关 revert
=============

   You have committed several times but want to undo the middle commit.
   All commits have been pushed, so you can't change existing history.

   你提交了多次，但想取消中间的某次提交。所有提交的内容都已经推送到服务端了，所以你不能改变已有的历史。

我们曾用过修改提交历史的 ``git rebase -i``
命令，用此方法可以取消多次提交中的某次提交，不过，这只是针对还没有推送到服务端的情况，如果已经提交到服务端，你就不能改变已有的历史了，只能想别的办法解决了。

Git 提供了 ``revert``
工具来解决这种问题，它相当于是对某次提交的逆操作，比如你提交时新建了一个文件，那么
Git 就会创建一个删除此文件的提交。语法如下：

.. code:: 

   $ git revert hash-code
   $ git revert hash-code --no-edit

其中的 hash-code 就是你要取消的提交的哈希值。第2条命令中的 ``no-edit``
参数表示由系统自动生成一句提交说明，如果没有这个参数，Git
会自动调用文本编辑器请你编写提交说明。

第51关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314162431316.png
   :alt: 

第52关 restore
==============

   You decided to delete your latest commit by running
   ``git reset --hard HEAD^``. (Not a smart thing to do.) You then
   change your mind, and want that commit back. Restore the deleted
   commit.

   你决定用 ``git reset --hard HEAD^``
   删除最后一次提交（一个不太明智的决定），然后你又反悔了，想回退到这条命令之前。请恢复被删除的提交。

我们先查一下提交日志，发现有过2次提交：

.. code:: 

   $ git log --pretty=oneline
   1dc1ecdd071fd2a5baa664dce42a48b13d40cdae First commit
   e586f55fde799d2b390d8a74d771db75279841f3 Initial commit

再看看操作日志：

.. code:: 

   $ git reflog
   1dc1ecd HEAD@{0}: reset: moving to HEAD^
   f766953 HEAD@{1}: commit: Restore this commit
   1dc1ecd HEAD@{2}: commit: First commit
   e586f55 HEAD@{3}: commit (initial): Initial commit

哦，原来还曾有过第3次提交，不过被 ``git reset --hard HEAD^``
删除掉了。\ ``git reset --hard HEAD^``
用于删除最后一次提交，使工作区恢复到上一次提交时的状态，仔细观察上面的操作日志也能发现，其中
"HEAD@{2}" 和 "HEAD@{0}" 的哈希值是一样的。

如果要撤销这条命令本身，也就是恢复到执行这条命令之前的状态，我们可以用下面的命令形式：

.. code:: 

   $ git reset --hard hash-code

上面命令中的 hash-code
就是你要恢复到的那次提交的哈希值。在执行此命令之后，提交日志中会增加一条提交日志，操作日志会自动增加一条
"reset: moving to hash-code" 的日志。

第52关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314162636130.png
   :alt: 

第53关 conflict
===============

   You need to merge mybranch into the current branch (master). But
   there may be some incorrect changes in mybranch which may cause
   conflicts. Solve any merge-conflicts you come across and finish the
   merge.

   你要把名为 mybranch 的分支合并到当前分支 master
   中，但是可能有些地方的修改会引起冲突。请解决冲突，完成合并。

在第38关我们学习过 ``git merge``
命令，但在工作中难免会发生合并冲突。发生冲突的原因是合并分支与被合并分支都修改了同一个文件的同一行代码，此时
Git 系统要求你介入，决定是保留你的代码还是别人的代码，或者都保留下来。

当发生冲突时，Git 会给出以下提示：

.. code:: 

   $ git merge mybranch
   Auto-merging poem.txt
   CONFLICT (content): Merge conflict in poem.txt
   Automatic merge failed; fix conflicts and then commit the result.

以上信息告诉你自动合并失败，需要你手动解决冲突并提交修改后的结果。在本关中，是一个名为
poem.txt 的文件的第2行代码发生了冲突。

这时你可以编辑有冲突的文件，文件内容如下：

.. code:: 

   Humpty dumpty
   <<<<<<< HEAD
   Categorized shoes by color
   =======
   Sat on a wall
   >>>>>>> mybranch
   Humpty dumpty
   Had a great fall

其中7个左尖括号 ``<<<<<<<`` 和7个右尖括号 ``>>>>>>>``
之间的区域是冲突的部分，而中间的7个等号 ``=======``
则把有冲突的代码分开，上部分是你的代码（通常是主线代码），下部分是别人的代码（通常是开发分支的代码）。编辑这部分内容，保留你想要的，删除你不要的，保存退出，再单独提交这个文件即可。

第53关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314163230751.png
   :alt: 

第54关 submodule
================

   You want to include the files from the following repo:
   ``https://github.com/jackmaney/githug-include-me`` into a the folder
   ``./githug-include-me``. Do this without cloning the repo or copying
   the files from the repo into this repo.

   你想把 ``https://github.com/jackmaney/githug-include-me``
   这个仓库的代码引入到自己项目的 ``./githug-include-me``
   目录，这个方法不需要克隆第三方仓库，也不需要把第三方仓库的文件复制到你的项目中。

如果你想把别人的仓库代码作为自己项目一个库来使用，可以采用模块化的思路，把这个库作为模块进行管理。Git
专门提供了相应的工具，用如下命令把第三方仓库作为模块引入：

.. code:: 

   $ git submodule add module-url

其中的 module-url 就是第三方仓库的地址。

第54关过关画面如下：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220314163807050.png
   :alt: 

第55关 contribute
=================

   This is the final level, the goal is to contribute to this repository
   by making a pull request on GitHub. Please note that this level is
   designed to encourage you to add a valid contribution to Githug, not
   testing your ability to create a pull request. Contributions that are
   likely to be accepted are levels, bug fixes and improved
   documentation.

   这是最后一关，目标是让你在 Github 上提交一个 pull request
   贡献。设计本关的目的就是鼓励你向 Githug 提交贡献，而不是测试你使用
   pull request 的技能。贡献包括新的关卡、修复BUG和改善文档。

.. |image1| image:: https://gitee.com/T-hree/Blog/raw/master/img/image-20220315094506374.png
