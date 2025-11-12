# This price gets nasdaq price history over a given date, and sorts it
# This for understanding the sort complexities

from src.utils.file_utils import find_root
from src.utils.df_utils import create_df, df_report, to_numeric
import time
import pandas as pd

# -- Setup --
PROJECT_ROOT = find_root()
file_path = PROJECT_ROOT / "data" / "nasdaq-price-hist.csv"
nasdaq_df = create_df(file_path=file_path, extension="csv")

# -- EDA --
df_report(nasdaq_df)

# -- Cleaning --
# convert numeric columns
nasdaq_df_cleaned, _ = to_numeric(
    nasdaq_df, subset_cols=["Open", "High", "Low", "Close"]
)

# -- SORTING --


def pandas_time_sort(df: pd.DataFrame, column: str, ascending: bool = False, kind=None):
    start_time = time.perf_counter()
    df_sorted = df.sort_values(by=column, ascending=False, ignore_index=True, kind=kind)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"\nSORT: {kind}\nEXECUTION TIME: {execution_time:6f}\n")

    return


# Compare sorting algorithms (compatible w/ pandas .sort_values)
sorting_algortihms = ["quicksort", "mergesort", "heapsort"]
for kind in sorting_algortihms:
    pandas_time_sort(df=nasdaq_df, column="Close", kind=kind)
