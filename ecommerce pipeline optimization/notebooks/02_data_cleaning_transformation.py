df_bronze = spark.read.format("delta").load("/mnt/bronze/ecommerce_orders")

# Clean: Remove rows with nulls
df_clean = df_bronze.na.drop()

# Enrich: Add total_price column
from pyspark.sql.functions import col, expr
df_transformed = df_clean.withColumn("total_price", (col("quantity") * col("price")) - col("discount"))

df_transformed.show()

# Save to Silver layer
df_transformed.write.format("delta").mode("overwrite").save("/mnt/silver/ecommerce_orders")