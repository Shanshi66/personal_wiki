# static

static可以修饰变量，也可以修饰函数。
1. 静态变量在全局数据区分配内存，参见[程序内存分布](../基础知识/0001-内存的栈与堆.md)
2. 静态局部变量在程序执行到该对象的声明处时被首次初始化，以后的函数调用不再进行初始化。程序结束时释放内存。(同全局变量一致)
3. 静态局部变量一般在声明处初始化，类静态成员在类外初始化
4. **静态局部变量的作用域为局部作用域，同全局变量不一样，这也是static的优势，可以进行作用域隔离，包括函数作用域、文件作用域等。**
5. 实例占用内存不包含静态成员变量
6. 静态成员函数不能访问非静态成员函数和数据

```c++
static int n = 1; // 静态全局变量

int foo() {
    static int local = 3; // 静态局部变量
}

class Circle final
{
private:
    static double PI; // 静态成员
    double radiu;
public:
    Circle(double r): radiu(r){}
    double area()
    {
        return PI*radiu*radiu;
    }
    static double get_pai() { // 静态成员函数
        return PI;
    }
};

double Circle::PI = 3.14; // 静态成员初始化

int main() {
    Circle c(3);
    cout << c.area() << endl;
    cout << Circle::get_pai() << endl;
    cout << c.PI << endl;
}
```

