# 支持多个ssh key

如果多个人共用一台机器，每个人需要单独有一个ssh key，ssh默认的ssh key是`./ssh/id_rsa`，其他的ssh key不会被识别，这时候可以通过如下方式添加：

```shell
$ eval $(ssh-agent -s)
$ ssh-add ~/.ssh/your_rsa_key # 添加你的密钥
```

