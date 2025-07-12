from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ECommerceOrders").getOrCreate()

# Load raw data
df_raw = spark.read.option("header", True).csv("/FileStore/data/sample_raw_data.csv", inferSchema=True)

df_raw.show()
df_raw.printSchema()

# Save to Bronze layer
df_raw.write.format("delta").mode("overwrite").save("/mnt/bronze/ecommerce_orders")