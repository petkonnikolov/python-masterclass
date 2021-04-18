sentence = input('Please enter the sentense here: ')


def palindrone_sentence(sentence):
    # letter_lst = []
    # for item in sentence:
    #     if item.isalnum():
    #         char = item.casefold()
    #         letter_lst.append(char)
    #     else:
    #         continue
    string = ''
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()


print(palindrone_sentence(sentence))
