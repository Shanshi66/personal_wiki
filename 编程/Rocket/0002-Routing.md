# 
```rust
#[get("/world")]              // <- route attribute
fn world() -> &'static str {  // <- request handler
    "hello, world!"
}
```