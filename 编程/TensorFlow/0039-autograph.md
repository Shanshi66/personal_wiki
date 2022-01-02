# autograph

Autograph机制可以将动态图转换成静态计算图，兼收执行效率和编码效率之利

## 编码规范

1. 被`@tf.function`修饰的函数应尽可能使用TensorFlow中的函数而不是Python中的其他函数。例如使用`tf.print`而不是`print`，使用`tf.range`而不是`range`，使用`tf.constant(True)`而不是True.

```python
@tf.function
def tf_random():
    a = tf.random.normal((3,3))
    tf.print(a)
```

2. 避免在`@tf.function`修饰的函数内部定义`tf.Variable`.

```python
x = tf.Variable(1.0,dtype=tf.float32)
@tf.function
def outer_var():
    x.assign_add(1.0)
    tf.print(x)
    return(x)

outer_var() 
outer_var()
```

3. 被`@tf.function`修饰的函数不可修改该函数外部的Python列表或字典等数据结构变量。

```python
tensor_list = []

@tf.function #加上这一行切换成Autograph结果将不符合预期！！！
def append_tensor(x):
    tensor_list.append(x)
    return tensor_list


append_tensor(tf.constant(5.0))
append_tensor(tf.constant(6.0))
print(tensor_list)

# [<tf.Tensor 'x:0' shape=() dtype=float32>]
```

## autograph过程

```python
import tensorflow as tf
import numpy as np 

@tf.function(autograph=True)
def myadd(a,b):
    for i in tf.range(3):
        tf.print(i)
    c = a+b
    print("tracing") # 不是tf.print
    return c

myadd(tf.constant("hello"),tf.constant("world"))
# =>
# tracing
# 0
# 1
# 2

myadd(tf.constant("good"),tf.constant("luck")) 
# => 不会输出tracing
# 0
# 1
# 2

myadd(tf.constant(1),tf.constant(2))
# =>
# tracing 又有了
# 0
# 1
# 2

myadd(1, 2)
# =>
# tracing 又有了
# 0
# 1
# 2

myadd(1, 2)
# =>
# tracing 还是有
# 0
# 1
# 2

@tf.function(autograph=True)
def myadd(a,b):
    for i in tf.range(3):
        tf.print(i)
    c = a+b
    tf.print("tracing") # !!
    return c

myadd(tf.constant("hello"),tf.constant("world"))
# =>
# 0
# 1
# 2
# tracing

```

autograph执行过程：
1. 先执行python代码，创建计算图，因此python代码中的输出会先打印。
   1. 函数里tf的算子会加到计算图里，因此最好都使用tf算子。
   2. 不同类型的输入，会重新建图。如果传入的参数不是tensor，每次都会创建计算图
   3. 创建变量只会在创建计算图的时候执行一次，因此不要在函数内定义变量
   4. python的数据结构如list、dict不会传给C++代码创建的计算图，因此不要修改python代码的外部数据结构
2. 执行计算图，计算图创建好之后，将不会执行python代码


## tensorboard追踪

```python
import datetime

# 创建日志
stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
logdir = './data/demomodule/%s' % stamp
writer = tf.summary.create_file_writer(logdir)

#开启autograph跟踪
tf.summary.trace_on(graph=True, profiler=True) 

#执行autograph
demo = DemoModule(init_value = tf.constant(0.0))
result = demo.addprint(tf.constant(5.0))

#将计算图信息写入日志
with writer.as_default():
    tf.summary.trace_export(
        name="demomodule",
        step=0,
        profiler_outdir=logdir)
```





