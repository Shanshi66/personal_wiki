# Python编程规范

1. PEP8为编写python代码提供了一个风格指南
2. 比遵守PEP8更重要的是项目内的一致性


## 命名风格

1. 对于常量全局变量，使用大写加下划线

2. 大部分情况下，缩写名称都会是代码含义变得模糊。如果缩写不够清晰，不要害怕使用完整的单词

3. 使用常量的另一个好的做法是将他们集中放在模块顶部，或者集中放在包中的一个文件内

4. 可以使用enum模块中的Enum类创建一组常量

   ```python
   from enum import Enum
   
   class Color(Enum):
       YELLOW = 1
       RED = 2
       GREEN = 3
       FAKE_YELLOW=1
   
   print(Color.YELLOW)
   print(Color.YELLOW.value)
   print((Color.YELLOW == 1))
   print((Color.YELLOW == Color.YELLOW))
   print((Color.YELLOW == Color.RED))
   print((Color.YELLOW == Color.FAKE_YELLOW))
   
   ==>
   Color.YELLOW
   1
   False
   True
   False
   True
   ```

5. 对于可变的且可以通过导入自由访问的全局变量，如果他们需要被保护，那么应该使用一个带一个下划线的小写字母，通常需要提供getter和setter

6. 函数和方法的名称应该使用小写加下划线，对于私有方法和函数，惯例是添加一个前缀下划线。

7. 以双下划线开始和结束的特殊方法应集中在类定义的开头，对于常规方法而言，不要使用这种方式命名

8. 参数名称使用小写，如果需要的话可以加下划线，与变量命名规则相同

9. property的名称使用小写或小写加下划线

10. 类名称始终采用驼峰式命名法，如果他们是模块的私有类，最好加个前缀下划线

11. 模块名称都使用小写，不带下划线(除init模块外)，如果模块是包的私有模块，加个下划线。包遵循和模块相同的规则。

## 命名指南

1. 使用has或is前缀命名布尔元素

2. 使用复数形式命名集合变量

3. 使用显式名称命名字典，如`persons_addresses = {'Bill': '6565 Monty Road'}`

4. 避免通用名称：如list，compute，tools，utils等。任何没有对其内容给出任何信息的名称，从长远看都对项目有很大害处。

5. 在大多数情况下，更多的小模块总是更好，即使内容很少，但名称可以很好地反映其内容

6. 使用现有名称不是个好的做法

7. 对于关键字，后缀下划线是一个避免冲突的方法，如`or_`，class通常被替换为kclass或cls

8. 类的名称必须简明、精确，容易理解。可以使用后缀表示其类型或特性。如：

   1. SQLEngine
   2. TestCase

   对于基类，可以使用一个Base或者Abstract前缀

   1. BaseCookie
   2. AbstractFormmatter

9. 模块和包的名称应体现其内容的目的，其名称应简短、小写、不带下划线，如

   1. postgres
   2. sha1

   ```python
   from widgets.stringwidgets import TextWidget
   from widgets.strings import TextWidget # better, simple
   ```

10. 如果一个模块类太多，可以创建一个包将类划分到不同模块中，将API放到`__init__`模块中

    ```python
    # foo包__init__.py
    from .module1 import feature1, feature2
    from .module2 import feature3
    
    # other py
    from foo import feature1, feature2, feature3 # 可直接导入
    ```

    

## 参数的最佳实践

1. 通过迭代设计构建参数。如果添加一些参数，他们应该尽可能有默认值，避免退化。
2. 契约式设计(Design by Contract, DbC)：可以使用assert在函数开始进行断言，执行的时候加`-O`进行过滤。
3. 最好是通过测试驱动开发(TDD)创建高鲁棒性代码。
4. 小心使用`*args`和`**kwargs`，可变参数会让函数签名变得模糊。可以使用容器(如list)或容器类(用key-word类替代`**kwargs`)代替。

## 工具

1. pylint：源代码分析器
2. pep8和flake8：小型代码风格检查器

