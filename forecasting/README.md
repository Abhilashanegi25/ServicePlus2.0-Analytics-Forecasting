# Forecasting

This directory contains the forecasting notebooks and selected forecasting outputs generated during the ServicePlus analytics project.

The forecasting component uses historical application data to study demand patterns and generate future forecasts.

## Forecasting Workflow

The overall process follows:

Historical Data
→ Data Preparation
→ Feature Engineering
→ Model Development
→ Model Comparison
→ Forecast Generation
→ Forecast Evaluation
→ State-Level Analysis

## Forecasting Notebooks

### `forecasting.ipynb`

Contains the main forecasting and modelling workflow.

The notebook documents the analytical process used to prepare the data, develop forecasting models and generate forecast-related outputs.

### `forecast.ipynb`

Contains additional forecasting analysis and forecast-generation work.

## Forecasting Models

The project includes modelling work involving:

- ARIMA
- SARIMA
- LightGBM

The models were evaluated and compared as part of the forecasting workflow.

## Forecasting Outputs

The `results/` directory contains selected outputs generated during the forecasting analysis.

### `model_comparison.csv`

Contains the comparison of forecasting models and their evaluation results.

### `actual_vs_forecast.csv`

Contains historical actual values alongside forecast values for comparison.

### `forecast_confidence_intervals.csv`

Contains forecast values together with confidence/uncertainty intervals.

### `feature_importance.csv`

Contains feature-importance information generated during the modelling workflow.

### `lightgbm_feature_importance.csv`

Contains feature-importance results specifically associated with the LightGBM model.

### `top_states_forecast.csv`

Contains selected state-level forecasting results.

### `forecast_change_kpi.csv`

Contains forecast-change KPI information derived from the forecasting outputs.

## Forecasting Analysis

The forecasting component was used to support analysis of:

- Historical application demand
- Future application trends
- Model performance
- Forecast uncertainty
- State-level demand
- Important predictive features
- Changes between forecast periods

## Results

The generated CSV outputs provide a compact representation of the forecasting results without requiring access to the original internship database.

The notebooks and outputs are included to demonstrate the modelling workflow and analytical results.

## Data Privacy

The original ServicePlus source dataset is not included in this repository.

The forecasting notebooks and selected result files are provided without exposing the restricted source database or raw operational records.
