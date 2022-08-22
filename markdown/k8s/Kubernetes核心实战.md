# Kubernetes核心实战

## 1、资源创建方式 

●命令行

●YAML 



## 2、Namespace 

名称空间用来隔离资源

```shell
kubectl create ns hello
kubectl delete ns hello
```

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: hello
```

## 3、Pod

运行中的一组容器，Pod是kubernetes中应用的最小单位.

![img](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/1625484036923-09a15ef3-33dc-4e29-91e4-e7fbc69070ce.png)



```yaml
kubectl run mynginx --image=nginx

# 查看default名称空间的Pod
kubectl get pod 
# 描述
kubectl describe pod 你自己的Pod名字
# 删除
kubectl delete pod Pod名字
# 查看Pod的运行日志
kubectl logs Pod名字

# 每个Pod - k8s都会分配一个ip
kubectl get pod -owide
# 使用Pod的ip+pod里面运行容器的端口
curl 192.168.169.136

# 集群中的任意一个机器以及任意的应用都能通过Pod分配的ip来访问这个Pod
```



```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: myapp
  name: myapp
spec:
  containers:
  - image: nginx
    name: nginx
  - image: flask
    name: flask
```

![image.png](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/1625553938232-51976552-5bab-4c98-bb8d-c4bf612bf866.png)

***此时的应用还不能外部访问\***



## 4、Deployment

控制Pod，使Pod拥有多副本，自愈，扩缩容等能力

```she
# 清除所有Pod，比较下面两个命令有何不同效果？
kubectl run mynginx --image=nginx

kubectl create deployment myflask --image=myflask
# 自愈能力
```

### 1、多副本

```shell
kubectl create deployment my-dep --image=nginx --replicas=3
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: my-dep
  name: my-dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-dep
  template:
    metadata:
      labels:
        app: my-dep
    spec:
      containers:
      - image: nginx
        name: nginx
```

### 2、扩缩容

```shell
kubectl scale --replicas=5 deployment/my-dep  # 命令指定 副本个数
kubectl edit deployment my-dep  # 编辑 yaml文件实现
```



### 3、自愈&故障转移

- 停机
- 删除Pod
- 容器崩溃
- ....

### 4、滚动更新

```shell
kubectl set image deployment/my-dep nginx=nginx:1.16.1 --record
kubectl rollout status deployment/my-dep
```

### 5、版本回退

```shell
#历史记录
kubectl rollout history deployment/my-dep


#查看某个历史详情
kubectl rollout history deployment/my-dep --revision=2

#回滚(回到上次)
kubectl rollout undo deployment/my-dep

#回滚(回到指定版本)
kubectl rollout undo deployment/my-dep --to-revision=2
```

> 更多：
>
> 除了Deployment，k8s还有 `StatefulSet` 、`DaemonSet` 、`Job`  等 类型资源。我们都称为 `工作负载`。
>
> 有状态应用使用  `StatefulSet`  部署，无状态应用使用 `Deployment` 部署
>
> https://kubernetes.io/zh/docs/concepts/workloads/controllers/



# 5、Service

> 将一组 [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/) 公开为网络服务的抽象方法。

```shell
#暴露Deploy
kubectl expose deployment my-dep --port=8000 --target-port=80

#使用标签检索Pod
kubectl get pod -l app=my-dep
```



