# Global Retail Analytics & Strategic Growth Plan
**Final Project Report**

---

## Section 1: Cover Page

*   **Project Title:** Global Retail Analytics & Strategic Growth Plan
*   **Sector:** E-commerce / Retail
*   **Team Members:**
    *   **Saloni:** Project Lead + Business Owner
    *   **Sakina:** Data Engineer (ETL Lead)
    *   **Sushant:** Analysis + Statistics Lead
    *   **Sahil:** Dashboard + Visualization Lead
    *   **Saniya:** Business + Report + Presentation Lead
*   **Institute:** Newton School of Technology
*   **GitHub Repository URL:** [shalini-saloni/capstone-project2](https://github.com/shalini-saloni/capstone-project2)
*   **Tableau Public Dashboard URL:** [Link to Dashboard]
*   **Submission Date:** April 26, 2026

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

The retail sector operates in a highly dynamic environment characterized by variable demand patterns, price sensitivity, and strong competition across geographies and channels. In this context, data-driven decision-making is essential to align inventory, pricing, promotions, and customer engagement with actual purchasing behavior rather than assumptions.

This project analyzes approximately 18.5K orders, 5.2M units sold, and 8.9M in revenue to support commercial decision-making. The findings indicate a clear upward revenue trajectory with pronounced peaks in November-December and observable dips in months such as February and April. The analysis also shows that revenue contribution is concentrated among a relatively small group of high-value customers and that country-level performance is uneven, with the UK, Netherlands, and Germany generating the highest revenue.

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

*   **Source:** Online Retail Dataset (UCI Machine Learning Repository).
*   **Structure:** 541,909 raw records and 8 columns.
*   **Time Period:** December 1, 2010, to December 9, 2011.
*   **Key Fields:**
    *   `InvoiceNo`: Unique identifier for each transaction.
    *   `StockCode`: Product identifier.
    *   `Description`: Item name.
    *   `Quantity`: Number of units per transaction.
    *   `InvoiceDate`: Date and time of purchase.
    *   `UnitPrice`: Price per unit in GBP.
    *   `CustomerID`: Unique customer identifier.
    *   `Country`: Customer's country of residence.

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

## Section 7: KPI & Metric Framework

| KPI | Definition | Business Value |
| :--- | :--- | :--- |
| **Total Revenue** | Sum of (Quantity × Price) | Measures overall commercial scale. |
| **AOV (Avg Order Value)** | Total Revenue / Unique Invoices | Indicates basket health and upsell success. |
| **Retention Rate** | % of customers returning month-over-month | Measures loyalty and platform stickiness. |
| **RFM Score** | Composite score of Recency, Frequency, Monetary | Identifies high-value vs. at-risk segments. |

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

## Section 10: Tableau Dashboard Design

The visualization suite was built to support two levels of decision-making:
1.  **Executive Summary View:** Real-time tracking of Total Revenue, AOV, and Active Customers against monthly targets.
2.  **Operational Drill-down:** Filterable views by Country and Segment to allow Sales Managers to identify localized underperformance.

*Reference: screenshots available in `tableau/screenshots/`*

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

## Section 13: Impact Estimation

| Outcome Area | KPI | Estimated 12-18 Month Impact | Primary Drivers |
| --- | --- | --- | --- |
| Revenue Growth | Annual revenue growth rate | 6%-10% uplift | Seasonal planning and segment-led campaigns. |
| Customer Retention | Retention rate | 5-9 percentage-point improvement | Key-customer retention program. |

---

## Section 14: Limitations

*   **Macro Factors:** Historical data does not account for future inflation or competitive shifts.
*   **Data Attributes:** Lack of customer demographics (age, gender) limits deep personalization.
*   **Attribution:** Revenue concentration findings identify *what* happened, but not the *why* (e.g., specific campaign exposure).

---

## Section 15: Future Scope

*   **Demand Forecasting:** Build predictive models at the SKU-country level.
*   **Churn Prediction:** Develop propensity models to flag customers before they leave.
*   **A/B Testing:** Integrate a testing framework to validate promotion effectiveness.

---

## Section 16: Conclusion

This project transformed raw transactional data into a strategic growth roadmap. By bridging the gap between data engineering (Python ETL) and business visualization (Tableau), we identified that the business's path to sustainability lies in **protecting high-value segments** and **mitigating seasonal volatility**. The recommended actions, if implemented, are projected to drive a significant revenue uplift and stabilize operational planning.

---

## Section 17: Appendix

*   **Data Dictionary:** [docs/data_dictionary.md](file:///Users/shalinisaloni/capstone-project2/docs/data_dictionary.md)
*   **ETL Pipeline:** [notebooks/02_cleaning.ipynb](file:///Users/shalinisaloni/capstone-project2/notebooks/02_cleaning.ipynb)
*   **Statistical Logic:** [notebooks/04_statistical_analysis.ipynb](file:///Users/shalinisaloni/capstone-project2/notebooks/04_statistical_analysis.ipynb)

---

## Section 18: Contribution Matrix (Mandatory)

| Team Member | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Saloni** | Primary | | Primary | | | | |
| **Sakina** | | Primary | | | | | |
| **Sushant** | | | Support | Primary | | | |
| **Sahil** | | | | | Primary | | |
| **Saniya** | | | | | | Primary | Primary |


