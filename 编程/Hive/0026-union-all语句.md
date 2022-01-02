# union all

union all可以对多个查询结果进行合并，不过要求子查询具有相同的列，数据类型一致

```sql
select log.ymd, log.level, log.message
from (
    select l1.ymd, l1.level, l1.message, 'Log1' as source from log1 l1
	union all
	select l2.ymd, l2.level, l2.message, 'Log2' as source from log1 l2
) log
sort by log.ymd asc;
```

