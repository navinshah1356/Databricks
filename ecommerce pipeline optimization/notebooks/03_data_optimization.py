df_silver = spark.read.format("delta").load("/mnt/silver/ecommerce_orders")

# Convert to Delta format with partitioning and Z-Ordering
df_silver.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("category") \
    .option("overwriteSchema", "true") \
    .save("/mnt/gold/ecommerce_orders")

from delta.tables import DeltaTable
gold_table = DeltaTable.forPath(spark, "/mnt/gold/ecommerce_orders")
gold_table.optimize().zorderBy("order_date")