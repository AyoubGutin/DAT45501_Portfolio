# DAT5501: Analysis Software and Career Practice Portfolio

This repository is a portfolio of Python projects for the DAT5501 module. It demonstrates skills in Python programming, data analysis, and software development best practices like unit testing and version control.

## Projects

Here is an overview of the projects included in this portfolio.

---

### 1. Linear Regression (Line of Best Fit)

This project calculates and plots a line of best fit (linear regression) for a given set of 2D data points using `numpy` and `matplotlib`.

- **Main Code:** `src/data_analysis/best_fit_line.py`
- **Unit Tests:** `tests/test_data_analysis/test_fitting.py`

**Key Functions:**

- `fit_line(x, y)`: Takes two `numpy` arrays (x and y coordinates) and uses `np.polyfit` with a degree of 1 to find the slope and intercept. It returns the calculated slope, intercept, and the predicted y-values for the line.
- `plot_line(x, y, y_pred)`: Uses `matplotlib` to display the original data as a scatter plot and overlay the calculated line of best fit (`y_pred`).

**Testing:**
The `test_fitting.py` file ensures the `fit_line` function is accurate. It includes:

- **Happy Path:** Tests with perfectly linear data.
- **Edge Case:** Tests with only two data points and a negative slope.
- **Sad Path:** Confirms that errors are raised for invalid inputs (e.g., empty arrays).

---

### 2. US Election Analysis

A script for loading and performing initial exploratory data analysis (EDA) on a CSV of 2016 US election data.

- **Main Code:** `src/data_analysis/election_analysis.py`
- **Data:** `data/US-2016-primary.csv`
- **Utility:** `src/utils/create_pandas_df.py`

---

### 3. Basic Python Scripts

A collection of smaller scripts demonstrating core Python concepts.

- **Compound Interest Calculator:**

  - **Code:** `src/basic_python/compound_interest.py`
  - **Tests:** `tests/test_basic_python/test_compound_interest.py`

- **Rectangle Area Calculator:**

  - **Code:** `src/basic_python/calculations.py`
  - **Tests:** `tests/test_basic_python/test_calculations.py`

- **Terminal Calendar Printer:**
  - **Code:** `src/basic_python/calendar_printer.py`
