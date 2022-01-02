# Cargo

## Cargo.toml vs Cargo.lock

- Cargo.toml 由人维护，描述项目依赖的包
- Cargo.lock 由Cargo维护，包含详细包依赖

当你的项目是一个完整应用时(application)，就上传cargo.lock到git，如果是一个依赖库项目，那么请把它添加到.gitignore中。

> If you’re building a non-end product, such as a rust library that other rust packages will depend on, put Cargo.lock in your .gitignore. If you’re building an end product, which are executable like command-line tool or an application, or a system library with crate-type of staticlib or cdylib, check Cargo.lock into git

因为终端应用需要在任何时间、任何机器都能构建出相同的程序，而library不同的用户构建的可能不一样，依赖用户的环境。