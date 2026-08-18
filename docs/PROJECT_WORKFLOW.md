# Project Workflow

## 1. Data Extraction

ServicePlus application and workflow information was extracted from the PostgreSQL database.

## 2. ETL & Transformation

The ETL layer processes application and execution data and transforms nested workflow information into structured analytical records.

Key transformations include:

- Application-level record preparation
- Service information extraction
- Workflow/task extraction
- Timestamp conversion
- Processing-time calculation
- Duplicate handling
- Creation of fact and dimension datasets

## 3. Data Warehouse

The transformed data is organized into fact and dimension tables under the analytical schema.

## 4. Analytics

Analytical datasets are generated for:

- Monthly trends
- Service distribution
- Department distribution
- Status distribution
- Location distribution
- Workflow actions
- Task processing analysis

## 5. Dashboarding

Apache Superset is used as the business-intelligence layer for interactive analytical dashboards.

## 6. Forecasting

Historical application data is used for forecasting analysis.

The forecasting workflow includes:

- Model comparison
- Forecast generation
- Actual vs forecast analysis
- Confidence intervals
- Feature importance
- State-level forecasting
- Forecast change analysis

## 7. Outputs

The final outputs include structured datasets, analytical reports, dashboards, forecasting notebooks, and forecasting result files.
