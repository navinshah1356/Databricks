import dlt
from pyspark.sql.functions import col, expr

# -------------------
# Bronze: Raw ingest
# -------------------
@dlt.table(
    comment="Raw order data from JSON logs"
)
def bronze_orders():
    return (
        spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "json")
            .load("/mnt/raw/orders/")
    )

# -------------------
# Silver: Cleaned + Incremental Merge (SCD Type 1)
# -------------------
@dlt.table(
    comment="Deduplicated and cleaned order data"
)
@dlt.expect("valid_price", "price >= 0")
@dlt.expect("valid_quantity", "quantity > 0")
def silver_orders():
    bronze_df = dlt.read("bronze_orders")

    # Drop duplicates based on order_id and keep latest
    from pyspark.sql.window import Window
    from pyspark.sql.functions import row_number

    windowSpec = Window.partitionBy("order_id").orderBy(col("order_timestamp").desc())

    latest_orders = (
        bronze_df.withColumn("row_num", row_number().over(windowSpec))
        .filter("row_num = 1")
        .drop("row_num")
    )

    return latest_orders

# -------------------
# Gold: Daily Revenue Aggregation
# -------------------
@dlt.table(
    comment="Daily total revenue by category"
)
def gold_daily_sales():
    df = dlt.read("silver_orders")
    df = df.withColumn("total_price", (col("quantity") * col("price")) - col("discount"))
    df = df.withColumn("order_date", expr("to_date(order_timestamp)"))

    return df.groupBy("order_date", "category") \
             .agg(expr("sum(total_price) as daily_revenue"))
