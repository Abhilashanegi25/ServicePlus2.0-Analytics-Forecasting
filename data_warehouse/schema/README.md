# Data Warehouse Schema

This directory documents the analytical schema used for the ServicePlus project.

## Modelling Approach

The project follows a fact-and-dimension modelling approach for analytical workloads.

The model separates:

- Application-level transactional facts
- Workflow/task-level facts
- Descriptive service information
- Department information
- Location information
- Application status
- Applicant-related information

## Core Fact Tables

### Fact Application

Grain: one record per application.

Key fields include:

- `application_id`
- `applicant_key`
- `service_key`
- `appl_ref_no`
- `submission_date`
- `due_date`
- `state`

This table supports application-level metrics, trend analysis and service-level analysis.

### Fact Task History

Grain: one record per application task/history record.

Key fields include:

- `task_history_key`
- `application_id`
- `appl_status`
- `task_name`
- `task_type`
- `designation`
- `location_name`
- `user_name`
- `task_action`
- `task_action_detail`
- `received_time`
- `executed_time`
- `current_process_id`
- `processing_time_hours`

This table supports workflow and operational processing analysis.

## Dimension Tables

### Dim Service

Contains service-level descriptive attributes:

- `service_key`
- `service_id`
- `base_service_id`
- `service_name`
- `department_id`
- `department_name`
- `state`

### Dim Department

Contains department-level information used for departmental analysis.

### Dim Location

Contains submission-location information.

### Dim Status

Contains application-status values.

### Dim Applicant

Contains selected applicant-related attributes used within the analytical model.

## Relationships

Conceptually, the model follows:

```text
Dim Applicant
      │
      │ applicant_key
      ▼
Fact Application
      │
      │ service_key
      ▼
Dim Service
      │
      └── department information

Fact Application
      │
      │ application_id
      ▼
Fact Task History
      │
      ├── task information
      ├── location information
      └── processing-time metrics
