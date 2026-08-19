# ServicePlus 2.0 — Analytics & Forecasting

An end-to-end data analytics, ETL, dashboarding and forecasting project developed during a Data Analytics internship at the National Informatics Centre (NIC), MeitY, New Delhi.

The project analyses ServicePlus application and workflow data to understand application volumes, service demand, department and location distributions, application status, workflow processing, service performance and future application trends.

---

## Project Overview

The project follows the complete data analytics lifecycle:

**Data → Profiling → Cleaning → ETL → Analytics → Dashboard → Forecasting**

The work involved processing application-level and workflow-level data, extracting information from nested JSON structures, preparing analytical datasets, developing an interactive Apache Superset dashboard and experimenting with statistical and machine-learning forecasting models.

The project combines both **descriptive analytics** and **predictive analytics**.

### Major Components

- Data profiling and quality analysis
- Data cleaning and transformation
- JSON extraction
- PostgreSQL-based ETL
- Application and workflow analysis
- Analytical CSV datasets
- Apache Superset dashboard
- Time-series forecasting
- Machine-learning forecasting
- Model evaluation
- Feature-importance analysis
- State-level forecasting

---

# Project Objectives

The main objectives of the project were to:

- Understand and profile the ServicePlus application data.
- Identify important application, service, department, location and workflow attributes.
- Analyse data quality, duplicates, missing values and categorical distributions.
- Extract useful information from nested application and execution JSON structures.
- Transform raw records into structured analytical data.
- Analyse application volumes and service demand.
- Analyse application status and workflow activity.
- Build an interactive business-intelligence dashboard.
- Analyse historical application trends.
- Develop and evaluate forecasting models.
- Generate forecast outputs, confidence intervals and feature-importance results.

---

# End-to-End Workflow

```text
ServicePlus Data
       │
       ▼
Data Profiling
       │
       ▼
Data Cleaning & Transformation
       │
       ▼
ETL using Python + PostgreSQL
       │
       ▼
Analytical Datasets
       │
       ├───────────────────┐
       ▼                   ▼
Apache Superset       Forecasting
       │                   │
       │             ┌─────┴──────────────┐
       │             ▼                    ▼
       │        Statistical Models   ML Models
       │        ARIMA / SARIMA       XGBoost / LightGBM
       │             │                    │
       │             └─────────┬──────────┘
       │                       ▼
       └──────────────► Analytical Insights
```

---

# Problem Statement

ServicePlus application and workflow data contains information at multiple levels of granularity.

Application-level records contain information related to applications, services, departments, submission details, dates and application status. Workflow execution data contains multiple task records associated with individual applications.

This creates several analytical challenges:

- Understanding the structure of the source data
- Extracting information stored inside nested JSON structures
- Separating application-level and task-level information
- Identifying and handling duplicate application records
- Standardising relevant categorical values
- Converting timestamp information into usable datetime values
- Deriving workflow processing metrics
- Preparing structured datasets for dashboard analysis
- Combining historical analysis with forecasting

The project addresses these challenges through a structured data-processing, analytics and forecasting workflow.

---

# 1. Data Profiling and Understanding

The first stage involved understanding the available ServicePlus data before performing transformations.

The profiling process examined:

- Dataset structure
- Application-level attributes
- Workflow-level attributes
- Missing values
- Duplicate records
- Cardinality
- Categorical distributions
- Application status
- Service distribution
- Department distribution
- Location distribution
- Temporal coverage
- Nested JSON structures

## Application-Level Information

The application data contains information used for analysing:

- Application identifiers
- Application reference numbers
- Services
- Departments
- Submission dates
- Due dates
- Submission locations
- Application status

These fields form the basis of application-level analysis.

## Workflow-Level Information

Workflow execution information contains multiple task records associated with applications.

Relevant task-level attributes include:

- Task identifiers
- Task names
- Task types
- Received timestamps
- Executed timestamps
- Actions
- Action details
- User information where available
- Location information where available

The workflow information therefore represents a different analytical grain from the application-level data.

## Data Quality Analysis

The profiling stage examined:

### Missing Values

Missing values were assessed to determine which fields could be directly used and which required special handling.

### Duplicate Records

Duplicate application records were identified and removed where application-level uniqueness was required.

### Cardinality

Unique-value counts were examined for important categorical fields such as:

- Services
- Departments
- Locations
- Application status
- Workflow actions

### Temporal Analysis

Application dates and workflow timestamps were examined to understand the available time range and prepare the data for trend analysis and forecasting.

---

# 2. Data Cleaning and Transformation

After profiling, the relevant fields were transformed into structures suitable for analysis.

The transformation work included:

- Extracting values from nested JSON objects
- Selecting relevant application attributes
- Selecting relevant workflow/task attributes
- Standardising service-related values
- Removing duplicate application records
- Converting timestamp strings into datetime values
- Extracting workflow execution information
- Calculating processing durations where valid timestamps were available
- Preparing categorical fields for downstream analysis

A simplified representation of the transformation process is:

