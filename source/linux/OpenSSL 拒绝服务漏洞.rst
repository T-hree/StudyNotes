.. _openssl--拒绝服务漏洞排查处置手册:

OpenSSL 拒绝服务漏洞排查处置手册
================================

.. _1-基本情况:

1、 基本情况
------------

OpenSSL
是一个开放源代码的软件库包，应用程序可以使用这个包来保护安全通信，避免窃听，同时确认另一端连接者的身份，OpenSSL
采用 C 语言作为主要开发语言，这使得 OpenSSL
具有优秀的跨平台性能，OpenSSL 支持 Linux、BSD、Windows、Mac、VMS
等平台，这使其具有广泛的适用性。

近日，监测到 OpenSSL 官方发布了安全更新，修复了 OpenSSL
拒绝服务漏洞（CVE-2022-0778），OpenSSL 中的 BN_mod_sqrt ()
函数包含一个致命错误，攻击者可以通过构造特定证书来触发无限循环，由于证书解析发生在证书签名验证之前，因此任何解析外部提供的证书场景都可能实现拒绝服务攻击，目前，此漏洞细节及
PoC 已公开，威胁极大。

对此，建议广大用户做好资产自查以及预防工作，以免遭受黑客攻击。

.. _2-影响范围:

2、 影响范围
------------

受影响版本

l OpenSSL == 1.0.2

l OpenSSL == 1.1.1

l OpenSSL == 3.0

其他受影响组件：Ubuntu、Debian、Redhat、CentOS、SUSE 等平台均受影响。

不受影响版本

l OpenSSL == 1.0.2zd（仅限高级支持用户）

l OpenSSL == 1.1.1n

l OpenSSL == 3.0.2

.. _3-处置建议:

3、 处置建议
------------

通用修补建议：

目前，OpenSSL 官方已针对此漏洞发布修复版本，建议用户尽快升级至安全版本。

升级 OpenSSL
~~~~~~~~~~~~

OpenSSL 1.0.2 用户应升级到 1.0.2zd（仅限高级支持客户）

OpenSSL 1.1.1 用户应升级到 1.1.1n

OpenSSL 3.0 用户应升级到 3.0.2

注意：OpenSSL 1.1.0 版本及 OpenSSL 1.0.2
版本已停服，建议更新为最新版本。高级支持用户需要更新请联系官方：\ `www.openssl.org/support/contracts <www.openssl.org/support/contracts>`__....

其他主流平台升级
~~~~~~~~~~~~~~~~

使用了 OpenSSL 的其他平台如 Ubuntu、Debian、Redhat、CentOS、SUSE
均受此漏洞影响，具体受影响的平台版本及修复建议请参考如下官方说明：

（\ **1）Ubuntu**

`www.linux.org/threads/usn-5328-2-o <www.linux.org/threads/usn-5328-2-o>`__...

ubuntu.com/security/notices/USN-53...

（\ **2）Debian**

`www.debian.org/security/2022/dsa-5 <www.debian.org/security/2022/dsa-5>`__...

（\ **3）Redhat**

access.redhat.com/security/cve/cve...

（\ **4）SUSE**

`www.suse.com/security/cve/CVE-2022 <www.suse.com/security/cve/CVE-2022>`__...

| 4、 参考链接
| 1）\ `www.openssl.org/news/secadv/202203 <www.openssl.org/news/secadv/202203>`__...

2）\ `www.openssl.org/policies/secpolicy <www.openssl.org/policies/secpolicy>`__...

3）\ `www.linux.org/threads/usn-5328-2-o <www.linux.org/threads/usn-5328-2-o>`__...

4）ubuntu.com/security/notices/USN-53...

5）\ `www.debian.org/security/2022/dsa-5 <www.debian.org/security/2022/dsa-5>`__...

6）access.redhat.com/security/cve/cve...

7）\ `www.suse.com/security/cve/CVE-2022 <www.suse.com/security/cve/CVE-2022>`__...

.. _4升级到最新版本:

4、升级到最新版本
-----------------

.. code:: shell

   wget https://www.openssl.org/source/openssl-1.1.1n.tar.gz
   tar zxvf openssl-1.1.1n.tar.gz
   cd openssl-1.1.1n
   yum install gcc
   yum install perl-App-cpanminus.noarch
   ./config --prefix=/usr/local/openssl
   make && make install
   echo "/usr/local/lib64/" >> /etc/ld.so.conf
   ldconfig
   openssl version
   ln -s  /usr/local/openssl/bin/openssl /usr/bin/openssl

.. _5可能出现的问题:

5、可能出现的问题
-----------------

.. _解决报错libsslso11-cannot-open-shared-object-file-no-such-file-or-directory:

解决报错libssl.so.1.1: cannot open shared object file: No such file or directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   mv /usr/bin/openssl /usr/bin/openssl.old
   mv /usr/lib/openssl /usr/lib/openssl.old
   ln -s /usr/local/openssl/bin/openssl /usr/bin/openssl
   ln -s /usr/local/openssl/include/openssl /usr/include/openssl
   echo "/usr/local/openssl/lib" >> /etc/ld.so.conf
   ldconfig -v

.. _6ps:

6、PS
-----

服务器支持的话，最好升高版本吧

`opensll官方 <https://www.openssl.org/source/>`__
