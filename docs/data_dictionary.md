# Online Retail Dataset — Data Dictionary

This data dictionary defines the columns in the transactional dataset stored in `data/raw/online_retail.csv`.

## Dataset Overview
- **File:** `data/raw/online_retail.csv`
- **Encoding:** `ISO-8859-1`
- **Grain:** One row per invoice line item (an invoice can contain multiple products/SKUs)
- **Columns:** 8

## Data Quality Notes (Observed in Raw File)
- `CustomerID` is frequently missing (~25% of rows), indicating anonymous/unattributed transactions.
- `Description` is rarely missing (<1%), but may include whitespace or inconsistent formatting.
- `InvoiceNo` includes cancellation invoices prefixed with `C`.
- `Quantity` may be negative (returns/cancellations) and can include extreme outliers.
- `UnitPrice` is generally positive but may contain zeros and rare negative/outlier values.

## Column Definitions

| Column | Type (raw CSV) | Description | Example | Notes / Constraints |
|---|---|---|---|---|
| `InvoiceNo` | string | Invoice identifier for a transaction event. Multiple rows can share the same invoice number (one per line item). | `536365`, `C536379` | Cancellation invoices commonly start with `C`. Not a unique key by itself. |
| `StockCode` | string | Product/SKU code identifying the item sold. | `85123A` | Alphanumeric codes are possible. Treat as text (do not coerce to numeric). |
| `Description` | string | Human-readable product description. | `WHITE HANGING HEART T-LIGHT HOLDER` | Nullable in a small fraction of records. May contain trailing spaces or punctuation differences across rows. |
| `Quantity` | integer | Number of units for the line item. | `6`, `-1` | Negative values can represent returns/cancellations. Extreme values may exist; validate ranges for your use case. |
| `InvoiceDate` | string (datetime-like) | Timestamp when the invoice was generated. | `2010-12-01 08:26:00` | Recommended to parse to datetime (format resembles `YYYY-MM-DD HH:MM:SS`). Timezone is not specified in the file. |
| `UnitPrice` | float | Price per unit for the line item. | `2.55` | May include zeros and rare negative/outlier values. Consider filtering non-positive prices if analyzing sales revenue. |
| `CustomerID` | float (nullable; integer-like) | Customer identifier. | `17850` | Stored as float in CSV due to missing values. Treat as nullable integer for analytics. Not all transactions are attributable to a customer. |
| `Country` | string | Customer country. | `United Kingdom` | Categorical field; common non-UK values include `Netherlands`, `Germany`, and `EIRE`. |

## Recommended Usage Notes
- **Order-level metrics:** Aggregate line items by `InvoiceNo` (and optionally `CustomerID`, `InvoiceDate`).
- **Revenue calculations:** When appropriate, compute revenue as `Quantity * UnitPrice`, but decide whether to include cancellations/returns and non-positive prices based on your analysis objective.
- **Customer analytics:** Restrict to non-null `CustomerID` for customer-level segmentation and retention metrics.
