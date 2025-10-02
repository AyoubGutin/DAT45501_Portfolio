def compound_interest(savings: float, interest: float, years: int) -> float:
    """
    This function:
        1) Tells user when the savings will double using rule of 72
        2) Calculates return on savings year by year compounded
        3) Notifies user when the savings has actually doubled
        4) Returns the total amount, rounded by 2 decimal places

    param:
        savings: (float) The amount a user wants to deposit
        interest: (float) The interest rate per year, annual, as a percentage
        years: (float) The years a user wants to save for

    return:
        The savings amount at end of term, rounded to two decimal places
    """

    # -- Error Checks -
    if savings <= 0:
        raise ValueError("Savings must be greater than 0.")
    if interest < 0:
        raise ValueError("Interest must be greater than 0.")
    if years <= 0:
        raise ValueError("Years must be greater than 0.")

    # -- Setup --
    interest_rate = interest / 100  # e.g. 5% → 0.05
    factor = 1 + interest_rate
    doubled_years = 72 / (interest_rate / 100)
    estimated_outcome = savings * 2
    doubled = False

    print(f"Your savings will double in {doubled_years} years")

    # -- Main Logic --
    for i in range(years):
        # calculate the savings * interest rate
        savings *= factor
        print(f"Year {i + 1}: {savings}")

        # check if the savings have doubled and notify the user only once, hence the double_check
        if not doubled and savings >= estimated_outcome:
            print("Your savings have doubled!")
            doubled = True

    return round(savings, 2)
