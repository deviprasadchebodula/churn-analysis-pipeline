# Telecom Customer Churn — EDA Pipeline

A modular, stage-based exploratory data analysis (EDA) pipeline built in Python and object-oriented design, applied to a telecom customer churn dataset. Each stage of the analysis — reading, cleaning, tabulating, summarizing, and visualizing — is implemented as an independent, reusable class, connected through a single orchestrator script.

## Overview

Raw customer data rarely arrives clean. This project demonstrates a disciplined approach to EDA: separating data ingestion, missing-value handling, and analysis into distinct, testable stages rather than one monolithic script. The result is a pipeline that is easy to debug, easy to extend to new datasets, and easy to explain to a reviewer one stage at a time.

## Pipeline Architecture

```
data_read.py ──▶ missing_data.py ──┬──▶ tables_data.py ──▶ charts.py   (frequency bar chart)
                                     ├──▶ describe.py     ──▶ charts.py   (histogram)
                                     └──▶ correlation.py                 (correlation matrix)
```

| Stage | File | Responsibility |
|---|---|---|
| 1. Ingestion | `data_read.py` | Load the raw CSV into a DataFrame |
| 2. Cleaning | `missing_data.py` | Detect and fill missing values (median for numeric, "Unknown" for categorical) |
| 3a. Frequency analysis | `tables_data.py` | Value counts for categorical columns |
| 3b. Summary statistics | `describe.py` | Mean, std, quartiles for numeric columns |
| 3c. Correlation analysis | `correlation.py` | Pairwise correlation matrix, ranked against churn |
| 4. Visualization | `charts.py` | Bar charts (frequency) and histograms (distribution) |
| Orchestrator | `main.py` | Connects every stage in sequence |

Each stage takes the previous stage's output as its only input — no shared global state, no re-reading files mid-pipeline.

## Dataset

`telecom_churn_data.csv` — 2,000 customer records, 16 features including demographics, subscription usage (minutes watched, support calls), and a binary `churn` label.

## Key Finding

Correlation analysis against the `churn` column shows customer support call volume and weekly usage minutes as the strongest (positive) predictors of churn in this dataset — a starting point for further modeling.

## Tech Stack

- Python 3.12
- pandas — data loading and manipulation
- matplotlib — visualization

## How to Run

```bash
git clone <repo-url>
cd telecom-churn-pipeline
pip install pandas matplotlib
python main.py
```

Running `main.py` executes the full pipeline end to end: loads the CSV, cleans missing values, generates frequency and distribution charts, and prints the correlation ranking against churn.

## Project Structure

```
.
├── data_read.py
├── missing_data.py
├── tables_data.py
├── describe.py
├── correlation.py
├── charts.py
├── main.py
├── telecom_churn_data.csv
└── outputs/
    ├── freq_gender.jpg
    └── hist_age.jpg
```

## Author

Dev Prasad Chebodula
