# Databricks notebook source
from pyspark.sql.functions import col, when

orders_df = spark.table("bronze_orders")

# Cast numerical and date fields to correct data types
silver_orders = (
    orders_df
    .withColumn("sales", col("sales").cast("double"))
    .withColumn("quantity", col("quantity").cast("integer"))
    .withColumn("discount", col("discount").cast("double"))
    .withColumn("profit", col("profit").cast("double"))
    .withColumn("shipping_cost", col("shipping_cost").cast("double"))
    .withColumn("order_date", col("order_date").cast("date"))
    .withColumn("ship_date", col("ship_date").cast("date"))
)

# COMMAND ----------

# Add profit margin, profit status, and discount bands
silver_orders = (
    silver_orders
    .withColumn(
        "profit_margin",
        when(col("sales") != 0, col("profit") / col("sales")).otherwise(0)
    )
    .withColumn(
        "profit_status",
        when(col("profit") > 0, "Profitable")
        .when(col("profit") < 0, "Loss")
        .otherwise("Break-even")
    )
    .withColumn(
        "discount_band",
        when(col("discount") == 0, "No Discount")
        .when(col("discount") <= 0.10, "1-10%")
        .when(col("discount") <= 0.20, "11-20%")
        .when(col("discount") <= 0.30, "21-30%")
        .otherwise("30%+")
    )
)

# COMMAND ----------

# Write cleaned and enriched data to Silver Delta table
silver_orders.write.format("delta").mode("overwrite").saveAsTable("silver_orders")

# Verify Silver table structure
spark.sql("SELECT order_id, sales, profit, profit_margin, profit_status, discount_band FROM silver_orders LIMIT 5").display()

# COMMAND ----------

