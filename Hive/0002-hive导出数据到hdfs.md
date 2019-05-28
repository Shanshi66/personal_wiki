# hive导出数据到hdfs

```sql
insert overwrite directory '$hdfs_path'
row format delimited fields terminated by '\t'  # 可无
select ...
```

`set mapred.reduce.tasks=1 `可以控制输出文件的个数