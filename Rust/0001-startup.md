# start-up

## 安装

1. `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`


## 基本概念

1. cargo是rust的构建工具和包管理器
2. Cargo.toml存放项目的metadata
3. crates指rust中的package
4. https://crates.io/，rust所有的crates
5. Cargo.lock，存放包的版本信息
6. Ferris，rust社区吉祥物
7. Rustaceans，ruster的自称，来自单词crustacean(甲壳纲动物，如果螃蟹、虾)

## 常用命令

1. `rustup update`rust更新
2. `cargo build`构建
3. `cargo run`运行
4. `cargo test`测试
5. `cargo doc`生成文档
6. `cargo publish`发布libary到cargo.io
7. `cargo --version`检查cargo版本
8. `cargo new <project-name>`生成<project-name>项目
   
## 常见问题

1. 包下载慢：在~/.cargo/config文件中添加国内源
    ```
    [source.crates-io]
    registry = "https://github.com/rust-lang/crates.io-index"
    replace-with = 'ustc'
    [source.ustc]
    registry = "git://mirrors.ustc.edu.cn/crates.io-index"
    ```
2. 