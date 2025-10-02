# Week 3: Line of Best Fit with Unit Testing

## Structure

```
DAT45501_Portfolio/
│
├─ labs/
│   └─ week_03/
│       ├─ best_fit_line.py
│       └─ tests/
│           └─ test_fitting.py
```

1. `best_fit_line.py`: Holds the two functions that make up a plot of a scatter plot with a line of best fit.
2. `test_fitting.py`: Holds the the Test Case for the values of the line of best fit, making up different unit tests for:
   1. happy paths (linear data)
   2. edge cases (linear data but negative slope and 2 points each)
   3. sad paths (to-do)

## `best_fit_line`

This file is responsible for calculating a line of best fit to go along with scatter plot, that has **linear** data

### Functions

#### `fit_line(x, y)`

It works by calling on **np.polyfit** on the numpy arrays provided, representing x,y coords, and the degree of the polynomial, in this case 1.

It unpacks the result of this, which are the coefficients of the slope and intercept. It then calculates the line of best fit to use (slope \* x + intercept).

#### `plot_line(x, y, y_pred)`

This function is repsonsible for plotting the scatter plot (x, y) along with the linear line of best fit (y = ax + b).

### Script-level Code

1. Initialises x, which represents months in the year
2. Initialises the variables slope and intercept, which makes up the actual slope and intercept. This is used to calculate the y coordinates
3. Artifically adds noise to the y array via random distribution, and adds this onto the y array
4. Calls the function to get the line of best fit on x and y, and plots the line of best fit. The coefficients of the line of best fit should match up to our slope and intercept, which is tested in: `tests/test_fitting.py`
