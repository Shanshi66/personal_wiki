# distribute by与cluster by

```sql
select s.ymd, s.symbol, s.price_close
from stocks
distribute by s.symbol
sort by s.symbol asc, s.ymd asc
```

distribute by控制map的输出在reducer里的划分，保证同一个key划分到同一个reduce。

结合distribute by和sort by可以实现文件的全局排序，distribute by需要写在sort by前面。

如果distribute by和sort by涉及到的列完全相同，则可以用cluster by代替

```sql
select s.ymd, s.symbol, s.price_close
from stocks
cluster by s.symbol
```

