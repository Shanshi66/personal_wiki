# python2中的编码问题

## 文件编码

python2中默认的文件编码是ASCII吗，所以如果文件中有中文，会报错。这个时候需要在文件前面加上

```shell
# -*- coding:utf-8 -*-
```

或者其他符合`coding[:=]\s*([-\w.]+) `正则表达式的其他语句。

## str和unicode

python中的字符串有两种类型：str和unicode，str的编码格式在不同设备和环境中可能不同，如在window cmd的解释器中默认是gbk， 在linux shell解释器中默认是utf-8。unicode字符串的编码格式是unicode。

```shell
# linux
>>> a = '编码'
>>> chardet.detect(a)
{'confidence': 0.7525, 'language': '', 'encoding': 'utf-8'}
```

str类型字符串可以通过decode转为unicode字符串，参数为str的编码格式：

```shell
>>> b = a.decode('utf-8')
>>> b
u'\u7f16\u7801'
>>> type(b)
<type 'unicode'>
```

unicode字符串可以通过encode转为str类型：

```shell
>>> c = b.encode('utf-8')
>>> c
'\xe7\xbc\x96\xe7\xa0\x81'
>>> type(c)
<type 'str'>
```

## 格式互转

使用python2进行格式互转的时候很容易出错，比如将上面的a转为gbk编码：

```shell
>>> a.encode('gbk')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
```

python2中编码格式转换都是通过unicode转的，上面代码中a是utf-8类型，要转成gbk，首先要将a转成unicode，然后再转成gbk。因此正确的做法是：

```shell
>>> a.decode('utf-8').encode('gbk')
'\xb1\xe0\xc2\xeb'
```

decode这一步python2是默认帮我们做的，但是它默认用的类型不是`utf-8`而是ascii，所以才会报上面的错。

```shell
>>> sys.getdefaultencoding()
'ascii'
```

如果要想缺省decode这一步，可以为设置默认的解码格式：

```shell
>>> sys.setdefaultencoding('utf-8')
>>> a.encode('gbk')
'\xb1\xe0\xc2\xeb'
```



参考文章：

https://blog.csdn.net/u014591781/article/details/78415044

https://www.zhihu.com/question/31833164