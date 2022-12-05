# mutable

mutable只用来修饰类成员变量，修饰之后的变量const成员函数也可以改变，即使本身是const对象。

看起来有点像给const用法打了一个补丁。引入 mutable 之后，C++ 可以有逻辑层面的 const，也就是对一个常量实例来说，从外部观察，它是常量而不可修改；但是内部可以有非常量的状态。

```c++
class DemoClass final
{
private:
    mutable int a = 0;    // mutable成员变量
public:
    void save_data() const          // const成员函数
    {
        a = 10;
    }
    void print() const
    {
        cout << a << endl;
    }
};

int main() {
    const DemoClass demo;
    demo.save_data();
    demo.print(); // 输出10
}

```