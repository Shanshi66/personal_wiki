# property

property是一个内置的描述符类型，省去自己定义，接收4个可选参数：

- fget：获取属性
- fset：设置属性
- fdel：删除属性
- doc：属性的doc

```python
class Value:
    def __init__(self, val):
        self._val = val

    def _value_get(self):
        return self._val

    def _value_set(self, val):
        self._val = val

    def _value_del(self):
        self._val = -1

    val = property(_value_get, _value_set, _value_del, doc = 'value')


val = Value(10)
print(val.val)
val.val = 100
print(val.val)
del val.val
print(val.val)

==>
10
100
-1
```

在使用继承的时候，子类需要重写整个property，只重写部分方法，无法影响property

```python
class ValueSon(Value):
    def _value_get(self):
        return self._val-1

val = ValueSon(10)
print(val.val)
```

python提供了内置的property装饰器，可以避免上述问题，而且更加方便

```python
class Value:
    def __init__(self, val):
        self._val = val

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        self._val = value


val = Value(10)
print(val.val)
val.val = 20
print(val.val)

==>
10
20
```

