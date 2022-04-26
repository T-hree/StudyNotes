git commit --amend用法
======================

**适用场景：**

比方说，你的代码已经提交到git库，leader审核的时候发现有个Java文件代码有点问题，于是让你修改，通常有2种方法：

**方法1**\ ：leader 将你提交的所有代码 abandon掉，然后你回去 通过git
reset
…将代码回退到你代码提交之前的版本，然后你修改出问题的Java文件，然后 git
add xx.java xxx.java -s -m “Porject : 1.修改bug…”

最后通过 git push origin HEAD:refs/for/branches

**方法2**\ ：

leader不abandon代码，你回去之后，修改出问题的Java文件，修改好之后，git
add 该出问题.java

然后 git commit –amend –no-edit,

最后 git push origin HEAD:refs/for/branches。

当我们想要对上一次的提交进行修改时，我们可以使用git commit
–amend命令。git commit
–amend既可以对上次提交的内容进行修改，也可以修改提交说明。

**举个例子：**

Step1：我们先在工作区中创建两个文件a.txt和b.txt。并且add到暂存区，然后执行提交操作：

Step2：此时我们查看一下我们的提交日志：

可以看到我们的提交日志中显示最新提交有两个文件被改变。

Step3：此时我们发觉我们忘了创建文件c.txt，而我们认为c.txt应该和a.txt,b.txt一同提交，而且a.txt文件中应该有内容‘a’。于是我们在工作区中创建c.txt，并add到暂存区。并且修改a.txt（故意写错语法且没有将a.txt的修改add到暂存区）：

Step4：我们查看一下此时的提交日志，可以看到上次的提交0c35a不见了，并且新的提交11225好就是上次提交的修补提交，它就像是在上次提交被无视了，修改后重新进行提交了一样：

Step5：此时我们发现a.txt文件修改没有成功，于是我们还得进行一次对a.txt的修改，将a.txt
add到stage，然后再执行一次与上一次类似的提交修补：

OK了，git commit –amend的用法大致就是这样。

**总结：git commit --amend
相当于上次提交错误的信息被覆盖了，gitk图形化界面上看不到上次提交的信息，git
log上也看不到之前的信息，而add 后再commit
相当于重新加了一个信息。相当于打了个补丁？**

修改commit的提交信息
====================

有时你提交过代码之后，发现一个地方改错了，你下次提交时不想保留上一次的记录；或者你上一次的commit
message的描述有误，这时候你可以使用接下来的这个命令：git commit
--amend。

git功能十分强大，接下来我将讲解一下git commit --amend命令的用法~

git log之后，可以看到你之前提交过的git历史：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/v2-0d0a335a3a87091c40ce138b8be1a9f0_1440w-20220312164430925.jpg
   :alt: 

接下来，在bash里输入wq退出log状态，执行：

.. code:: text

   $ git commit --amend

这时bash里会出现以下内容：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/v2-b2ab0be08ad6a72d151c5a0ef94ed646_1440w-20220312164430971.jpg
   :alt: 

其中，\ *second commit*
是你上次提交的描述，下面是一下说明信息，有告诉你上次提交的文件信息等等，可忽略。接下来你要是想修改描述信息的话。直接键入：i，此时进入了输入模式，变成这样子：

.. figure:: https://pic2.zhimg.com/80/v2-c7756d0088e911ef843b5600365926bd_1440w.jpg
   :alt: 

可用键盘上下键转到描述所在的那一行，然后进行修改：

.. figure:: https://pic3.zhimg.com/80/v2-c5da05b7c480adeab60361e7c97c298e_1440w.jpg
   :alt: 

修改完成后，按下 Esc键退出编辑模式，在键入 :wq
回车退出并保存修改，完成提交。这是你再git log 看一下提交日志：

.. figure:: https://gitee.com/T-hree/Blog/raw/master/img/v2-e622a7ece92566b273eb9b70f48547b8_1440w-20220312164431048.jpg
   :alt: 

| 已经修改了提交描述信息，且原来的git版本没有了\ [STRIKEOUT:~喜大普奔！！你完成]
| 但是有个地方要注意，就是该操作会改变你原来的commit id哦。
