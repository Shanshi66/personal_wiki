# HashMap

使用之前引入相应包
```rust
use std::collections::HashMap;
```

## 创建方法

所有K，所有V必须类型相同

- HashMap::new()
- HashMap::with_capacity(capacity)
- 从迭代器创建，如将Vec转成迭代器，然后再使用collect收集

```rust
// 创建一个HashMap，用于存储宝石种类和对应的数量
let mut my_gems = HashMap::new();

let mut my_gems = HashMap::with_capacity(capacity); // 如果预先知道数据量

// 将宝石类型和对应的数量写入表中
my_gems.insert("红宝石", 1);
my_gems.insert("蓝宝石", 2);
my_gems.insert("河边捡的误以为是宝石的破石头", 18);

fn main() {
    let teams_list = vec![
        ("中国队".to_string(), 100),
        ("美国队".to_string(),10),
        ("日本队".to_string(),50),
    ];
    // collect方法可以转成很多种类型，所以需要通过指定HashMap引导Rust，具体KV类型可以让Rust推导
    let teams_map: HashMap<_,_> = teams_list.into_iter().collect(); 
    
    println!("{:?}",teams_map)
}
```

## 所有权转移

- 若类型实现 Copy 特征，该类型会被复制进 HashMap，因此无所谓所有权
- 若没实现 Copy 特征，所有权将被转移给 HashMap 中


```rust
fn main() {
    use std::collections::HashMap;

    let name = String::from("Sunface");
    let age = 18;

    let mut handsome_boys = HashMap::new();
    handsome_boys.insert(name, age);

    println!("因为过于无耻，{}已经被从帅气男孩名单中除名", name); // error，name所有权已经被转移
    println!("还有，他的真实年龄远远不止{}岁",age);
}
```

使用引用确保生命周期与hashmap保持一致
```rust
fn main() {
    use std::collections::HashMap;

    let name = String::from("Sunface");
    let age = 18;

    let mut handsome_boys = HashMap::new();
    handsome_boys.insert(&name, age);

    std::mem::drop(name);  // error
    println!("因为过于无耻，{:?}已经被除名", handsome_boys);
    println!("还有，他的真实年龄远远不止{}岁",age);
}
```

## 查询

- `m.get(&K)`查到了返回`Some(&T)`,没查到返回None

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score: Option<&i32> = scores.get(&team_name);

for (key, value) in &scores {
    println!("{}: {}", key, value);
}
```

## 更新

```rust
fn main() {
    use std::collections::HashMap;

    let mut scores = HashMap::new();

    scores.insert("Blue", 10);

    // 覆盖已有的值
    let old = scores.insert("Blue", 20);
    assert_eq!(old, Some(10));

    // 查询新插入的值
    let new = scores.get("Blue");
    assert_eq!(new, Some(&20));
    
    // 查询Yellow对应的值，若不存在则插入新值
    let v = scores.entry("Yellow").or_insert(5);
    assert_eq!(*v, 5); // 不存在，插入5

    // 查询Yellow对应的值，若不存在则插入新值
    let v = scores.entry("Yellow").or_insert(50);
    assert_eq!(*v, 5); // 已经存在，因此50没有插入


    let text = "hello world wonderful world";

    let mut map = HashMap::new();
    // 根据空格来切分字符串(英文单词都是通过空格切分)
    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }
}
```

- `or_indert()`返回`&mut v`

## 扩展

- 目前，HashMap 使用的哈希函数是 SipHash，它的性能不是很高，但是安全性很高
- 如果要追求性能，可以考虑第三方库，如ahash

