# Retail Analytics Capstone (Python + Tableau)

## Objective
Build an end-to-end retail analytics workflow that turns raw transactional data into decision-ready insights and a Tableau dashboard.

This capstone focuses on:
- Preparing an analytics-ready dataset (cleaning + feature engineering)
- Understanding revenue trends, seasonality, and market performance
- Segmenting customers (RFM + clustering) to inform CRM strategy
- Delivering insights through a Tableau dashboard and written report

## Team Roles
| Role | Responsibilities | Owner |
|---|---|---|
| Project Lead / Storytelling | Scope, business framing, final narrative, stakeholder-ready outputs | _TBD_ |
| Data Engineer (ETL) | Ingestion, cleaning, feature engineering, data validation, export to `data/processed/` | _TBD_ |
| Data Analyst | EDA, KPI design, statistical analysis, segmentation | _TBD_ |
| BI Developer (Tableau) | Dashboard design, interactivity, publishing, screenshots | _TBD_ |

## Contribution Matrix
| Team Member | Primary Role | Key Contributions | Deliverables |
|---|---|---|---|
| Member 1 | ETL | Data ingestion, cleaning, validation, and feature engineering | Cleaned dataset, ETL workflow, processed exports |
| Member 2 | Analysis | Exploratory data analysis, KPI definition, statistical analysis, and customer segmentation | EDA outputs, analytical findings, segmentation results |
| Member 3 | Dashboard | Tableau dashboard design, chart development, filters, and interaction design | Interactive dashboard, dashboard screenshots |
| Member 4 | Report | Report writing, insight narration, recommendations, and documentation formatting | Final report, documentation, presentation-ready narrative |
| Member 5 | Project Lead | Project coordination, milestone tracking, business framing, and final review | Project plan, consolidated outputs, final submission |

## Dataset Summary
- **File:** `data/raw/online_retail.csv`
- **Grain:** Line-item transactions by invoice and product (SKU)
- **Date range (cleaned):** 2010-12-01 → 2011-12-09
- **Size (cleaned):** 392,732 rows • 18,536 orders • 4,339 customers • 37 countries
- **Core fields:** `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`
- **Engineered fields (cleaned):** `Revenue`, `InvoiceMonth`, `InvoiceYear`
- **Notes:** Source CSV is read using `encoding='ISO-8859-1'` in the cleaning notebook.

## Tools Used
- **Python (Jupyter):** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Segmentation / ML:** scikit-learn (StandardScaler, K-Means)
- **BI & delivery:** Tableau (dashboard + storytelling)
- **Project artifacts:** Markdown/PDF reports, presentation deck

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

## Key Insights (Highlights)
- **Seasonality & volatility:** Revenue peaks in Q4 (especially Oct–Nov), with notable dips in February and April, indicating clear opportunities for targeted low-season recovery campaigns.
- **Customer concentration:** Revenue is disproportionately concentrated in a small cohort (top 10 customers contribute ~17% of customer-attributed revenue; top 50 contribute ~33%).
- **Market mix:** The UK dominates revenue; the Netherlands and Germany are among the strongest non-UK markets, supporting localized growth plans.
- **Segmentation:** RFM features and K-Means clustering separate customers into actionable cohorts for differentiated CRM and offer strategy.

## Tableau Dashboard
- **Dashboard link:** https://drive.google.com/file/d/1_dpIDmuvGNGnANQdHyLr5Xb50fXVX9Qq/view?usp=sharing
- **Screenshots:** `tableau/screenshots/`

### Dashboard Insights
- **KPI summary:** The dashboard reports **18.5K total orders**, **5.2M quantity sold**, and **8.9M total revenue**, showing strong transaction scale and commercial activity.
- **Revenue trend over time:** Monthly revenue starts at **568,101** in January, falls to **446,085** in February, recovers through March and May, and accelerates strongly from August onward.
- **Peak season:** Revenue reaches its highest levels in **September (950,690)**, **October (1,035,642)**, **November (1,156,206)**, and **December (1,087,613)**, confirming a strong Q4 sales concentration.
- **Low-season months:** **February (446,085)** and **April (468,374)** are the weakest months, suggesting potential for targeted recovery campaigns and better demand planning.
- **Top country revenue:** Among the countries shown in the dashboard, **Netherlands (285,446)**, **EIRE (265,262)**, and **Germany (228,678)** generate the highest revenue, followed by **France (208,934)** and **Australia (138,454)**.
- **Customer concentration:** The top customer accounts contribute disproportionately high revenue, led by customer IDs **14646 (280,206)**, **18102 (259,657)**, and **17450 (194,391)**.
- **Business takeaway:** The Tableau view shows that revenue is highly seasonal and concentrated among a relatively small set of customers and markets, making retention, seasonal planning, and country-specific strategy especially important.

## Conclusion
This project builds a reproducible analytics pipeline and dashboard for retail decision-making, surfacing where revenue comes from (seasonality, customers, and countries) and how to act on it (planning, retention, and segment-led campaigns).

For the full narrative and recommendations, see `reports/project_report.md`.
