# Databricks notebook source
print(spark.version)

# COMMAND ----------

file_path = "/Workspace/Global_Retail_Analytics/superstore_2016.xlsx"

# Read the primary Orders sheet
df = (
    spark.read
    .option("headerRows", 1)
    .excel(file_path)
)

display(df)

# COMMAND ----------

df.printSchema()
df.count()

# COMMAND ----------

# Extract Orders Sheet
orders_df = (
    spark.read
    .option("headerRows", 1)
    .option("dataAddress", "Orders")
    .excel(file_path)
)

# Extract Returns Sheet
returns_df = (
    spark.read
    .option("headerRows", 1)
    .option("dataAddress", "Returns")
    .excel(file_path)
)

# Extract People Sheet
people_df = (
    spark.read
    .option("headerRows", 1)
    .option("dataAddress", "People")
    .excel(file_path)
)

# COMMAND ----------

import re

def clean_column_names(df):
    new_cols = [re.sub(r'[^a-zA-Z0-9]+', '_', c).strip('_').lower() for c in df.columns]
    return df.toDF(*new_cols)

# Apply column cleaning
orders_df_clean = clean_column_names(orders_df)

# Save to Bronze Delta table
orders_df_clean.write.format("delta").mode("overwrite").saveAsTable("bronze_orders")

# Verify
spark.sql("SELECT * FROM bronze_orders LIMIT 5").display()

# COMMAND ----------

# Clean and save Returns sheet
returns_df_clean = clean_column_names(returns_df)
returns_df_clean.write.format("delta").mode("overwrite").saveAsTable("bronze_returns")

# Clean and save People sheet
people_df_clean = clean_column_names(people_df)
people_df_clean.write.format("delta").mode("overwrite").saveAsTable("bronze_people")

# Verify all Bronze tables
spark.sql("SHOW TABLES").display()