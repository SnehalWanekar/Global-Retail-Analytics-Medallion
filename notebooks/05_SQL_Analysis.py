# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT 
# MAGIC     ROUND(SUM(total_sales), 2) AS grand_total_sales,
# MAGIC     ROUND(SUM(total_profit), 2) AS grand_total_profit,
# MAGIC     ROUND(SUM(total_profit) / SUM(total_sales) * 100, 2) AS overall_profit_margin_pct
# MAGIC FROM gold_category_performance;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     product_name,
# MAGIC     category,
# MAGIC     sub_category,
# MAGIC     ROUND(total_sales, 2) AS sales,
# MAGIC     ROUND(total_profit, 2) AS profit,
# MAGIC     ROUND(profit_margin * 100, 2) AS profit_margin_pct
# MAGIC FROM gold_product_performance
# MAGIC ORDER BY total_sales DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     country,
# MAGIC     state,
# MAGIC     region,
# MAGIC     ROUND(total_sales, 2) AS sales,
# MAGIC     ROUND(total_profit, 2) AS profit
# MAGIC FROM gold_region_performance
# MAGIC WHERE total_profit < 0
# MAGIC ORDER BY total_profit ASC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     discount_band,
# MAGIC     ROUND(total_sales, 2) AS sales,
# MAGIC     ROUND(total_profit, 2) AS profit,
# MAGIC     ROUND(profit_margin * 100, 2) AS profit_margin_pct
# MAGIC FROM gold_discount_analysis
# MAGIC ORDER BY avg_discount ASC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     category,
# MAGIC     product_name,
# MAGIC     ROUND(total_sales, 2) AS sales,
# MAGIC     DENSE_RANK() OVER (PARTITION BY category ORDER BY total_sales DESC) AS category_sales_rank
# MAGIC FROM gold_product_performance
# MAGIC QUALIFY category_sales_rank <= 3;