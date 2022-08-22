# Pycharm reStructuredText 帮助文件中文乱码



在使用 IntelliJ 对 reStructuredText 文件进行编辑的时候。

我们可能会遇到乱码的情况。

如下图：

![image-20220731230155376](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220731230155376.png)

可以看到，我们在使用 IntelliJ 的时候中文是乱码的。

这里有几个地方是需要修改的，首先你需要修改你的项目使用的是 UTF-8 编码。

Ctrl + Alt + S 进入设置，然后选择 Editor > File Encodings

你需要将你的全局设置，项目编码都设置成 UTF-8，如果你使用的是中文操作系统，可能这里默认设置是 GBK，不要使用 GBK。



![image-20220731230211087](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220731230211087.png)



然后重启你的 IntelliJ， 你可能会发现你的修改没有生效。

这是因为 reStructuredText 的插件使用了 Java 的 JavaFX 或者 Swing，这在默认情况下是不支持 UTF-8 的。

你需要对 IntelliJ 的启动参数进行设置。

选择帮助下面的修改自定 VM 选项。

![image-20220731230221358](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220731230221358.png)

在文件的最后添加

```
-Dfile.encoding=UTF-8A
```

这个表示的是在 IntelliJ 启动的时候，我们将 VM 的启动参数强制使用 UTF-8 编码。

![image-20220731230229546](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220731230229546.png)

在完成上面的修改后，重启你的 IntelliJ，然后在对文件进行对比查看。

你可以看到你的 IntelliJ 已经能够支持中文了。

![image-20220731230243174](https://raw.githubusercontent.com/T-hree/Blog_img/main/img/image-20220731230243174.png)

