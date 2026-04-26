"""ETL pipeline for the Online Retail capstone project.

This script loads the raw dataset, performs basic exploration, cleans the data,
engineers revenue and date features, validates the final output, and saves the
cleaned dataset to the processed data directory.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "online_retail.csv"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DATA_PATH = PROCESSED_DATA_DIR / "cleaned_data.csv"


def load_data(input_path: Path) -> pd.DataFrame:
	"""Load the raw retail dataset using the correct encoding."""
	if not input_path.exists():
		raise FileNotFoundError(f"Input file not found: {input_path}")

	return pd.read_csv(input_path, encoding="ISO-8859-1")


def explore_data(df: pd.DataFrame) -> None:
	"""Print a quick initial profile of the raw dataset."""
	print("Head of raw data:")
	print(df.head())
	print()

	print("Raw data info:")
	df.info()
	print()

	print("Missing values by column:")
	print(df.isna().sum().sort_values(ascending=False))
	print()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
	"""Clean the dataset by handling missing values, invalid rows, and duplicates."""
	cleaned_df = df.copy()

	cleaned_df = cleaned_df.dropna(subset=["CustomerID", "Description"])
	cleaned_df = cleaned_df[cleaned_df["Quantity"] >= 0]
	cleaned_df = cleaned_df.drop_duplicates()

	cleaned_df["InvoiceDate"] = pd.to_datetime(cleaned_df["InvoiceDate"], errors="coerce")
	cleaned_df = cleaned_df.dropna(subset=["InvoiceDate"])

	cleaned_df["CustomerID"] = cleaned_df["CustomerID"].astype("Int64")
	cleaned_df["InvoiceNo"] = cleaned_df["InvoiceNo"].astype(str)
	cleaned_df["StockCode"] = cleaned_df["StockCode"].astype(str)
	cleaned_df["Country"] = cleaned_df["Country"].astype(str)

	return cleaned_df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
	"""Create revenue and date-based features."""
	engineered_df = df.copy()
	engineered_df["Revenue"] = engineered_df["Quantity"] * engineered_df["UnitPrice"]
	engineered_df["InvoiceMonth"] = engineered_df["InvoiceDate"].dt.month
	engineered_df["InvoiceYear"] = engineered_df["InvoiceDate"].dt.year
	return engineered_df


def validate_data(df: pd.DataFrame) -> None:
	"""Print final validation details for the cleaned dataset."""
	print(f"Final dataset shape: {df.shape}")
	print("Final dataset info:")
	df.info()


def save_data(df: pd.DataFrame, output_path: Path) -> None:
	"""Save the cleaned dataset to disk."""
	output_path.parent.mkdir(parents=True, exist_ok=True)
	df.to_csv(output_path, index=False)
	print(f"Cleaned dataset saved to: {output_path}")


def main() -> None:
	"""Run the full ETL pipeline."""
	raw_df = load_data(RAW_DATA_PATH)

	print(f"Loaded shape: {raw_df.shape}")
	print()

	explore_data(raw_df)

	rows_before = len(raw_df)
	cleaned_df = clean_data(raw_df)
	rows_after_cleaning = len(cleaned_df)

	print(f"Rows before cleaning: {rows_before}")
	print(f"Rows after cleaning: {rows_after_cleaning}")
	print()

	processed_df = engineer_features(cleaned_df)

	print("Feature engineering preview:")
	print(processed_df[["InvoiceDate", "InvoiceMonth", "InvoiceYear", "Quantity", "UnitPrice", "Revenue"]].head())
	print()

	validate_data(processed_df)
	save_data(processed_df, PROCESSED_DATA_PATH)


if __name__ == "__main__":
	main()
