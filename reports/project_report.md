# Global Retail Analytics & Strategic Growth Plan
**Final Project Report**

---

## Section 1: Cover Page

*   **Project Title:** Global Retail Analytics & Strategic Growth Plan
*   **Sector:** E-commerce / Retail
*   **Team Name:** VYRA
*   **Team Members:** Shalini Saloni; Sakina Farukh Ahemad; Sushant Kumar Ojha; Sahil Manjhi; Saniya Jabbar Khatik
*   **Faculty Mentor:** _TBD_
*   **Institute:** Newton School of Technology
*   **GitHub Repository URL:** [shalini-saloni/capstone-project2](https://github.com/shalini-saloni/capstone-project2)
*   **Submission Date:** April 28, 2026

---

## Section 2: Executive Summary

This report presents a comprehensive analytics-driven growth strategy for a global online retail business. Faced with volatile monthly revenue and high customer concentration, the project utilized a multi-stage pipeline—from Python-based ETL to advanced statistical clustering—to uncover actionable growth levers.

**Key Findings:**
*   **Seasonal Peaks:** Revenue is heavily concentrated in Q4 (November-December), driven by holiday demand, while significant dips occur in February and April.
*   **Market Concentration:** Over 80% of revenue originates from the UK, though high-growth potential is evident in Germany and the Netherlands.
*   **Customer Loyalty:** A small cohort of high-value customers (Champions) contributes to the majority of the revenue, highlighting a critical need for retention strategies.

**Top Recommendations:**
*   Implement a **Segmented CRM Strategy** to target at-risk high-value customers.
*   Adopt a **Seasonal Commercial Calendar** to manage inventory and demand fluctuations.
*   Optimize **Market-Specific Assortments** in top-performing European regions.

---

## Section 3: Sector & Business Context

### Sector Overview
The retail sector operates in a highly dynamic environment characterized by variable demand patterns, price sensitivity, and strong competition across geographies and channels. 

### Decision-Maker / Stakeholder
The primary stakeholders for this project include the **Chief Operating Officer (COO)** and **E-commerce Marketing Managers**, who require data-driven evidence to allocate budgets and manage inventory.

### Why This Problem Matters
In this context, data-driven decision-making is essential to align inventory, pricing, promotions, and customer engagement with actual purchasing behavior rather than assumptions. Inefficient planning leads to stockouts during peaks and overstocking during dips.

---

## Section 4: Problem Statement & Objectives

### Problem Definition
The business currently lacks a structured understanding of its customer segments and seasonal demand drivers, leading to inefficient inventory allocation and missed revenue opportunities during low-season months.

### Project Scope
*   **In-Scope:** ETL pipeline development, RFM segmentation, Cohort analysis, and Tableau dashboarding for the 2010-2011 Online Retail dataset.
*   **Out-of-Scope:** Real-time stream processing, supply chain logistics optimization, and individual SKU-level price elasticity modeling.

### Success Criteria
*   Creation of a stable ETL pipeline with 100% data integrity for core fields.
*   Identification of at least 4 distinct customer segments using K-Means clustering.
*   Development of a dashboard that reduces management's time-to-insight for monthly performance reviews.

---

## Section 5: Data Description

*   **Source Citation:** Online Retail Dataset, UCI Machine Learning Repository.
*   **Access Link:** [UCI Machine Learning Repository - Online Retail](https://archive.ics.uci.edu/ml/datasets/online+retail)
*   **Dataset Size & Coverage:** 541,909 raw records across 37 countries.
*   **Time Period:** December 1, 2010, to December 9, 2011.
*   **Key Columns:** `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`.
*   **Data Quality Issues:** High percentage of missing `CustomerID` (~25%) and negative quantities representing returns/cancellations.

---

## Section 6: Data Cleaning & ETL Pipeline

The cleaning pipeline was executed in Python to ensure reproducibility and scale.

1.  **Missing Value Treatment:**
    *   Dropped 135,080 rows with missing `CustomerID` to enable accurate segmentation.
    *   Ensured all `Description` fields were populated.
2.  **Anomaly Removal:**
    *   Removed negative quantities (returns) to focus on gross sales performance.
    *   Identified and removed 5,225 duplicate records.
3.  **Data Type Conversion:**
    *   Converted `InvoiceDate` to datetime format.
    *   Standardized `CustomerID` as integers and identifiers as strings.
4.  **Feature Engineering:**
    *   Calculated `Revenue` = `Quantity` × `UnitPrice`.
    *   Extracted `InvoiceMonth` and `InvoiceYear` for temporal analysis.

---

## Section 7: KPI Framework

| KPI | Definition | Formula | Why It Matters |
| :--- | :--- | :--- | :--- |
| **Total Revenue** | Total commercial value of sales. | $\sum (\text{Quantity} \times \text{UnitPrice})$ | Measures overall business scale and growth. |
| **AOV** | Average Order Value. | $\frac{\text{Total Revenue}}{\text{Total Invoices}}$ | Indicates customer spending behavior and upsell success. |
| **Retention Rate** | Stickiness of the customer base. | $\frac{\text{Returning Customers}}{\text{Total Customers}}$ | Measures loyalty and long-term platform health. |
| **RFM Score** | Customer value segmentation. | $R + F + M$ (Weighted) | Identifies "Champions" vs. at-risk customers. |

---

## Section 8: Exploratory Data Analysis (EDA)

### Key Insights
1.  **Seasonal Dominance:** Revenue surges by over 60% in November compared to the annual average, indicating a heavy reliance on year-end shopping.
2.  **The Pareto Effect:** The top 10 customers contribute roughly 15% of total revenue, creating a "key account" dependency.
3.  **Geographic Reach:** While the UK is the primary market (84% of revenue), the Netherlands and Germany show significantly higher Average Order Values, suggesting more profitable bulk-buying behavior in these regions.
4.  **Peak Hours:** Order volume peaks consistently between 10:00 AM and 3:00 PM, providing a clear window for digital marketing and flash promotions.

---

## Section 9: Statistical Analysis

### Customer Segmentation (RFM + K-Means)
Using K-Means clustering (K=4), we identified four distinct behavior groups:
*   **Champions:** High frequency and high spend. (Priority: Retention/Loyalty).
*   **Loyalists:** Consistent but moderate spenders. (Priority: Upsell).
*   **At Risk:** High-value customers who haven't purchased recently. (Priority: Re-engagement).
*   **Hibernating:** One-time buyers with low spend. (Priority: Low).

### Cohort Analysis
Monthly retention matrices revealed that roughly 20-25% of customers acquired in any given month return for a second purchase, with a gradual decay over 6 months.

---

## Section 10: Dashboard Walkthrough

### Dashboard Objective
To provide a consolidated view of business health for executive review while allowing regional managers to drill down into specific markets.

### Executive View
*   **KPI Scorecard:** Top-line metrics (Revenue, Orders, Customers) at a glance.
*   **Revenue Trend:** Monthly performance tracking against historical data.

### Operational View
*   **Country Deep-Dive:** Map view showing revenue distribution across the globe.
*   **Top Customers/Products:** List views to identify key revenue drivers.

### Filters and Interactivity
*   **Date Range Filter:** To analyze specific quarters or months.
*   **Country Filter:** To isolate specific markets (e.g., UK vs. Germany).
*   **Segment Filter:** To view metrics for specific clusters (e.g., "Champions").

---

## Section 11: Insights Summary (Decision Language)

*   **Insight 1:** Q4 revenue is 3x higher than Q1. **Decision:** Buffer inventory by 40% starting in September.
*   **Insight 2:** "Champions" segment contributes 45% of revenue but makes up only 10% of the base. **Decision:** Launch a dedicated VIP concierge service for this group.
*   **Insight 3:** Thursday is the highest-volume day. **Decision:** Schedule all major email marketing blasts for Wednesday evenings.
*   **Insight 4:** High return rates in specific SKUs (identified in EDA). **Decision:** Review supplier quality or update product descriptions for those items.

---

## Section 12: Recommendations

### 1. Seasonal Demand Management
*   **Insight:** Revenue peaks in November-December and dips in February/April.
*   **Action:** Implement a seasonal commercial calendar including pre-peak inventory buffering and targeted February recovery campaigns.
*   **KPI:** Seasonal revenue variance (%).

### 2. High-Value Customer Retention
*   **Insight:** A small customer group contributes a disproportionately large share of total revenue.
*   **Action:** Launch a key-customer retention program including account-based service and early-access offers.
*   **KPI:** Top-customer retention rate.

---

## Section 13: Limitations and Next Steps

### Data & Method Limitations
*   **Historical Nature:** The 2010-2011 data does not reflect post-pandemic shifts in e-commerce behavior.
*   **Attribute Gap:** Lack of customer demographic data (age, gender) limits the depth of personalization in the "Recommendations" phase.
*   **Static Analysis:** The K-Means clustering is a snapshot; customer behavior shifts over time, requiring periodic re-clustering.

### Suggested Future Work
*   **Predictive Forecasting:** Build an ARIMA or Prophet model to forecast Q4 inventory needs more accurately.
*   **Churn Propensity:** Develop a logistic regression model to predict the probability of a "Loyalist" becoming "At Risk".
*   **Tableau Integration:** Link the dashboard to a live database for real-time monitoring.

---

## Section 14: Contribution Matrix (Mandatory)

| Team Member | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Shalini Saloni** | Primary | | Primary | | | | |
| **Sakina Farukh Ahemad** | | Primary | | | | | |
| **Sushant Kumar Ojha** | | | Support | Primary | | | |
| **Sahil Manjhi** | | | | | Primary | | |
| **Saniya Jabbar Khatik** | | | | | | Primary | Primary |


