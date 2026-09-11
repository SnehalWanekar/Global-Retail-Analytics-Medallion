# Global Retail Sales & Profitability Analytics

An end-to-end modern data engineering and business intelligence platform built on Databricks, PySpark, Delta Lake, and Power BI. This project demonstrates how to process large-scale retail data using a Medallion Architecture (Bronze -> Silver -> Gold), establish direct lakehouse connectivity via Databricks SQL Warehouse, and build high-impact executive dashboards.

---

## 🏗️ Architecture & Tech Stack

```text
Global Superstore Dataset (50K+ Records)
   │
   ▼
[ Databricks Unity Catalog ]
   ├── Bronze Layer : Raw CSV Data Ingestion & Storage
   ├── Silver Layer : Schema Validation, Type Casting & Data Cleansing
   └── Gold Layer   : Business-Aggregated Analytics Tables
   │
   ▼
[ Databricks SQL Warehouse ]
   │  (PAT Authentication Connection)
   ▼
[ Power BI Desktop ]
   └── Executive Overview & Business Insight Dashboards


Storage & Data Lake: Delta Lake, Databricks Unity Catalog

Processing & Querying: PySpark, Spark SQL, Databricks SQL Warehouse

Data Modeling & BI: Power BI Desktop, DAX Measures

Architecture: Medallion Architecture (Bronze / Silver / Gold)

📊 Key Business Insights & Value Delivered
Discount Threshold Impact: Analysis revealed that promotional discounts up to 15% yield healthy profit margins averaging 28%. However, discounts exceeding 20% cause severe profit degradation, dropping margins to -18.5%.

Regional Performance Drag: Isolated over $150K+ in cumulative profit drag across 12 specific states/regions driven by a combination of high fulfillment overhead and excessive discounting.

Product Profitability Leaks: High top-line revenue volume in categories like Tables and Bookcases is consistently offset by unmanaged promotional pricing, resulting in net operational losses.

🚀 Key Features & Implementation Steps
Data Engineering (Databricks & PySpark)
Bronze Layer: Ingested 50K+ global retail records into native Delta Lake tables preserving original raw formats.

Silver Layer: Cleansed datasets by casting data types, handling missing values, standardizing date formats, and enriching transaction records.

Gold Layer: Created aggregate models (gold_category_performance, gold_product_performance, gold_region_performance, and gold_discount_analysis) optimized for analytical reporting.

BI & Dashboarding (Power BI & DAX)
Engineered Data Pipeline: Connected Power BI to Databricks SQL Warehouse using Personal Access Tokens (PAT).

DAX Measure Modeling: Developed modular measures for Total Sales, Total Profit, Total Quantity, and dynamic Profit Margin.

Executive Overview Page: Built interactive card visuals, sub-category breakdown charts, and geographical matrix tables.

Insight Workspaces: Converted secondary pages into narrative-driven visual cards and dynamic KPI displays highlighting critical margin leakage points.


Global-Retail-Analytics-Medallion/
├── README.md
├── notebooks/
│   ├── 01_Ingestion_Bronze.py
│   ├── 02_Data_Quality_EDA.py
│   ├── 03_Silver_Transformation.py
│   ├── 04_Gold_Transformation.py
│   └── 05_SQL_Analysis.sql
└── dashboards/
    ├── Global_Retail_Analytics.pbix
    └── screenshots/
        ├── executive_overview.png
        ├── product_discount_analysis.png
        └── regional_insights.png

Strategic Recommendations
Automate Discount Guardrails: Implement checkout rules limiting standard sales discounts to a maximum of 15%, requiring explicit managerial approval for higher tiers.

Fulfillment Cost Audit: Conduct a logistics review across bottom-performing regional territories to adjust shipping subsidy structures and restore base profit margins.