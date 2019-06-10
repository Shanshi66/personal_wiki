# paste命令

parse命令可以按列将文件合并在一起，默认以制表符隔开，可以指定分隔符

```shell
> cat file1.txt
1
2
3
4
5
> cat file2.txt
welcome
to
beijing
> paste file1.txt file2.txt
1	welcome
2	to
3	beijing
4
5
> paste -d "," file1.txt file2.txt
1,welcome
2,to
3,beijing
4,
5,
```



