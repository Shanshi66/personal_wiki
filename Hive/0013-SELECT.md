# SELECT

## 不同类型字段引用

- 对于array类型，引用方式是：`array_field[index]`，index从0开始。
- 对于map类型，引用方式是`map_field[key]`。
- 对于struct类型，引用方式是：`struct_field[key]`

##　使用正则表达式指定列

```sql
> select symbol, `price.*` from stocks
```

查找以`price`开始的列

## 列计算

hive支持的算术运算符：

```sql
+,-,*,/,%(取余),&,|,^,~(后四个分别是按位与，或，异或，取反)
```

如果字段类型不同，计算的时候会将类型转为数据范围更广的那个进行计算。

hive计算的时候也会出现数据溢出的情况，注意数据类型。

