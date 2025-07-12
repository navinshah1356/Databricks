# Databricks notebook source
from pyspark.sql.functions import col, round

# COMMAND ----------
sales_with_products = clean_sales_df.join(clean_products_df, "product_id")

# Add revenue and profit
result_df = sales_with_products.withColumn(
    "revenue", col("quantity") * col("price")
).withColumn(
    "profit", (col("price") - col("cost_price")) * col("quantity")
)

result_df.select("order_id", "product_name", "quantity", "revenue", "profit").show(5)
