# string

## 一般用法

// TODO

## 新标准特性

### 字面量后缀(C++14)

在字符串字面量后面加上后缀s，明确地表示它是 string 字符串类型，而不是 C 字符串，这就可以利用 auto 来自动类型推导

```c++
using namespace std::literals::string_literals; //必须打开名字空间
auto str = "std string"s; // 后缀s，表示是标准字符串，直接类型推导
assert("time"s.size() == 4); // 标准字符串可以直接调用成员函数
```

### 原始字符串

C++11 还为字面量增加了一个"原始字符串"（Raw string literal）的新表示形式，类似python中的raw字符串，不需要对一些符号进行转义。

```c++
auto str = R"(nier:automata)";  // 原始字符串：nier:automata
auto str1 = R"(char""'')";      // 原样输出：char""''
auto str2 = R"(\r\n\t\")";      // 原样输出：\r\n\t\"
auto str3 = R"(\\\$)";          // 原样输出：\\\$
auto str4 = "\\\\\\$";          // 转义后输出：\\\$
auto str5 = R"==(R"(xxx)")==";  // 原样输出：R"(xxx)"，可以在括号两边加最多16个字符的界定符，可以是任意字符
```

### 字符串转换函数

C++11新增了几个新的字符串转换函数，参数是string，而不是C字符串。

- stoi()、stol()、stoll() 等把字符串转换成整数；
- stof()、stod() 等把字符串转换成浮点数；
- to_string() 把整数、浮点数转换成字符串

```c++
assert(stoi("42") == 42);          // 字符串转整数
assert(stol("253") == 253L);       // 字符串转长整数
assert(stod("2.0") == 2.0);       // 字符串转浮点数
assert(to_string(1984) == "1984");       // 整数转字符串
```

### 字符串视图

string本质是`vector<char>`，如果字符串太长，修改、复制成本很高，C++17中新增字符串视图(string_view),内部只保存一个指针和长度，无论是拷贝，还是修改，都非常廉价。

//TODO


## 正则表达式

C++11新增正则表达式库regex，利用它的强大能力，你就能够任意操作文本、字符串。弥补C++字符串处理的短板。

//TODO

