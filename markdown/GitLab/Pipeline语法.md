# Pipeline语法



## job

在每个项目中， 使用名为 .gitlab-ci.yml 文件配置 GitLab CI/CD管道。

在文件中可以定义一个或者多个作业（job）

每个作业必须具有唯一的名称(不能使用关键字)

每个作业是独立执行的。 作业定义了在约束条件下进行相关操作，每个作业至少要包含一个script



```yaml
job1:
  script: "job1 is running script"

job2: 
  script: "job2 ......."
```



这里在Pipeline中定义了两个作业， 每个作业运行不同的命名。 命令可以是shell或脚本 



## script

每个作业至少要包含一个script

 ```yaml
 
 job:
   script:
     - uname -a
     - bundle exec rspec
 ```



注意： 有时，`script` 命令将需要用单引号和双引号引起来。 例如 包含冒号命令（`:`）需要加引号，以便被包裹的YAML解析器知道来解释整个时间作为一个字符串，而不是一个 "键: 值"对。使用特殊字符是也要小心,如：`{}` ,`[]`, `,`,`.` 等等等.....



## before_script

用于定义一个命令， 该命令在每个作业之前运行。 必须是一个数组。指定的 script 与主脚本中指定的任何脚本串联在一起， 并在单个shell中之前执行

Before_script 失败导致整个作业失败，其他作业将不在执行。作业失败不会影响 after_script 运行



## after_script

用于定义将每个作业 (包括失败的任务) 之后运行的命令

这必须是一个数组

指定的脚本在新的shell中执行，与任何before_script 或script脚本分开



## stages

用于定义作业可以使用的阶段（顺序）， 并且是全局定义的。

同一阶段的作业 并行运行， 不同阶段按顺序执行。

```yaml
stages:
  - build
  - test 
  - codescan
  - deploy
```



## .pre & .post

.pre 始终是整个管道的第一个运行阶段， .post始终是整个管道的最后一个运行阶段。

用户定义的阶段都在两者之间运行。 .pre 和 .post 的顺序无法更改。

如果管道仅包含.pre 或 .post 的作业， 则不会创建管道

```yaml
test:
  stage: .pre
  tags:
    - build
  only:
    - main
  script:
    - echo "test"
text1:
  stage: .post
  tags:
    - deploy
  script:
    - echo "test1"
 
```



## stage



是按job定义的，并且依赖于全局定义的 stages。 它允许将作业分为不同的阶段, 并且同一stage 作业可以并行执行（取决于 特定条件）



![image-20220823153143512](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220823153143512.png)



在这里可能遇到 两个job看上去是 并行运行的  实际上并没有

这里的原因是 使用了同一个runner  

每个runner 每次运行的作业数量默认是1, 将它改为10 即可

```shell
vim /etc/gitlab-runner/config.toml

concurrent = 10
```

![image-20220823153618595](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220823153618595.png)



## variables

定义变量， pipeline 变量， job变量， job变量优先级最大





