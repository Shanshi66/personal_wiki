# future模块

`__future__`模块将python新版本中的一些功能反向迁移到旧版本中，采用的是导入语句的形式

```python
from __future__ import <feature> # 引入的feature不需要调用，特性自动生效
```

这个语句只能影响它所在的模块

python2中的__future__模块的功能：

1. division： python3的除法运算符

2. absolute_import：将所有不以点字符开头的import语句格式解释为绝对导入

3. print_function：将print语句变为函数调用

4. unicode_literals: 将每个字符串解释为Unicode