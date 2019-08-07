# cherry-pick

cherry-pick可以将某个分支的某一个commit合并到当前分支的head

```shell
$ git cherry-pick <commit-id>
```

需要注意的是，如果<commit-id>是merge产生的，cherry-pick会报错，因为<commit-id>有两个父亲。

```shell
$ git cherry-pick a8c5ad438f6173dc34f6ec45bddcef2ab23285e0
error: Commit a8c5ad438f6173dc34f6ec45bddcef2ab23285e0 is a merge but no -m option was given.
fatal: cherry-pick failed
```

git cherry-pick其实做了两件事：

1. 找到<commit-id>和它父亲之间的变化
2. 将这些变化应用到当前分支

如果有两个父亲，git就不知道该使用哪些change了，因此需要使用`-m`选项指定父亲。

```shell
$ git cherry-pick <commit-id> -m 1
```

`-m`后面接着parent的序号，顺序和`git show`中展现的一样



参考：

https://stackoverflow.com/questions/12626754/git-cherry-pick-syntax-and-merge-branches/12628579#12628579

https://backlog.com/git-tutorial/cn/stepup/stepup7_4.html

https://stackoverflow.com/questions/9229301/git-cherry-pick-says-38c74d-is-a-merge-but-no-m-option-was-given