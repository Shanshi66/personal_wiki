# 特征

特征类似java中的接口，具备什么样的特征，就可以支持什么样的行为

## 定义与使用

```rust

pub trait Summary {
    fn summarize(&self) -> String;
}
pub struct Post {
    pub title: String, // 标题
    pub author: String, // 作者
    pub content: String, // 内容
}

impl Summary for Post { //
    fn summarize(&self) -> String {
        format!("文章{}, 作者是{}", self.title, self.author)
    }
}

pub struct Weibo {
    pub username: String,
    pub content: String
}

impl Summary for Weibo {
    fn summarize(&self) -> String {
        format!("{}发表了微博{}", self.username, self.content)
    }
}

fn main() {
    let post = Post{title: "Rust语言简介".to_string(),author: "Sunface".to_string(), content: "Rust棒极了!".to_string()};
    let weibo = Weibo{username: "sunface".to_string(),content: "好像微博没Tweet好用".to_string()};
    
    println!("{}", post.summarize());
    println!("{}", weibo.summarize());
}
```

- trait: 关键字
- Summary: 特征名
- summarize: 方法，不定义具体怎么实现，在具体类定义的时候在会具体定义实现方法
- 关于特征实现与定义的位置，有一条非常重要的原则（孤儿规则）：如果你想要为类型 A 实现特征 T，那么 A 或者 T 至少有一个是在当前作用域中定义的！确保你不会改别人代码，别人也不会改你代码。
- pub：别人可以在他们的包中使用该特征
- 如果你要使用一个特征的方法，那么你需要引入该特征到当前的作用域中

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)") //默认实现
    }
}

pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author()) // 默认实现可以调用特征中其他方法，即使没有实现
    }
}

impl Summary for Post {}

impl Summary for Weibo {
    fn summarize(&self) -> String {
        format!("{}发表了微博{}", self.username, self.content)
    }
}
```

## 使用特征作为函数参数

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

fn main() {
    let post = Post{title: "Rust语言简介".to_string(),author: "Sunface".to_string(), content: "Rust棒极了!".to_string()};
    let weibo = Weibo{username: "sunface".to_string(),content: "好像微博没Tweet好用".to_string()};

    notify(&post);
    notify(&weibo);
}
```

- `&impl Summay`，只要实现Summary特征的类型都可以作为参数，类似于多态
- 接收特征的方法里只能调用特征的方法

## 特征约束

```rust
pub fn notify(item: &impl Summary) { //语法糖
    println!("Breaking news! {}", item.summarize());
}

pub fn notify<T: Summary>(item: &T) { // 完整形式，函数参数必须实现了Summary特征
    println!("Breaking news! {}", item.summarize());
}

pub fn notify(item: &(impl Summary + Display)) {} // 多重约束
pub fn notify<T: Summary + Display>(item: &T) {} // 多重约束

fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {}
fn some_function<T, U>(t: &T, u: &U) -> i32 // where约束，简化签名形式
    where T: Display + Clone,
          U: Clone + Debug {}
```

### 有条件的实现方法

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}
impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self {
            x,
            y,
        }
    }
}
impl<T: Display + PartialOrd> Pair<T> { //只为具有Display和PartialOrd特征的类型实现cmp_display方法
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```

### 有条件实现特征

```rust
impl<T: Display> ToString for T { //只为具有Display特征的类型实现ToString特征
    // --snip--
}

```

## 函数返回中的impl trait

```rust
fn returns_summarizable() -> impl Summary { //返回一个具有Summary特征的类型
    Weibo {
        username: String::from("sunface"),
        content: String::from(
            "m1 max太厉害了，电脑再也不会卡",
        )
    }
}

fn returns_summarizable(switch: bool) -> impl Summary { // 报错，只能返回一个类型
    if switch {
        Post {
            title: String::from(
                "Penguins win the Stanley Cup Championship!",
            ),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                 hockey team in the NHL.",
            ),
        }
    } else {
        Weibo {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
        }
    }
}
```


## 通过derive派生特征

通过derive可以自动派生特征的默认实现代码

- `#[derive(Debug)]`可以派生Debug特征，可以使用`println!("{:?}",s)`打印结构体信息

## 关联类型

可以在trait中定义关联类型，然后在方法中使用。

```rust
pub trait Iterator {
    type Item; // 关联类型定义

    fn next(&mut self) -> Option<Self::Item>; // 返回关联类型
}

impl Iterator for Counter {
    type Item = u32; // 关联类型为u32

    fn next(&mut self) -> Option<Self::Item> {
        // --snip--
    }
}
```

也可以使用泛型来实现上述功能，但是代码会比较冗长，特别是返回类型约束比较多的时候。使用关联类型代码可读性更好

```rust
pub trait Iterator<Item> {
    fn next(&mut self) -> Option<Item>;
}
```

## 默认泛型参数

特征可以设置默认参数类型，如Add的右参数，默认与左参数一致

```rust
trait Add<RHS=Self> { // RHS是泛型参数，默认是Self
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

struct Millimeters(u32);
struct Meters(u32);

// 注意，impl后面没有使用参数声明，Meters使用的是结构体类型
impl Add<Meters> for Millimeters { 
    type Output = Millimeters;

    fn add(self, other: Meters) -> Millimeters {
        Millimeters(self.0 + (other.0 * 1000))
    }
}
```

## 调用同名方法

有的时候，多个特征，结构体本身都可能实现相同方法名，怎么区分调用？

### 包含self参数的同名方法
```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}

fn main() {
    let person = Human;
    Pilot::fly(&person); // 调用Pilot特征上的方法
    Wizard::fly(&person); // 调用Wizard特征上的方法
    person.fly(); // 调用Human类型自身的方法
}
```

### 不包含同名参数的方法 -- 完全限定语法

```rust
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name()); // Spot
    println!("A baby dog is called a {}", <Dog as Animal>::baby_name()); // puppy
    println!("A baby dog is called a {}", Animal::baby_name()); //无法编译通过，因为实现Animal Trait的类型可能很多，无法知道是哪一个。
}
```

语法：`<Type as Trait>::function(receiver_if_method, next_arg, ...);`

## 特征定义中的特征约束

如果要定义一个特征A，要使用其他特征B的功能，在使用A时，必须要实现B。可以在特征定义的时候进行约束。

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}

struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}

impl fmt::Display for Point { // 没有这个会报错
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

fn main() {
    let p = Point{x:1,y:2};
    p.outline_print();
}

```

## 在外部类型上使用外部特征

特征有个孤儿规则：特征或者类型必需至少有一个是本地，才能在此类型上定义特征。

现在有这样一个场景，有个`Vec<T>`类型，定义在标准库中，我们想自定义`Display`，但是也是定义在标准库中，我们无法在本地实现`Display`特征。

解决以上问题，可以使用newtype模式，简要概括就是使用元组结构体对类型进行Wrap，如下面的Wrapper，rust编译的时候会自动忽略Wrapper，没有运行时消耗

```rust
use std::fmt;

struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

fn main() {
    let w = Wrapper(vec![String::from("hello"), String::from("world")]);
    println!("w = {}", w);
}
```




