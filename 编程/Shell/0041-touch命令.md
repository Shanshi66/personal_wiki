# touch命令

touch命令可以生成一个空白文件或是修改以有文件的时间戳。

```shell
> touch blank_file.txt
```

如果blank_file.txt不存在，会创建blank_file.txt。如果blank_file.txt存在，会修改该文件相关所有时间戳为当前时间。

也可以指定要修改的时间类型：

- touch -a 只更改文件的访问时间
- touch -m 只更改文件的修改时间

也可以将时间戳更改为指定时间

```shell
> touch -d '2019-01-02' blank_file.txt
> ll blank_file.txt
-rw-r----- 1 luosen4 luosen4 0 Jan  2 00:00 blank_file.tx
```



