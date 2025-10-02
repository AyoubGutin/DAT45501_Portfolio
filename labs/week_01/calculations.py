def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Function to calculate a rectangles area by multiplying the length and width

    Args:
        - length (float): The length of the rectangle
        - width (float): The width of the rectangle

    Returns:
        - area (float): The area of the rectangle
    """
    # Check for correct typing
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("length and width must be numbers")

    # Check for correct value
    if width < 0 or length < 0:
        raise ValueError("length and width can't be positive")

    else:
        area = width * length
        return round(area, 2)
