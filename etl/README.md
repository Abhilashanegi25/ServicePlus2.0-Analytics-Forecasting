# ETL Pipelines

This directory contains the Python-based ETL scripts used to transform ServicePlus application and workflow data into analytical fact and dimension datasets.

## ETL Workflow

The ETL process follows:

Extract → Parse → Clean → Transform → Load

## Scripts

### `etl_v2.py`

Processes application-level data and builds the service dimension.

Main operations include:

- Extracting application and execution data from PostgreSQL
- Removing duplicate applications
- Parsing nested application information
- Extracting service identifiers and names
- Extracting department information
- Building the `dim_service` dataset
- Loading the result into the analytical PostgreSQL schema

### `fact_application_v2.py`

Builds the application-level fact table.

The transformation extracts:

- Application ID
- Service ID
- Application reference number
- Submission date
- Due date
- State
- Completion time

Completion time is derived from the executed workflow tasks associated with an application.

### `fact_task_history.py`

Processes workflow execution data and creates task-level records.

The resulting dataset contains information such as:

- Application ID
- Task ID
- Task name
- Task type
- Received time
- Executed time
- Action information
- Task duration

Processing duration is calculated from the difference between task received and executed timestamps.

### `task_history_etl.py`

Builds a more detailed task-history fact dataset.

It extracts:

- Application status
- Task information
- User/designation information
- Location
- Task actions
- Action details
- Processing timestamps
- Current process information
- Processing time in hours

## Database Configuration

Database credentials are intentionally not stored in the repository.

The scripts use the `DATABASE_URL` environment variable.

A template is provided in:

`etl/.env.example`

Example:

`DATABASE_URL=postgresql+psycopg2://USERNAME:PASSWORD@localhost:5432/DATABASE_NAME`

Replace the placeholder values in your local environment only.

## Data Privacy

The original ServicePlus source database and raw operational data are not included in this repository.

The ETL scripts are provided to demonstrate the transformation and data-engineering workflow without exposing restricted source data.
