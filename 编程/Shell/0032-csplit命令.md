# csplit命令

csplit命令可以根据上下文分割文件，如以下server log，想将3个server的log分割到3个文件中

```shell
> cat server.log
SERVER-1
[connection] 192.168.0.1 succes
[connection] 192.168.0.2 failed
[disconnect] 192.168.0.3 pending
[connection] 192.168.0.4 success
SERVER-2
[connection] 192.168.0.1 failed
[connection] 192.168.0.2 failed
[disconnect] 192.168.0.3 success
[connection] 192.168.0.4 failed
SERVER-3
[connection] 192.168.0.1 pending
[connection] 192.168.0.2 pending
[disconnect] 192.168.0.3 pending
```

csplit命令操作如下：

```shell
> csplit server.log /SERVER/ -n 2 -s {*} -f server -b '%02d.log'
> ls 
server00.log  server01.log  server02.log  server03.log  server.log
> cat server01.log
SERVER-1
[connection] 192.168.0.1 succes
[connection] 192.168.0.2 failed
[disconnect] 192.168.0.3 pending
[connection] 192.168.0.4 success
> cat server02.log
SERVER-2
[connection] 192.168.0.1 failed
[connection] 192.168.0.2 failed
[disconnect] 192.168.0.3 success
[connection] 192.168.0.4 failed
```

说明：

1. `/SERVER/`是整个表达式模式，`/REGEX/`。用来匹配特定的行，分割从此开始。每一个匹配会从匹配的当前行开始，一直到下一个匹配行(不包括)。结果里面server00.log为空，因为不包含第一行。
2. `{*}`用来表示重复分割直到文件末尾，也可以用数字指定分割次数：`{整数}`
3. `-s`表示静默模式，不打印其他信息
4. `-f`指定分割后文件的前缀
5. `-b`指定分割后文件的后缀，格式与C语言里的printf格式类似，文件名=前缀+后缀
6. `-n`指定分割后文件后缀的数字个数，有5之后这个可以省略