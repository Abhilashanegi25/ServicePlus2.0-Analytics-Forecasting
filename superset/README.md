# Apache Superset Dashboard

The ServicePlus Analytics Dashboard was developed in Apache Superset as the interactive visualization and business-intelligence layer of the project.

The dashboard brings together application, workflow, service-performance and forecasting analysis into a single interactive interface.

## Dashboard Structure

The dashboard is organized into five main tabs:

1. Overview
2. Applications
3. Task Processing
4. Service Performance
5. Forecasting & Trends

Global filters are available for:

- State
- Service
- Submission Date

These filters allow the analysis to be narrowed to specific geographic, service-level and time-based segments.

---

## 1. Overview

The Overview tab provides a high-level view of ServicePlus activity.

It serves as the starting point of the dashboard and provides a consolidated view of overall application activity before moving into the detailed analytical sections.

---

## 2. Applications

The Applications tab focuses on application submissions, processing status, geographic distribution and service demand.

### Key Performance Indicators

The dashboard includes:

- Available Services
- Total Applications
- Applications Processed
- Applications in Progress

### Application Analysis

The tab includes analysis of:

- Application status distribution
- Application volume by state
- Most requested services

### Applicant Analytics

The Applications section also provides applicant-level analysis, including:

- Total Applicants
- Districts Covered
- Active States
- Applicants by State
- Top Districts by Applicants
- Applicant Age Group Distribution
- Average Applicant Age by State

---

## 3. Task Processing

The Task Processing tab focuses on workflow execution and operational processing activity.

The analysis covers:

- Task execution volume
- Completed and rejected tasks
- Processing time
- User/processor activity
- Verification-office workload

This provides an operational view of application workflow activity and processing concentration.

---

## 4. Service Performance

The Service Performance tab focuses on service-level operational performance.

The analysis includes:

- Service processing performance
- Processing-time patterns
- SLA compliance
- SLA breaches
- Offices requiring attention

This section connects service-level demand with operational performance.

---

## 5. Forecasting & Trends

The Forecasting & Trends tab connects historical application activity with the forecasting work carried out in the project.

It presents:

- Historical application trends
- Forecasted demand
- Actual versus forecast values
- Forecast changes
- Forecast uncertainty
- State-level forecasts

The underlying forecasting work includes ARIMA, XGBoost, LightGBM, feature-importance analysis and forecast confidence intervals.

---

## Dashboard Data Flow

The dashboard follows the analytical workflow:

ServicePlus Data
        ↓
PostgreSQL
        ↓
ETL & Transformation
        ↓
Analytical Tables / Datasets
        ↓
Apache Superset
        ↓
Interactive Dashboard

Forecasting outputs are generated from historical application data and are incorporated into the forecasting and trend analysis.

---

## Technology

The dashboard layer uses:

- Apache Superset
- PostgreSQL
- SQL
- Python-generated analytical datasets
- Forecasting outputs

---

## Screenshots

Screenshots of the completed dashboard are available in:

`screenshots/`

The screenshot set covers the dashboard views represented in the repository.

Before publication, screenshots should be reviewed to ensure that restricted or personally identifiable information is not exposed.

---

## Dashboard Documentation

The complete dashboard is provided as a PDF in the repository:

[`documentation/Dashboard.pdf`](../documentation/Dashboard.pdf)

The PDF contains the final dashboard views covering the Overview, Applications, Task Processing, Service Performance, and Forecasting & Trends sections.

Additional dashboard screenshots are available in:

`screenshots/`

The screenshots provide individual visual references for selected dashboard views.

Before publication, dashboard visuals should be reviewed to ensure that restricted or personally identifiable information is not exposed.---

## Data Privacy

The public repository does not contain:

- Database credentials
- Passwords
- Raw database dumps
- Restricted source datasets

The repository contains selected analytical outputs, forecasting results, dashboard screenshots, code and documentation prepared for project documentation purposes.