```text
Raw Records
     │
     ▼
JSON Extraction
     │
     ▼
Field Selection
     │
     ▼
Data Cleaning
     │
     ▼
Timestamp Conversion
     │
     ▼
Deduplication
     │
     ▼
Derived Metrics
     │
     ▼
Analytical Data
```

---

# Project Documentation

The repository includes the main project documentation and final dashboard as PDF files.

### Internship Project Report

[View the Internship Project Report](./documentation/Internship_Project_Report.pdf)

The detailed report covers the project background, data understanding, profiling, cleaning, ETL, analytics, dashboard development and forecasting work.

### Project Presentation

[View the Project Presentation](./documentation/Project_Presentation.pdf)

The presentation provides a concise overview of the project, methodology, implementation, analysis, dashboard and forecasting results.

### Dashboard

[View the Dashboard](./documentation/Dashboard.pdf)

The complete Apache Superset dashboard is provided as a PDF containing the final dashboard views.

---

# Dashboard

The project dashboard was developed in **Apache Superset** and is organised into five main analytical tabs:

1. **Overview**
2. **Applications**
3. **Task Processing**
4. **Service Performance**
5. **Forecasting & Trends**

The dashboard brings together application, applicant, workflow, service-performance and forecasting analysis.

### Overview

Provides a high-level view of ServicePlus activity and the major operational indicators.

### Applications

Focuses on application volumes, application status, service demand, geographic distribution and applicant-related analysis.

### Task Processing

Focuses on workflow execution, task activity, processing time, workflow actions and operational workload.

### Service Performance

Focuses on service-level performance, processing behaviour and SLA-related analysis.

### Forecasting & Trends

Connects historical application trends with forecasted demand, forecast changes, uncertainty and state-level forecasts.

The complete dashboard is available in [`documentation/Dashboard.pdf`](./documentation/Dashboard.pdf).

---

# Analytics

The `analytics/` directory contains selected analytical datasets generated from the transformed ServicePlus data.

| Dataset | Purpose |
|---|---|
| `department_distribution.csv` | Application distribution by department |
| `location_distribution.csv` | Application distribution by submission location |
| `monthly_trend.csv` | Monthly application trend |
| `service_distribution.csv` | Application distribution by service |
| `status_distribution.csv` | Application distribution by application status |
| `workflow_actions.csv` | Workflow action frequencies |

See [`analytics/README.md`](./analytics/README.md) for details.

---

# ETL

The `etl/` directory contains the Python implementation used to transform ServicePlus application and workflow data.

The ETL layer includes:

- Database configuration
- Application extraction
- Application-level transformation
- Service dimension preparation
- Task-history extraction
- Workflow processing
- Processing-time calculation
- Loading analytical tables into PostgreSQL

Main files include:

- `etl_v2.py`
- `fact_application_v2.py`
- `fact_task_history.py`
- `task_history_etl.py`
- `db_config.py`

See [`etl/README.md`](./etl/README.md) for the implementation details.

---

# Forecasting

The `forecasting/` directory contains the forecasting notebooks and generated model outputs.

The forecasting work includes:

- Historical trend analysis
- ARIMA
- SARIMA
- XGBoost
- LightGBM
- Lag features
- Rolling averages
- Model evaluation
- Feature importance
- Forecast confidence intervals
- State-level forecasts

The notebooks are available under [`forecasting/notebooks/`](./forecasting/notebooks/).

Generated outputs are available under [`forecasting/results/`](./forecasting/results/).

---

# Technology Stack

- **Python** — data processing, ETL and forecasting
- **Pandas / NumPy** — data manipulation and analysis
- **PostgreSQL** — database and analytical storage
- **SQLAlchemy** — database connectivity
- **Apache Superset** — interactive dashboarding
- **Statsmodels** — statistical forecasting
- **Scikit-learn** — model evaluation and preprocessing
- **XGBoost** — machine-learning forecasting
- **LightGBM** — machine-learning forecasting
- **Jupyter Notebook** — experimentation and analysis
- **Git / GitHub** — version control

---

# Repository Structure

```text
ServicePlus2.0-Analytics-Forecasting/
│
├── README.md
│
├── documentation/
│   ├── Internship_Project_Report.pdf
│   ├── Project_Presentation.pdf
│   └── Dashboard.pdf
│
├── analytics/
│   ├── README.md
│   ├── department_distribution.csv
│   ├── location_distribution.csv
│   ├── monthly_trend.csv
│   ├── service_distribution.csv
│   ├── status_distribution.csv
│   └── workflow_actions.csv
│
├── etl/
│   ├── README.md
│   ├── db_config.py
│   ├── etl_v2.py
│   ├── fact_application_v2.py
│   ├── fact_task_history.py
│   ├── task_history_etl.py
│   └── .env.example
│
├── forecasting/
│   ├── README.md
│   ├── notebooks/
│   │   ├── forecast.ipynb
│   │   └── forecasting.ipynb
│   └── results/
│
├── superset/
│   └── README.md
│
└── docs/
    └── PROJECT_WORKFLOW.md

