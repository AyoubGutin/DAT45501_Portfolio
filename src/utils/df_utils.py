# Utility functions for handling a dataframe

import pandas as pd
import numpy as np
import csv
from typing import Dict, Any


def detect_delimiter(file_path: str, encoding: str = "utf-8"):
    """
    Detects delimiters in a csv using the CSV sniffer.
    This is built into pandas read_csv when sep is None, but wanted to build it on my own to understand how it uses and calls csv.Sniffer

    params:
        file_path (str): File path of the csv
        encoding (str): Encoding of the csv file, default is utf-8 which is standard
    """
    try:
        with open(file_path, mode="r", newline="", encoding=encoding) as f:
            sample = f.read(1024)
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            return dialect.delimiter
    except Exception as e:
        print(f"Error sniffing the file: {e}")
        return None


def create_df(
    file_path: str,
    extension: str,
    sep: str = None,
    header: int = 0,
    encoding: str = "utf-8",
    parse_dates: list = None,
    skiprows: list | int = None,
) -> pd.DataFrame:
    """
    Custom util function to create a pandas dataframe from a csv or excel file.
    Covers most cases

    args:
        file_path (str): File path of the csv or excel file
        extension (str): File extension 'csv', 'xls', 'xlsx', etc.
        sep (str): CSV delimiter, default is ','
        header (int): Row number for header, default is 0
        encoding (str): Encoding for CSV files, default 'utf-8'
        parse_dates (list or None): Columns to parse as dates
        skiprows (list or int or None): Rows to skip at the start of the file

    returns:
        A pandas dataframe
    """
    supported_excel_ext = ["xls", "xlsx", "xlsm", "xlsb"]
    sep = detect_delimiter(file_path=file_path, encoding=encoding)
    df = pd.DataFrame()
    try:
        if extension.lower() == "csv":
            df = pd.read_csv(
                file_path,
                sep=sep,
                header=header,
                encoding=encoding,
                parse_dates=parse_dates,
                skiprows=skiprows,
            )
        elif extension.lower() in supported_excel_ext:
            df = pd.read_excel(
                file_path, header=header, parse_dates=parse_dates, skiprows=skiprows
            )

    except Exception as e:
        print(f"Error loading file: {e}")

    return df


def df_report(df: pd.DataFrame) -> None:
    """
    Conduct EDA on dataframes and generate a report

    args:
        df (pd.DataFrame) The DataFrame to analyse

    """
    format_sep = "+-" * 10

    # Shape
    print(f"{format_sep} SHAPE {format_sep}")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # General Information
    print(f"\n{format_sep}GENERAL INFO{format_sep}")
    df.info()
    print("\n")

    # Null Values
    print(f"{format_sep} NULL VALUE COUNT {format_sep}")
    null_counts = df.isnull().sum()
    null_counts_filtered = null_counts[null_counts > 0].sort_values(ascending=False)
    if null_counts_filtered.empty:
        print("No null values found.")
    else:
        print("Columns with null values:")
        print(null_counts_filtered.head(20).to_string())
        print(f"... and {max(len(null_counts_filtered) - 20, 0)} more.")

    # Duplicate Rows
    print(f"\n{format_sep} NULL VALUE COUNT {format_sep}")
    num_duplicates = df.duplicated().sum()
    if num_duplicates == 0:
        print("No duplicate rows found")
    else:
        print(f"Found {num_duplicates} duplicate rows")

    # Numeric Columns Summary
    print(f"\n{format_sep} NUMERIC SUMMARY {format_sep}")
    try:
        numeric_summary = df.describe(include=[np.number])
    except Exception as e:
        print(f"Possible Error: {e}")
        numeric_summary = pd.DataFrame()
    if numeric_summary.empty:
        print("No numerical columns")
    else:
        print(numeric_summary.to_string())

    # Categorical Columns Summary
    print(f"\n{format_sep} CATEGORICAL SUMMARY {format_sep}")
    categorical_summary = df.describe(include=["object", "category"])
    if categorical_summary.empty:
        print("No categorical columns found")
    else:
        print(categorical_summary.to_string())

    print(f"\n{format_sep} END OF REPORT {format_sep}")


def drop_null_rows(df: pd.DataFrame, subset_cols: list = None) -> pd.DataFrame:
    """
    Drops rows that have null values in a DataFrame

    args:
        df (pd.DataFrame): The dataframe to be cleaed
        subset_cols (list or None): A list of column names to check, if none, all columns are considered
    """
    original_rows = len(df)

    cleaned_df = df.dropna(subset=subset_cols)

    rows_dropped = original_rows - len(cleaned_df)
    print(f"Dropped {rows_dropped} rows that had null values")

    return cleaned_df


def idenitfy_invalid_numerics(df: pd.DataFrame, col: str) -> Dict[str, Any]:
    report = {}
    # Replace invalid values as NaN
    coerced_series = pd.to_numeric(df[col], errors="coerce")

    # get where conversion resulted in a NaN, and locate where this happened via mask
    invalid_mask = coerced_series.isna() & df[col].notna()
    invalid_values = df.loc[invalid_mask, col]

    report[col] = {
        "count": len(invalid_values),
        "unique_values": invalid_values.unique().tolist(),
    }

    return report


def to_numeric(df: pd.DataFrame, subset_cols: list = None) -> pd.DataFrame:
    conversion_report = {}

    df_cleaned = df.copy()

    cols_to_proces = subset_cols if subset_cols is not None else []

    for col in cols_to_proces:
        if df_cleaned[col].dtype == "object":
            df_cleaned[col] = df_cleaned[col].str.replace(",", "", regex=False)
            df_cleaned[col] = df_cleaned[col].str.replace(" ", "", regex=False)

        # identification incorrect numerics and report it
        col_report = idenitfy_invalid_numerics(df_cleaned, col)
        conversion_report.update(col_report)

        # Actual conversion
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce")

        count = conversion_report.get(col, {}).get("count", 0)
        unique_values = conversion_report.get(col, {}).get("unique_values")
        if count > 0:
            print(f"Column {col} had {count} invalid value(s) converted to NaN.")
            print(f"Column {col} invalid values: {unique_values}")

        else:
            print(f"Sucessfully converted Column {col} to numeric")

    return df_cleaned, conversion_report
