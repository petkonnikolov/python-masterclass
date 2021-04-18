

def sum_numbers(*values: float) -> float:
    """Sum up all passed numbers

    Returns:
        float: passed number values
    """
    sumof = 0
    for i in values:
        sumof += i

    return sumof


print(sum_numbers(12.5, 3.147, 98.1))
