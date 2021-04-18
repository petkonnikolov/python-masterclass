

def factorial(n: int) -> int:
    """Calculating factorial

    Args:
        n (int): input number

    Returns:
        int: factorial number
    """
    if n == 0:
        return 1
    total = 1
    init = 1
    while init <= n:
        fact = init * total
        init += 1
        total = fact
    else:
        return fact


for i in range(0, 36):
    print(i, factorial(i))