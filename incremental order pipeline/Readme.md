# E-Commerce Orders Optimization Pipeline (Databricks + PySpark)

## 📌 Overview
This project demonstrates a scalable and optimized data pipeline for e-commerce order data using Databricks and PySpark. The pipeline consists of ingestion, transformation, optimization (Delta Lake), and final analytics-ready data storage.

## 🧰 Technologies
- Databricks
- PySpark
- Delta Lake
- Parquet
- Z-Ordering
- GitHub

## 📂 Pipeline Stages
1. **Ingestion** – Load raw CSV data
2. **Transformation** – Clean, enrich, and prepare data
3. **Optimization** – Use Delta Lake, partitioning & Z-ordering
4. **Analytics** – Analyze optimized Gold layer

## 📦 How to Use
1. Upload all files to Databricks Workspace or run locally with PySpark
2. Run the notebooks in sequence:
   - 01_data_ingestion.py
   - 02_data_cleaning_transformation.py
   - 03_data_optimization.py
   - 04_data_analysis_gold_layer.py

## 📁 Input Data
Included: `data/sample_raw_data.csv`

## ✅ Output
Optimized Delta tables partitioned by `category` and Z-Ordered by `order_date`

## 👨‍💻 Author
Navin Shah | Data & BI Consultant
