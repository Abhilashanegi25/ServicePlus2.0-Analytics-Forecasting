# Analytics

This directory contains analytical datasets generated from ServicePlus application and workflow data.

## Reports

### Department Distribution

`department_distribution.csv`

Contains application counts by standardized department.

Columns:

- `department_standardized`
- `applications`

### Location Distribution

`location_distribution.csv`

Contains application counts by submission location.

Columns:

- `submission_location`
- `applications`

### Monthly Trend

`monthly_trend.csv`

Contains monthly application volumes.

Columns:

- `month`
- `applications`

### Service Distribution

`service_distribution.csv`

Contains service-level application/service counts after service-name standardization.

Columns:

- `service_standardized`
- `service_count`

### Status Distribution

`status_distribution.csv`

Contains application counts by application status.

Columns:

- `appl_status`
- `applications`

### Workflow Actions

`workflow_actions.csv`

Contains occurrences of workflow actions.

Columns:

- `action_detail`
- `occurrences`

## Purpose

These datasets provide the analytical layer used for trend analysis, distribution analysis, workflow analysis, and dashboard visualizations.

The files in this directory are derived analytical outputs rather than the original ServicePlus source data.
