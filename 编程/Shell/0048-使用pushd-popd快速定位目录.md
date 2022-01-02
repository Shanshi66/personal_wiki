# pushd-popd

当我们需要频繁地在多个目录之间切换时，可以pushd和popd命令。pushd会将当前目录压入一个栈内，popd会弹出栈内目录。

```shell
> pushd learning # 进入learning目录，并将路径压入栈内
~/learning ~ ~ ~/learning/shell

> pushd shell # 进入shell目录
~/learning/shell ~/learning ~ ~ ~/learning/shell

> dirs # 显示栈内目录 
~/learning/shell ~/learning ~ ~ ~/learning/shell

> pushd +1 # 栈内目录从左往右从0~n，进入1号目录，即~/learning
> pwd
/home/luosen4/learning

> dirs
~/learning ~ ~ ~/learning/shell ~/learning/shell 

> popd # 删除栈顶目录
~ ~ ~/learning/shell ~/learning/shell

> popd +2 # 删除2号目录
~ ~ ~/learning/shell
```

如果只有两个目录要切换，可以使用`cd -`，这个命令会在当前目录和上一个目录之间切换

