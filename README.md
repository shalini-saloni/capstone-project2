# Retail Analytics Capstone (Python + Tableau)

## Objective
Build an end-to-end retail analytics workflow that turns raw transactional data into decision-ready insights and a Tableau dashboard.

This capstone focuses on:
- Preparing an analytics-ready dataset (cleaning + feature engineering)
- Understanding revenue trends, seasonality, and market performance
- Segmenting customers (RFM + clustering) to inform CRM strategy
- Delivering insights through a Tableau dashboard and written report

## Team Information
- **Group Name:** VYRA
- **Group Members:** Shalini Saloni; Sakina Farukh Ahemad; Sushant Kumar Ojha; Sahil Manjhi; Saniya Jabbar Khatik
- **Faculty Mentor:** _TBD_

## Team Roles
| Role | Responsibilities | Owner |
|---|---|---|
| Project Lead / Storytelling | Scope, business framing, final narrative, stakeholder-ready outputs | Shalini Saloni |
| Data Engineer (ETL) | Ingestion, cleaning, feature engineering, data validation, export to `data/processed/` | Sakina Farukh Ahemad |
| Data Analyst | EDA, KPI design, statistical analysis, segmentation | Sushant Kumar Ojha |
| BI Developer (Tableau) | Dashboard design, interactivity, publishing, screenshots | Sahil Manjhi |
| Report Writer | Report writing, insight narration, recommendations, and documentation formatting | Saniya Jabbar Khatik |

## Contribution Matrix
| Team Member | Primary Role | Key Contributions | Deliverables |
|---|---|---|---|
| Sakina Farukh Ahemad | ETL | Data ingestion, cleaning, validation, and feature engineering | Cleaned dataset, ETL workflow, processed exports |
| Sushant Kumar Ojha | Analysis | Exploratory data analysis, KPI definition, statistical analysis, and customer segmentation | EDA outputs, analytical findings, segmentation results |
| Sahil Manjhi | Dashboard | Tableau dashboard design, chart development, filters, and interaction design | Interactive dashboard, dashboard screenshots |
| Saniya Jabbar Khatik | Report | Report writing, insight narration, recommendations, and documentation formatting | Final report, documentation, presentation-ready narrative |
| Shalini Saloni | Project Lead | Project coordination, milestone tracking, business framing, and final review | Project plan, consolidated outputs, final submission |

## Dataset Summary
- **File:** `data/raw/online_retail.csv`
- **Grain:** Line-item transactions by invoice and product (SKU)
- **Date range (cleaned):** 2010-12-01 → 2011-12-09
- **Size (cleaned):** 392,732 rows • 18,536 orders • 4,339 customers • 37 countries
- **Core fields:** `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`

## Tools Used
- **Python (Jupyter):** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Segmentation / ML:** scikit-learn (StandardScaler, K-Means)
- **BI & delivery:** Tableau (dashboard + storytelling)

## Folder Structure
```text
capstone-project2/
├─ data/
│  ├─ raw/
│  │  └─ online_retail.csv
│  └─ processed/
│     └─ cleaned_data.csv
├─ docs/
│  └─ data_dictionary.md
├─ notebooks/
│  ├─ 01_extraction.ipynb
│  ├─ 02_cleaning.ipynb
│  ├─ 03_eda.ipynb
│  ├─ 04_statistical_analysis.ipynb
│  └─ 05_final_load_prep.ipynb
├─ reports/
│  ├─ project_report.md
│  ├─ project_report.pdf
│  └─ presentation.pdf
├─ scripts/
│  └─ etl_pipeline.py
└─ tableau/
   └─ screenshots/
```

---

## Project Report Summary

### 1. Cover Page
- **Project Title:** Global Retail Analytics & Strategic Growth Plan
- **Group Name:** VYRA
- **Group Members:** Shalini Saloni; Sakina Farukh Ahemad; Sushant Kumar Ojha; Sahil Manjhi; Saniya Jabbar Khatik
- **Faculty Mentor:** _TBD_

### 2. Executive Summary
This project analyzes 541K records from the UCI Online Retail dataset to optimize inventory and customer retention. Key findings include extreme seasonal volatility in Q4 and high revenue concentration among "Champion" customers.

### 3. Sector & Business Context
- **Sector:** E-commerce / Retail.
- **Stakeholders:** COO and Marketing Managers.
- **Goal:** Shift from assumption-based to data-driven commercial planning.

### 4. Problem Statement
The business lacks structured customer segmentation and seasonal demand forecasting, leading to stockouts and missed revenue.

### 5. Data Description
- **Source:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
- **Key Fields:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country.

### 6. Cleaning & Transformation
- Dropped missing CustomerIDs (~25%).
- Removed returns (negative quantities) for sales analysis.
- Engineered `Revenue` and temporal features.

### 7. KPI Framework
- **Total Revenue**: $\sum (Q \times P)$
- **AOV**: $\frac{Revenue}{Invoices}$
- **Retention Rate**: Loyalty stickiness.

### 8. Exploratory Analysis
- **Seasonality**: November revenue is 60% above average.
- **Pareto Effect**: Top 10 customers drive 15% of revenue.

### 9. Statistical Analysis
- **Method**: K-Means Clustering (K=4) based on RFM scores.
- **Segments**: Champions, Loyalists, At Risk, Hibernating.

### 10. Dashboard Walkthrough
- **Objective**: Health monitoring and regional drill-down.
- **Views**: Executive KPI scorecard and Operational map view.

### 11. Key Insights
- Q4 revenue is 3x higher than Q1.
- Thursday is the highest-volume day for orders.

### 12. Recommendations
- Implement a seasonal inventory buffer (40%) starting in September.
- Launch a VIP concierge service for the "Champions" segment.

### 13. Limitations & Next Steps
- **Limitations**: Historical 2010 data; lack of demographics.
- **Next Steps**: Predictive churn modeling and live data integration.

### 14. Contribution Matrix
| Team Member | Roles |
| :--- | :--- |
| **Shalini Saloni** | Project Lead, EDA |
| **Sakina Farukh Ahemad** | ETL, Data Engineering |
| **Sushant Kumar Ojha** | Analysis, Statistics |
| **Sahil Manjhi** | Dashboard, Visualization |
| **Saniya Jabbar Khatik** | Report, Presentation |

---

For the full detailed narrative, see [reports/project_report.md](file:///Users/shalinisaloni/capstone-project2/reports/project_report.md).
