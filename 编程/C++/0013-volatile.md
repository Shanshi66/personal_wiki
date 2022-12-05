# volatile

volatile修饰的变量表示不稳定的，变量的值可能会以“难以察觉”的方式被修改（比如操作系统信号、外界其他的代码），所以禁止编译器做任何形式的优化。

比如const volatile变量就有可能被改变。

volatile是一种危险的操作，尽量少用。


```c++
const volatile int MAX_LEN  = 1024;

auto ptr = (int*)(&MAX_LEN);
*ptr = 2048; // 通过指针强制写入
cout << MAX_LEN << endl;      // 输出2048
```