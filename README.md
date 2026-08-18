# NIC ServicePlus Analytics & Forecasting

An end-to-end data analytics and forecasting project developed during a Data Analytics internship at the National Informatics Centre (NIC), MeitY, New Delhi.

The project focuses on transforming ServicePlus application and workflow data into structured analytical datasets, dashboards, and forecasting outputs.

## Project Overview

The workflow follows:

Data Extraction → ETL & Transformation → Data Warehouse → Analytics → Apache Superset → Forecasting

The project includes:

- ETL pipelines for application and workflow data
- Structured fact and dimension tables
- Analytical reporting and trend analysis
- Apache Superset dashboards
- Time-series forecasting
- Forecast comparison and confidence intervals
- Feature-importance analysis
- State-level forecasting outputs

## Architecture

```text
ServicePlus Data
       │
       ▼
   PostgreSQL
       │
       ▼
      ETL
       │
       ├───────────────┐
       ▼               ▼
Data Warehouse     Analytics
(Fact/Dimension)   & Reports
       │               │
       └───────┬───────┘
               ▼
        Apache Superset
               │
               ▼
          Dashboards

Historical Data
       │
       ▼
  Forecasting
       │
       ├── Model Comparison
       ├── Actual vs Forecast
       ├── Confidence Intervals
       ├── Feature Importance
       └── State-level Forecasts
