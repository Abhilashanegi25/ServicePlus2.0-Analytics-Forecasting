# Data Warehouse Schema

The analytical data warehouse follows a fact-and-dimension structure designed to support application, service, department, location, status, and workflow analysis.

## Fact Tables

### fact_application

Application-level records containing application identifiers, service information, submission dates, due dates, state information, and completion information.

### fact_task_history

Task-level workflow records containing task details, execution timestamps, actions, user/designation information, and processing-time measures.

### fact_workflow

Workflow-level analytical records used for workflow and process analysis.

## Dimension Tables

### dim_applicant
Applicant-related reference information.

### dim_department
Department and department-related service information.

### dim_location
Location reference information.

### dim_service
Service and service-category information.

### dim_status
Application/status reference information.

## Purpose

The warehouse structure separates measurable transactional/workflow information from descriptive attributes, making the data easier to query and use for analytical dashboards and reporting.
