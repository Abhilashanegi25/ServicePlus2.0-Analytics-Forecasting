# Data Warehouse

This directory contains the data-warehouse-related structure and selected transformed datasets used for ServicePlus analytics.

The warehouse follows a fact-and-dimension approach designed to support analytical queries across applications, services, departments, locations, statuses and workflow activity.

## Warehouse Structure

The main components are:

- `sample_data/` — selected non-raw datasets representing transformed fact and dimension tables
- `schema/` — documentation of the analytical data model

## Fact Tables

### Fact Application

The application-level fact dataset contains one record per application and includes fields such as:

- Application ID
- Applicant key
- Service key
- Application reference number
- Submission date
- Due date
- State

This table supports application-level metrics and trend analysis.

### Fact Task History

The task-history fact dataset represents workflow/task-level activity associated with applications.

It contains information including:

- Task history key
- Application ID
- Application status
- Task name
- Task type
- Designation
- Location
- User information
- Task action
- Action details
- Received time
- Executed time
- Current process ID
- Processing time

### Fact Workflow

The workflow dataset contains application-level workflow execution information, including:

- Application ID
- Task name
- User name
- Received time
- Executed time
- Action details

## Dimension Tables

### Service Dimension

Contains service-related attributes such as:

- Service key
- Service ID
- Base service ID
- Service name
- Department ID
- Department name
- State

### Department Dimension

Contains department-level information used for departmental analysis.

### Location Dimension

Contains submission-location information.

### Status Dimension

Contains application-status values used for status analysis.

### Applicant Dimension

Contains selected applicant-related attributes used in the analytical model.

Because the original source data may contain personally identifiable information, only selected transformed/sample outputs are included in this repository.

## Data Model

The overall analytical structure can be represented as:

```text
                    ┌─────────────────┐
                    │  Dim Service    │
                    └────────┬────────┘
                             │
                             │
┌─────────────────┐          ▼          ┌─────────────────┐
│ Dim Applicant   │ ───► Fact Application ◄── Dim Status │
└─────────────────┘                     └─────────────────┘
                             │
                             ▼
                    Fact Task History
                             │
                             ▼
                     Workflow Analysis

       Dim Department ──► Dim Service
       Dim Location   ──► Fact / Workflow Analysis
