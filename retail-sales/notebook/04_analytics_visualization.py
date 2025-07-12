# Databricks notebook source
import pandas as pd
import matplotlib.pyplot as plt

# COMMAND ----------
top_products = result_df.groupBy("product_name").sum("revenue").orderBy("sum(revenue)", ascending=False)

top_products_pd = top_products.toPandas()
top_products_pd.plot(kind="bar", x="product_name", y="sum(revenue)", legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
