# auto

**在编译阶段**，让编译器自动进行类型推导。只能在初始化阶段生效，但有些场合推导不出来。另外类成员不允许使用auto初始化。

```c++
auto  i = 0;          // 自动推导为int类型
auto  x = 1.0;        // 自动推导为double类型

auto  str = "hello";  // 自动推导为const char [6]类型

std::map<int, std::string> m = {{1,"a"}, {2,"b"}};  // 自动推导不出来
auto c = {1,2,3,4}; // 推导不出来

auto  iter = m.begin();  // 自动推导为map内部的迭代器类型

auto  f = bind1st(std::less<int>(), 2);  // 自动推导出类型，具体是啥不知道

class Test {
public:
    auto a = 0;  // 不行
}

```

auto可以让代码更简洁，也能避免对类型硬编码。比如将map类型改成unordered_map不用改代码。

**注意**:
1. auto只会推导出值类型，不会推导出引用
2. auto可以附加上const、volatile、*、&这样的类型修饰符，得到新的类型。

```c++
auto        x = 10L;    // auto推导为long，x是long
auto&       x1 = x;      // auto推导为long，x1是long&
auto*       x2 = &x;    // auto推导为long，x2是long*
const auto& x3 = x;        // auto推导为long，x3是const long&
auto        x4 = &x3;    // auto推导为const long*，x4是const long*

```

在for中使用auto
```c++
vector<int> v = {2,3,5,7,11};  // vector顺序容器

for(const auto& i : v) {      // 常引用方式访问元素，避免拷贝代价
    cout << i << ",";          // 常引用不会改变元素的值
}

for(auto& i : v) {          // 引用方式访问元素
    i++;                      // 可以改变元素的值
    cout << i << ",";
}
```

函数返回值使用auto(C++14)

```c++
auto get_a_set()              // auto作为函数返回值的占位符
{
    std::set<int> s = {1,2,3};
    return s;
}
```

# decltype

也是在编译截断生效，从表达式推导出类型

```c++
int x = 0;          // 整型变量
decltype(x)     x1;      // 推导为int，x1是int
decltype(x)&    x2 = x;    // 推导为int，x2是int&，引用必须赋值
decltype(x)*    x3;      // 推导为int，x3是int*
decltype(&x)    x4;      // 推导为int*，x4是int*
decltype(&x)*   x5;      // 推导为int*，x5是int**
decltype(x2)    x6 = x2;  // 推导为int&，x6是int&，引用必须赋值
```

**decltype可以推导值类型，也可以推导出引用类型**，完全可以把decltype看做是一个类型名：

```c++
using int_ptr = decltype(&x);    // int *
using int_ref = decltype(x)&;    // int &
```

C++14之后，decltype和auto可以联合使用：
```c++

int x = 0;            // 整型变量
decltype(auto)     x1 = (x);  // 推导为int&，等同于decltype(x)
decltype(auto)     x2 = &x;   // 推导为int*，等同于decltype(&x)
decltype(auto)     x3 = x1;   // 推导为int&，等同于decltype(x1)
```

代替特别复杂的类型：
```c++

class DemoClass final
{
public:
    using set_type      = std::set<int>;  // 集合类型别名
private:
    set_type      m_set;                   // 使用别名定义成员变量

    // 使用decltype计算表达式的类型，定义别名
    using iter_type = decltype(m_set.begin());

    iter_type     m_pos;                   // 类型别名定义成员变量
};

```