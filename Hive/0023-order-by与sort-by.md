# order by 与sort by

order by是全局排序，所有数据都会过一个reducer，非常慢。sort by是局部排序，只保证每个reducer的输出是有序的。

```sql
select s.ymd, s.symbol, s.price_close
from stocks s
order by s.ymd asc, s.symbol desc

select s.ymd, s.symbol, s.price_close
from stocks s
sort by s.ymd asc, s.symbol desc
```