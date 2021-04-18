string = input('Please enter three integers in format "a,b,c": ')

list1 = string.split(sep=',')

for index in range(len(list1)):
    list1[index] = int(list1[index])

# calculation = (list1[0] + list1[1]) - list1[2]

a, b, c = list1

calculation = (a + b) - c

print(calculation)