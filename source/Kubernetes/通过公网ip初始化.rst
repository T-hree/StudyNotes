========================
通过公网ip初始化
========================



正常初始化
=====================

::

    ip a  ==> 172.16.16.4
    kubeadm init \
    --apiserver-advertise-address=172.16.16.4 \   # 必须是内网ip
    --control-plane-endpoint=cluster-endpoint \  # 入口别名
    --image-repository registry.cn-hangzhou.aliyuncs.com/lfy_k8s_images \  # 容器镜像指定下载地址
    --kubernetes-version v1.20.9 \  # 版本
    --service-cidr=10.96.0.0/16 \
    --pod-network-cidr=192.168.0.0/16   # 网络插件（calico的指定地址 如需修改 插件也需要修改）

公共初始化后：
::

    Your Kubernetes control-plane has initialized successfully!

    To start using your cluster, you need to run the following as a regular user:

      mkdir -p $HOME/.kube
      sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
      sudo chown $(id -u):$(id -g) $HOME/.kube/config

    Alternatively, if you are the root user, you can run:

      export KUBECONFIG=/etc/kubernetes/admin.conf

    You should now deploy a pod network to the cluster.
    Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
      https://kubernetes.io/docs/concepts/cluster-administration/addons/

    You can now join any number of control-plane nodes by copying certificate authorities
    and service account keys on each node and then running the following as root:

      kubeadm join cluster-endpoint:6443 --token 6wky18.3wagdhvdkwm25fpz \
        --discovery-token-ca-cert-hash sha256:70f02dd21cc5ae6d39fb8ed04bc5b5c04299d741e8cd64065a5e8cbc038b7256 \
        --control-plane

    Then you can join any number of worker nodes by running the following on each as root:

    kubeadm join cluster-endpoint:6443 --token 6wky18.3wagdhvdkwm25fpz \
        --discovery-token-ca-cert-hash sha256:70f02dd21cc5ae6d39fb8ed04bc5b5c04299d741e8cd64065a5e8cbc038b7256

此时如果将 --apiserver-advertise-address= 后面的ip修改为公网ip这次就会初始化失败:
::

    [wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s

    [kubelet-check] Initial timeout of 40s passed.

    systemctl status kubelet
    not "master" find  找不到主节点

找到原因
===================

1. 当指定"--apiserver-advertise-address"为公网ip时，kubeadm会在"[kubelet-check] Initial timeout of 40s passed."后卡很长时间，然后提示说初始化失败

2. 查看kubelet日志，发现`not "master" find`错误提示。于是进行了第二次尝试，并新建了一个ssh对话，用来查看在初始化的时候docker容器的状态

3. docker ps -a 发现etcd的容器处于退出状态:
::

    57eac1801556   0369cf4303ff      "etcd --advertise-cl…"   5 s ago   Exited      k8s_etcd_ecd-k8s-master_kube-system

4. 于是对该容器打个log 显示无法指定ip,ip为公网ip

5. 查看kubeadm生成的etcd配置文件，"xxx"为我的公网ip:
::

    containers:
      - command:
        - etcd
        - --advertise-client-urls=https://182.61.32.58:2379
        - --cert-file=/etc/kubernetes/pki/etcd/server.crt
        - --client-cert-auth=true
        - --data-dir=/var/lib/etcd
        - --initial-advertise-peer-urls=https://182.61.32.58:2380
        - --initial-cluster=k8s-master=https://182.61.32.58:2380
        - --key-file=/etc/kubernetes/pki/etcd/server.key
        - --listen-client-urls=https://0.0.0.0:2379   # !!!
        - --listen-metrics-urls=http://127.0.0.1:2381
        - --listen-peer-urls=https://0.0.0.0:2380   # !!!
        - --name=k8s-master
        - --peer-cert-file=/etc/kubernetes/pki/etcd/peer.crt
        - --peer-client-cert-auth=true
        - --peer-key-file=/etc/kubernetes/pki/etcd/peer.key
        - --peer-trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt
        - --snapshot-count=10000
        - --trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt
        image: registry.cn-hangzhou.aliyuncs.com/lfy_k8s_images/etcd:3.4.13-0
        imagePullPolicy: IfNotPresent

发现kubeadm自动把"--listen-peer-urls"改为了kubeadm初始化时指定的"--apiserver-advertise-address"，
即公网ip，而且"--listen-client-urls="，后面也加上了公网ip。这两个参数大概意思是指定要监听的ip地址，
而云服务器的网卡没有配置公网ip，因此就无法指定该ip，导致etcd无法正常启动。对其进行修改即可，
经测试，worker node 可以通过指定的公网ip join到master node，可以完成项目部署。