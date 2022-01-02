# Dataframe合并两列

以下代码自定义了一个udf将dataframe两列合并成一列，每列是个元组。需要注意的是，udf要注明返回值类型，否者会返回一个java object名字

```python
from pyspark.sql.functions import udf
from pyspark.sql import functions as F
merge2col = udf(lambda x, y: (x, y), StructType([StructField("user_id", StringType(), False), StructField("cnt", IntegerType(), False)]))
base_data = base_data.withColumn("user_cnt", merge2col(F.col('user_id'), F.col('cnt')))
```

