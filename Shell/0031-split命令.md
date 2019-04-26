# split命令

split命令可以用来分割文件

## 指定分割大小

`-b`选项是按字节分割，可以按k，G，M等分割

```shell
> $ ll -h
total 2.4M
-rw-r----- 1 luosen4 luosen4 2.4M Apr 24 21:08 data.file
> split -b 100k data.file # 以100k分割文件
> ls
data.file  xab  xad  xaf  xah  xaj  xal  xan  xap  xar  xat  xav  xax
xaa        xac  xae  xag  xai  xak  xam  xao  xaq  xas  xau  xaw  xay
```

## 数字后缀

split默认以字母为后缀，可以是用`-d`选项以数字为后缀，`-a`可以指定后缀长度：

```shell
> split -b 100k data.file  -a 4
> ls
data.file  xaaab  xaaad  xaaaf  xaaah  xaaaj  xaaal  xaaan  xaaap  xaaar  xaaat  xaaav  xaaax
xaaaa      xaaac  xaaae  xaaag  xaaai  xaaak  xaaam  xaaao  xaaaq  xaaas  xaaau  xaaaw  xaaay
> split -b 100k data.file -d -a 4
> ls
data.file  x0001  x0003  x0005  x0007  x0009  x0011  x0013  x0015  x0017  x0019  x0021  x0023
x0000      x0002  x0004  x0006  x0008  x0010  x0012  x0014  x0016  x0018  x0020  x0022  x0024
```

## 指定前缀

split之后的文件默认以x为前缀，可以指定前缀：

```shell
> split -b 100k data.file -d -a 4 split_file.
> ls
data.file        split_file.0004  split_file.0009  split_file.0014  split_file.0019  split_file.0024
split_file.0000  split_file.0005  split_file.0010  split_file.0015  split_file.0020
split_file.0001  split_file.0006  split_file.0011  split_file.0016  split_file.0021
split_file.0002  split_file.0007  split_file.0012  split_file.0017  split_file.0022
split_file.0003  split_file.0008  split_file.0013  split_file.0018  split_file.0023
```

## 按行数分割

`-l`选项可以按行数分割

```shell
> split -l 1000 data.file
> ls
data.file  xaa  xab  xac  xad  xae  xaf  xag  xah  xai  xaj  xak  xal  xam  xan  xao  xap  xaq  xar  xas
> wc -l xaa
1000 xaa
```



