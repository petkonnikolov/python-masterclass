# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alpha_set = set(alphabet)
vowels = 'aeiouy'
vowel_set = set(vowels)
# consonant_set = alpha_set.difference(vowel_set)

# print(alpha_set)
# print(vowel_set)
# print(consonant_set)

text = input("Please enter some text: ")
input_set = set(text)

non_vowel_set = sorted(input_set.difference(vowel_set))

print(non_vowel_set)