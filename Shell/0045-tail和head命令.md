# tail和head命令

```shell
> head <file-name> # 打印文件前10行
> head -n N <file-name> # 打印文件前N行
> head -n -N <file-name> # 打印文件除最后N行外的所有行

> tail <file-name> # 打印文件最后10行
> tail -n N <file-name> # 打印文件最后N行
> tail -n +(N+1) <file-name> # 打印文件除最开始N行外的所有行
> tail -f <file-name> # 跟踪file-name
> tail -f <file-name> -pid <PID> # 进程结束后tail命令自动结束
```

