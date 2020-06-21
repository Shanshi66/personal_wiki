# python设计模式

3类设计模式：

- 创建型模式：用于生成具有特定行为的对象，如工厂模式，单例模式
- 结构型模式：有助于为特定用例构建代码，如适配器模型，代理模型，外观模式
- 行为模式：有助于分配责任和封装行为，如观察者模式、访问者模式



## 创建型模式

### 单例模式

**实现方式一**

可以通过自定义`__new__`函数实现，返回同一个类。这种方法在继承的时候有问题，如下面例子。

```python
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

class ConcreteClass(Singleton):
    pass


b = Singleton()
print(id(b))

a = ConcreteClass()
print(id(a))
==>
4454753104
4454753104

----

a = ConcreteClass()
print(id(a))

print(ConcreteClass.__dict__['_instance'])
print(Singleton.__dict__['_instance']) # 父类dict还是None

b = Singleton() # 还会重新_instance创建实例
print(id(b))

==>

4459955024
<__main__.ConcreteClass object at 0x107d81690>
None
4459955088

```

当出现以上问题的时候错误比较难查。而且上面的方式不好拓展，当有多个不同功能的类需要单例的时候，需要重复定义单例类。

**实现方式二**

更安全先进的方式是使用元类

```python
class Singleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]

class ConcreteSingleton(metaclass=Singleton):
    pass

class SubConcreteSingleton(ConcreteSingleton):
    pass



b = ConcreteSingleton()
print(id(b))

a = ConcreteSingleton()
print(id(a))

c = SubConcreteSingleton()
print(id(c))

d = SubConcreteSingleton()
print(id(d))

==>
4528710544
4528710544
4528710608
4528710608
```

**实现方式三**

单例的本质是共享相同的状态，所以所有实例共享一个dict也可以看做是单例

```python
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob
      
a = Borg()
a.var = 1
print(a.__dict__)
b = Borg()
print(b.__dict__)

==>
{'var': 1}
{'var': 1}
```

**实现方式四**

将单例作为一个模块级变量，因为模块是单例的



## 结构型模式

### 适配器模式

> 如果它走路像鸭子，说话像鸭子，那它就是鸭子

即，如果类A不支持类B的操作，可以通过某种方式让A适配B

```python
class Article(object):
    def summary(self, article):
        print('Title: {}'.format(article['title']))


class ArticleAdapter(object): #将一个字符串模拟成一个article
    def __init__(self, sentence):
        self._sentence = sentence

    @property
    def title(self): # 适配title字段
        return self._sentence

    def __getitem__(self, item): # 适配字典操作
        return getattr(self, item, 'Unknown')

adapter = ArticleAdapter('title-1')

article = Article()
article.summary(adapter)
```

### 代理

> Client --> Proxy --> Subject

proxy用来优化昂贵subject的访问。例如，如果只需要知道网页的header信息，我们没必要读取整个网页。

```python
from urllib.request import urlopen

class Url(object):
    def __init__(self, url):
        self._url = urlopen(url)

    def header(self):
        return dict(self._url.headers.items())

    def get(self):
        return self._url.read()

baidu = Url('http://www.baidu.com')
print(baidu.header())
print(baidu.get())
```

使用代理的另一个好处是数据唯一性，对于同一个资源，可以使用多个代理，当资源发生变化时，所以代理都能感知到，代理之间不用进行版本同步。

### 外观

**外观是高级功能的快捷方式**

可以在`__init__.py`模块中提供一个函数，这个函数里通过调用模块中其他组件提供一个高级功能，使得调用方不用感知模块底层的复杂性



## 行为模式

### 观察者模式

观察者模式用于通知列表中的对象关于被观察组件的状态改变，常见于事件驱动编程。

```python
class Event(object):
    _observers = []
    def __init__(self, subject):
        self._subject = subject

    @classmethod
    def register(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def unregister(cls, observer):
        if observer in cls._observers:
            cls._observers.remove(observer)

    @classmethod
    def notify(cls, subject):
        event = cls(subject)
        for observer in cls._observers:
            observer(event)


class WriteEvent(Event): # write事件
    def __repr__(self):
        return 'WriteEvent'

def logObserver(event):
    print(
        'logObserver: {} was notified with subject {}'.format(event, event._subject)
    )

class AnotherObserver(object):
    def __call__(self, event):
        print(
            'AnotherObserver: {} was notified with subject {}'.format(event, event._subject)
        )

WriteEvent.register(logObserver) # write事件有很多观察者
WriteEvent.register(AnotherObserver())

WriteEvent.notify('something happened') # write事件发生了某个主题的变化
```

### 访问者模式

访问者模式可以帮助分离算法和数据结构：

- 一个类保存数据结构，提供算法类的接入口
- 算法在其他类中

```python
class VisitableList(list):
    def accept(self, visitor): # 算法类接入口
        visitor.visit_list(self)

class VisitableDict(dict):
    def accept(self, visitor):
        visitor.visit_dict(self)

class Printer(object):
    def visit_list(self, instance):
        print('list content: {}'.format(instance))
    def visit_dict(self, instance):
        print('dict content: {}'.format(instance))

p = Printer()
list_example = VisitableList(['1', '2'])
dict_example = VisitableDict({'1': 1, '2':2})
list_example.accept(p)
dict_example.accept(p)

# 为重复写accept麻烦，可利用python语言特点动态绑定
def visited(data, visitor):
    cls = data.__class__.__name__
    method_name = '{}_{}'.format('visit', cls)
    method = getattr(visitor, method_name, None)
    if isinstance(method, Callable):
        method(data)
    else:
        print('invalid visitor')
 
==>
list content: ['1', '2']
dict content: {'1': 1, '2': 2}
list content: [1, 2, 3]
```

