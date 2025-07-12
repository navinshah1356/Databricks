# Retail Sales Analytics with PySpark (Databricks)

This project demonstrates a basic data engineering and analytics pipeline using **Databricks** and **PySpark**.

## 📌 Project Overview

- Ingest retail sales and product data
- Perform data cleansing and transformation
- Calculate key performance metrics like revenue and profit
- Visualize simple sales trends

## 📁 Project Structure

```
retail-sales-pyspark/
│
├── data/
│   ├── sales.csv
│   └── products.csv
│
├── notebooks/
│   ├── 01_data_ingestion.py
│   ├── 02_data_cleaning.py
│   ├── 03_data_transformation.py
│   ├── 04_analytics_visualization.py
│
├── configs/
│   └── config.json
│
├── requirements.txt
└── README.md
```

## 🚀 How to Run in Databricks

1. Upload this folder to your Databricks workspace.
2. Open and run the notebooks in sequence.
3. Replace file paths in `config.json` or notebooks as per your DBFS mount or workspace.

## 🧰 Technologies Used

- PySpark (Spark DataFrames)
- Databricks Notebooks
- Pandas & Matplotlib (for visualizations)
- JSON (for configuration)

---

**Tags:** `#Databricks` `#PySpark` `#DataEngineering` `#Portfolio`
