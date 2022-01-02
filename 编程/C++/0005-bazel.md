# bazel

## bazel选项

- `--copt` : `--copt=-g  --copt=-O0`会传递`-g`，`-O0`选项给gcc
- `-c`: 指定编译模式，opt优化，dbg调试
- `--local_resources`: 指定本地资源。bazel默认会使用本地全部资源，很容易爆内存

