# Calendar printer for terminal

week_list = ["S", "M", "T", "W", "T", "F", "S"]


def calendar_printer():
    bad_input = True
    while bad_input:
        try:
            days_in_month = int(input("How many days in the month? "))
            if not 28 <= days_in_month <= 31:
                print("Enter a realistic number of days (28-31)")
                continue
            bad_input = False
        except ValueError:
            print("Please enter a valid number")

    bad_input = True
    while bad_input:
        try:
            start_day = int(
                input(
                    "What day of the week does the month start on? (1=Sun, 2=Mon, 3=Tue, ..., 7=Sat"
                )
            )
            if not 1 <= start_day <= 7:
                print("Not between 1 and 7, try again")
                continue
            bad_input = False
        except ValueError:
            print("Please enter a valud umber")

    lines = []
    # Print the fixed header
    lines.append("   ".join(week_list))

    # Create leading spaces before the 1st day
    num_list = ["--"] * (start_day - 1)

    # Add each day number
    for i in range(1, days_in_month + 1):
        num_list.append(
            f"{i:2}"
        )  # width of 2 so its double and singe digits are aligned

        # Every 7 days, print a new week
        if len(num_list) == 7:
            lines.append("  ".join(num_list))
            num_list = []

    # Print remaining days + dashes for empty slots
    if num_list:
        num_list += ["--"] * (7 - len(num_list))
        lines.append("  ".join(num_list))

    print("\n".join(lines))
    return lines


lines = calendar_printer()
