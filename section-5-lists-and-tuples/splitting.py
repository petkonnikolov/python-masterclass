generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']

values = ''.join(generated_list)
print(values)

value_list = values.split()
print(value_list)

for item in range(len(value_list)):
    value_list[item] = int(value_list[item])
print(value_list)

int_list = []
for item in value_list:
    int_list.append(int(item))
print(int_list)