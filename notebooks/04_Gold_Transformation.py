# Databricks notebook source
from pyspark.sql.functions import col, sum as _sum, avg

orders = spark.table("silver_orders")

gold_category = (
    orders
    .groupBy("category", "sub_category")
    .agg(
        _sum("sales").alias("total_sales"),
        _sum("profit").alias("total_profit"),
        _sum("quantity").alias("total_quantity"),
        avg("discount").alias("avg_discount")
    )
    .withColumn("profit_margin", col("total_profit") / col("total_sales"))
)

gold_category.write.format("delta").mode("overwrite").saveAsTable("gold_category_performance")

# COMMAND ----------

gold_product = (
    orders
    .groupBy("product_id", "product_name", "category", "sub_category")
    .agg(
        _sum("sales").alias("total_sales"),
        _sum("profit").alias("total_profit"),
        _sum("quantity").alias("total_quantity"),
        avg("discount").alias("avg_discount")
    )
    .withColumn("profit_margin", col("total_profit") / col("total_sales"))
)

gold_product.write.format("delta").mode("overwrite").saveAsTable("gold_product_performance")

# COMMAND ----------

gold_region = (
    orders
    .groupBy("region", "country", "state")
    .agg(
        _sum("sales").alias("total_sales"),
        _sum("profit").alias("total_profit"),
        _sum("quantity").alias("total_quantity")
    )
    .withColumn("profit_margin", col("total_profit") / col("total_sales"))
)

gold_region.write.format("delta").mode("overwrite").saveAsTable("gold_region_performance")

# COMMAND ----------

gold_discount = (
    orders
    .groupBy("discount_band")
    .agg(
        _sum("sales").alias("total_sales"),
        _sum("profit").alias("total_profit"),
        _sum("quantity").alias("total_quantity"),
        avg("discount").alias("avg_discount")
    )
    .withColumn("profit_margin", col("total_profit") / col("total_sales"))
)

gold_discount.write.format("delta").mode("overwrite").saveAsTable("gold_discount_analysis")

# COMMAND ----------

spark.sql("SHOW TABLES LIKE 'gold_*'").display()