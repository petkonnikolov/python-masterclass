
# def fizz_buzz(s: int, e: int) -> str: 
#     """Return next answer in fizz buzz"""
#     for i in range(s, e):
#         if i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#         elif i % 3 and i % 5 == 0:
#             print("fizz buzz")
#         else:
#             print("{}".format(i))

# fizz_buzz(1, 101)


def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz
 
    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)
 
 
for i in range(1, 101):
    response = input("Provide response for value '{}' :".format(i))
    if response == fizz_buzz(i):
        print("Good Job!")
    else:
        print("Wrong")
        break

