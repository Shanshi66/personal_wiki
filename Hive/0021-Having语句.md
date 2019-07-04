# Having语句

Having语句可以对groupby产生的结果进行条件过滤

```sql
select year(ymd), avg(price_close) from stocks
where exchange = 'NASDAQ' and symbol = 'AAPL'
group by year(ymd)
having avg(price_close) > 50
```

如果没有having语句，需要嵌套一个select语句

```sql
select s2.year, s2.avg from
(
    select year(ymd) as year, avg(price_close) as avg from stocks
    where exchange = 'NASDAQ' and symbol = 'AAPL'
    group by year(ymd)
) s2
where s2.avg > 50
```

