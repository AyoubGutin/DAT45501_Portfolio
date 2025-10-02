# -- Imports --
import numpy as np
import matplotlib.pyplot as plt


# -- Linear Line of Best Fit Function --
def fit_line(x: np.array, y: np.array):
    """
    args:
        x: (numpy array) Array of x coordinates / values
        y: (numpy array) Array of y coordinates / values

    returns:
        slope, intercept, y_pred: (tuple)
            - slope: (float) slope of the line of best fit
            - intercept: (float) y-intercept of the line of best fit
            - y_pred (numpy array) Coordinates of the line of best fit

    """
    coefficients = np.polyfit(x, y, 1)  # 1 means its linear e.g y = 5x + 2

    slope, intercept = coefficients
    y_pred = slope * x + intercept  # define the new expression for line of best fit

    return slope, intercept, y_pred


# -- Plot the Line of Best Fit along a scatter plot --
def plot_line(x: np.array, y: np.array, y_pred: np.array):
    """
    Displays the scatter plot along with line of best fit

    args
        x: (numpy array) X coordinates / values
        y: (numpy array) Y coordinates / values
        y_pred (numpy array) Line of best fit coordinates
    """
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.plot(x, y_pred)

    ax.set_xlabel("Months")
    ax.set_ylabel("Sales")

    ax.set_title("Monthly Sales with Line of Best Fit")

    plt.show()


if __name__ == "__main__":
    # Linear Data
    months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    slope_actual = 2
    intercept_actual = 40

    # Get Noise
    noise_level = 2
    np.random.seed(42)
    sales = slope_actual * months + (
        intercept_actual + np.random.normal(0, noise_level, size=months.shape)
    )

    slope, intercept, y_pred = fit_line(months, sales)
    print(slope, intercept)
    plot_line(months, sales, y_pred)
