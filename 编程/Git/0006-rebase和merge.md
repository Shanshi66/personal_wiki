# rebase和merge

rebase和merge都可以合并分支，但是合并方式不一样，导致合并之后之后的提交记录不一样

对于两个分支：

![](img/0006-1.png)

merge之后的两个分支的提交记录会分开保存：

![](img/0006-2.png)

rebase之后提交记录合并为一条线：

![](img/0006-3.png)

一般，在topic分支中更新merge分支的最新代码，使用rebase。向merge分支导入topic分支，先使用rebase，再使用merge。

> merge分支是指要发布稳定版本的分支，topic分支是功能分支，如：修bug，加功能等