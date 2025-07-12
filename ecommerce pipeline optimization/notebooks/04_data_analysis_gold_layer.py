df_gold = spark.read.format("delta").load("/mnt/gold/ecommerce_orders")

from pyspark.sql.functions import sum

df_gold.groupBy("category").agg(sum("total_price").alias("total_revenue")).show()

df_gold.groupBy("product_id").agg(sum("quantity").alias("total_units_sold")) \
    .orderBy("total_units_sold", ascending=False).show()