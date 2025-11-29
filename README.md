# DAT5501: Analysis Software and Career Practice Portfolio

This repository is a portfolio of Python projects for the DAT5501 module. It demonstrates skills in Python programming, data analysis, and software development best practices like unit testing and version control.

---

## Repository Structure

The code is organised into the following main packages:

- `src/basic_python`: Core Python scripting
- `src/algorithms`: Implementations of classic algorithms, like sorting
- `src/data_analysis`: Notebooks and scripts for traditional data analysis, like plots, EDA, and forecasting
- `src/machine_learning`: Jupyter notebooks for supervised and unsupervised learning
- `src/utils`: Reusable helper functions for working with files and Pandas dataframes made from scratch
- `tests`: Unit tests covering some key modules in `basic_python`, `algorithms`, and `data_analysis`

---

## Projects

Here is an overview of some of the projects included in this portfolio.

### 1. Basic Python Scripts

A collection of smaller scripts demonstrating core Python concepts.

- **Compound Interest Calculator:**

  - **Code:** `src/basic_python/compound_interest.py`
  - **Tests:** `tests/test_basic_python/test_compound_interest.py`

- **Rectangle Area Calculator:**

  - **Code:** `src/basic_python/calculations.py`
  - **Tests:** `tests/test_basic_python/test_calculations.py`

- **Terminal Calendar Printer:**
  - **Code:** `src/basic_python/calendar_printer.py`

### 2. Sorting Algorithms

Implementation and testing of classic comparison sorting algorithms on numeric data

Main Folder: `src/algorithms/sorting/`

- `bubble_sort.py`: Compares and swaps adjacent elements
- `insertion_sort.py`: Builds a sorted list by inserting each new element into the correct position, one at a time
- `selection_sort.py`: Selects minimum element from an unsorted portion, and moves it to the front, one at a time
- `sort_daily_price_change.py`: Sorts and measures time via pandas sorting algorithms, such as quick sort and merge sort, on nasdaq price history.

Tests:

- `tests/test_algorithms/tests_sorted.py`: Verifies each sorting correctly orders lists and handles edge cases and errors

Documentation:

- `src/algorithms/sorting/readme.md`: Describes each sorting algorithm made

### 3. Linear Regression (Line of Best Fit)

This project calculates and plots a line of best fit (linear regression) for a given set of 2D data points using `numpy` and `matplotlib`. It also builds on the knowledge gained, and has supplementary fitting and forecasting of line of best fits w/ a range of degrees.

- **Main Code:** `src/data_analysis/best_fit_line.py`
- **Notebook:** `src/data_analysis/fitting_forecasting.ipynb`. This extends the main code's concepts with more advanced concepts, like polynomials of various degrees, forecasting, and testing the models using metrics like BIC.
- **Unit Tests:** `tests/test_data_analysis/test_fitting.py`

**Key Functions of Main Code:**

- `fit_line(x, y)`: Takes two `numpy` arrays (x and y coordinates) and uses `np.polyfit` with a degree of 1 to find the slope and intercept. It returns the calculated slope, intercept, and the predicted y-values for the line.
- `plot_line(x, y, y_pred)`: Uses `matplotlib` to display the original data as a scatter plot and overlay the calculated line of best fit (`y_pred`).

**Testing of Main Code:**
The `test_fitting.py` file ensures the `fit_line` function is accurate. It includes:

- **Happy Path:** Tests with perfectly linear data.
- **Edge Case:** Tests with only two data points and a negative slope.
- **Sad Path:** Confirms that errors are raised for invalid inputs (e.g., empty arrays).

### 4. US Election Analysis

A script for loading and performing initial exploratory data analysis (EDA) on a CSV of 2016 US election data.

- **Main Code:** `src/data_analysis/election_analysis.py`
- **Data:** `data/US-2016-primary.csv`
- **Utility:** `src/utils/create_pandas_df.py`

### 5. Phishing Classification

Notebook for detecting phishing websites using machine learning.

`src/machine_learning/phishing_classification.ipynb`

- Loading labelled phishing dataset
- Processing the data, making it ready for training (dropping cateogrical columns, shortcut features, etc)
- Training decision tree to distinguish phishing from legitimate
- Evaluating the performance using metrics like accuracy, precision, confusion matrices, and more.
- Plotting decision tree

More information can be found in the notebook markdown

### 6. Customer Value Regression

A project to estimate customer value (lifetime) from customer attributes using supervised learning.

`src/machine_learning/customer_value_regression.ipynb`

- Loading and cleaning a datase
- EDA of features and targets
- Training and evaluating the linear regression model .
- Interpreting coefficients and the importance of features to understand why predictions were made

---

## Getting Started

### Prerequisites

- Python 3.10+ installed
- Install dependencies
  - `pip install -r requirements.txt`

### Running Script

Run scripts as modules so imports work correctly with the project structure.

**Example:**
`python -m src.data_analysis.best_fit_line`

### Running Notebooks

For the jupyter notebooks, running them directly is fine.

### Running Tests

`pytest` to run all tests
