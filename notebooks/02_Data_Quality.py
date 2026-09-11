# Databricks notebook source
orders_df = spark.table("bronze_orders")
returns_df = spark.table("bronze_returns")
people_df = spark.table("bronze_people")

print(f"Total Bronze Orders: {orders_df.count()}")
print(f"Total Bronze Returns: {returns_df.count()}")
print(f"Total Bronze People: {people_df.count()}")

# COMMAND ----------

from pyspark.sql.functions import col, sum as _sum

def check_nulls(df):
    return df.select([
        _sum(col(c).isNull().cast("int")).alias(c)
        for c in df.columns
    ])

display(check_nulls(orders_df))

# COMMAND ----------

total_count = orders_df.count()
distinct_count = orders_df.dropDuplicates().count()

print(f"Total Rows: {total_count}")
print(f"Distinct Rows: {distinct_count}")
print(f"Duplicate Rows: {total_count - distinct_count}")

# COMMAND ----------

# Check for negative sales, quantity, or invalid discounts
print("Invalid Sales (< 0):", orders_df.filter(col("sales") < 0).count())
print("Invalid Quantity (<= 0):", orders_df.filter(col("quantity") <= 0).count())
print("Invalid Discount (< 0 or > 1):", orders_df.filter((col("discount") < 0) | (col("discount") > 1)).count())
print("Negative Profit Count (Business Check):", orders_df.filter(col("profit") < 0).count())