# Delta Live Tables: Incremental Orders Pipeline (E-Commerce)

## 📌 Overview
A real-world simulation of an incremental order processing pipeline using **Delta Live Tables (DLT)** in Databricks.

## 🧪 Scenario
- JSON order logs are ingested daily into `/mnt/raw/orders/`
- Pipeline processes data into:
  - **Bronze Table**: Raw ingestion
  - **Silver Table**: Deduplicated & clean (SCD Type 1 logic)
  - **Gold Table**: Daily revenue summary

## 🧰 Technologies
- Databricks
- PySpark
- Delta Live Tables (DLT)
- JSON logs, Delta Lake, Parquet

## 📂 Project Structure
---
dlt-incremental-orders-pipeline/
├── dlt_pipeline.py
├── data/
│ ├── orders_2025-07-01.json
│ ├── orders_2025-07-02.json
│ └── orders_2025-07-03.json
├── README.md
└── requirements.txt
---


## 🚀 How to Run
1. Upload `dlt_pipeline.py` to a Databricks Workspace
2. Create a new **Delta Live Table Pipeline**
   - Source: `/mnt/raw/orders/`
   - Target: `/mnt/dlt_output/`
3. Monitor Bronze → Silver → Gold outputs

## ✅ Output Tables
- `bronze_orders`
- `silver_orders`
- `gold_daily_sales`

## 👨‍💻 Author
Navin Shah | Data Engineer
