# mktemp命令

有时候想创建临时文件或目录，但是想保持用户目录整洁，可以使用mktemp命令。这个命令会在`/tmp`目录下创建文件或目录，`/tmp`目录每次机器重启都会清空。

## 创建临时文件

```shell
> filename=`mktemp`
> echo $filename
/tmp/tmp.7U5bygz9Hn
```

## 创建临时目录

```shell
> dirname=`mktemp -d`
> echo $dirname
/tmp/tmp.kak8riPHPp
> ll /tmp/tmp.kak8riPHPp/
total 0
```

## 只生成文件或目录名字

```shell
> tmpfile=`mktemp -u`
> echo $tmpfile
/tmp/tmp.Qu6m91JsGJ
> ll /tmp/tmp.Qu6m91JsGJ
ls: cannot access /tmp/tmp.Qu6m91JsGJ: No such file or directory
```

## 根据模板生成名字

```shell
> tmpfile=`mktemp test.XXX` # 模板中至少要保证有3个X
> echo $tmpfile
test.aAB
```

