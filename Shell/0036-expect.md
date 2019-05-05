# expect

有时候一个命令行程序需要接收很多参数，让人记住全部参数及顺序会很不友好，这个时候通过`read -p`给出提示信息。如：想备份某个后缀文件备份文件夹，每次运行需指定后缀。

```shell
#!/bin/bash

read -p 'suffix: ' suffix

cp *.$suffix backup
```

如果参数太多，手动输入很麻烦，这个时候可以考虑自动化运行。有两种方式：

1. 将要输入的参数写入文件，每个参数一行，通过cat文件内容将参数传给命令
2. 使用expect

expect是一个解释器，有三个主要命令：

1. spawn：运行“目标程序”
2. expect：接收“目标程序”发出的模式
3. send：向目标程序发送字符串
4. interact：允许用户交互，如ssh登录后不退出

自动备份的expect程序如下：

```shell
#!/bin/expect

spawn sh backup.sh # 运行目标程序

expect {
	# 如果接收到suffix（*suffix*是一种模式：包含suffix的字符串）
    "*suffix*" {
    	# 发送
		send "png\n"
		exp_continue
    }
    # 如果接收到...
    ... {
    	...
    }
}
```

expect的一个常见应用就是ssh登录，例子参见：[ssh登录](../幸福小技巧/0001-mac-iterm2登录远程服务器.md)

