# Databricks notebook source
from pyspark.sql import SparkSession
import json

# COMMAND ----------
spark = SparkSession.builder.appName("RetailSalesIngestion").getOrCreate()

# COMMAND ----------
with open("../configs/config.json") as f:
    config = json.load(f)

sales_path = config["input_paths"]["sales_data"]
products_path = config["input_paths"]["products_data"]

# COMMAND ----------
sales_df = spark.read.csv(sales_path, header=True, inferSchema=True)
products_df = spark.read.csv(products_path, header=True, inferSchema=True)

sales_df.show(5)
products_df.show(5)
