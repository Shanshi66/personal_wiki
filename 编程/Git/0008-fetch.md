# fetch

可以使用fetch命令拉取远程分支，但是这会将远程修改与本地修改合并，如果不想合并，可以使用fetch命令。fetch会将远程修改存在一个无名分支，`FETCH_HEAD`指向头部，本地代码不会修改。

如果想继续同步，可以使用

```
git pull
git merge FETCH_HEAD
```

