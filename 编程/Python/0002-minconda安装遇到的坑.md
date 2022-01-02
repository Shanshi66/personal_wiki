# minconda安装遇到的坑

在公司堡垒机上安装了miniconda，conda init的时候遇到需要sudo密码的问题。

conda init命令需要向.bashrc文件里写代码，但是.bashrc文件的权限被限制了，不能修改，个人自定义环境变量只能写在.bash_profile。

解决方法是将conda写入的代码从网上拷贝一份写到.bash_profile里。这里有一份：

```shell
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
if [ 1 -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/home/luosen4/miniconda3/etc/profile.d/conda.sh" ]; then
       . "/home/luosen4/miniconda3/etc/profile.d/conda.sh"
       CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/home/luosen4/miniconda3/bin:$PATH"
    fi
fi
# unset __conda_setup
# <<< conda init <<<"
```

参考自：

https://github.com/ContinuumIO/anaconda-issues/issues/10173