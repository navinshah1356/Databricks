# Databricks notebook source
from pyspark.sql.functions import col

# COMMAND ----------
clean_sales_df = sales_df.dropna()
clean_products_df = products_df.dropna()

# Drop duplicates if any
clean_sales_df = clean_sales_df.dropDuplicates()
clean_products_df = clean_products_df.dropDuplicates()

clean_sales_df.show(5)
clean_products_df.show(5)
