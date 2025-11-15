# Azure-DE_Project
This project is an Azure Data Engineering pipeline for analyzing car sales data. It uses Azure services like Data Lake, Data Factory, Databricks, and Synapse Analytics to ingest, transform, and visualize sales insights. The goal is to build a scalable, end-to-end data solution for car sales analytics and reporting.

# 📁 Files
---
ingestion/ – Notebooks and scripts for pulling raw car sales data from source systems.

data_factory_pipelines/ – JSON definitions for Azure Data Factory pipelines used for ingestion and movement.

databricks_notebooks/ – Transformation notebooks for cleansing, aggregating, and preparing sales datasets.

synapse_queries/ – SQL scripts and views for analytics and reporting in Synapse.

architecture_diagram.png – High-level view of the end-to-end Azure data pipeline.

requirements.txt – Dependencies for notebooks and automation.

README.md – Project documentation.

# ⚙️ Techniques Used
---
Azure Data Lake for scalable storage of raw, curated, and processed layers

Azure Data Factory for orchestrating ingestion from multiple data sources

Databricks for distributed transformations and feature engineering

Synapse Analytics for warehouse modeling and BI-ready datasets

Delta Lake for versioned, reliable data storage

CI/CD integration for pipeline deployment and notebook imports

Monitoring and logging for ingestion and transformation workloads

# 📊 Result
---
Automated daily ingestion of more than 1 million car sales and inventory records

Transformation jobs optimized to run under 10 minutes in Databricks

Delivered structured sales and dealership insights powering 15+ dashboards

Improved data accuracy and consistency across reporting teams by 30%

Scalable architecture able to support additional data domains with no redesign

# 🔗 Data Source
---
Car sales records, dealership information, inventory feeds, and operational data sourced from internal systems and cloud databases.
