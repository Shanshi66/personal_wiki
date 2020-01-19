# checkout

1. `git checkout [--] <file>`

   用暂存区的内容覆盖工作区，不改变HEAD

2. `git checkout <commit-id> [--] <file>` 

   用指定commit-id的文件覆盖当前文件，不改变HEAD

3. `git checkout [-f(强制)] <commit-id>`

   切换到指定commit-id上，切换成功会处于”分离头指针“状态

4. `git branch <branch> <commit-id>`

   以某个commit创建分支

5. `git checkout -datch <branch>`

   切换到游离分支状态，指向当前分支的最后一次提交

6. `git checkout -B <branch>`

   强制创建分支，会覆盖同名分支

7. `git checkout --orphan <branch>`

   如果当前分支提交历史太乱，可以复制当前分支内容，创建一个空log分支

8. `git checkout -p [<file>] <branch>`

   将当前你分支与指定分支进行比较，通过交互式界面可以选择将指定分支的修改应用于当前分支