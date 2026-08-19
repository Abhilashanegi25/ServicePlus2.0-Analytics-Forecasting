# Project Documentation

This directory contains technical documentation describing the architecture, workflow and implementation of the ServicePlus 2.0 Analytics & Forecasting project.

## Documentation

### Project Workflow

[`PROJECT_WORKFLOW.md`](./PROJECT_WORKFLOW.md)

Provides the end-to-end technical workflow of the project, covering:

- Source data and data understanding
- Data profiling and quality analysis
- Data cleaning and transformation
- JSON parsing and field extraction
- ETL pipelines
- PostgreSQL analytical storage
- Fact and dimension table design
- Analytical dataset generation
- Apache Superset dashboard development
- Forecasting workflow
- Model evaluation and forecasting outputs

## Role of This Directory

The `docs/` directory provides the technical reference for understanding how the different components of the repository connect.

The project is organised into the following major stages:

```text
ServicePlus Source Data
        │
        ▼
Data Profiling & Quality Analysis
        │
        ▼
Data Cleaning & JSON Transformation
        │
        ▼
ETL Pipelines
        │
        ▼
PostgreSQL Analytical Layer
        │
        ├───────────────┐
        ▼               ▼
   Analytics        Forecasting
        │               │
        ▼               ▼
Apache Superset    Model Results
        │               │
        └───────┬───────┘
                ▼
        Analytical Insights
