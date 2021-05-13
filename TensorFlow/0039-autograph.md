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




