# dos2unix

在windows上编写一个shell脚本后，使用rz上传到服务器，发现文件中出现一堆`\r`，这是因为windows和linux处理换行的方式不一样。linux换行只有`\n`，windows下有`\r\n`。

可以使用dos2unix命令将windows文件转为unix文件:

```
dos2unix <filename>
```