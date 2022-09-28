# Character Counter
# The program will count the number of times a letter occurs in a defined word or phrase

sample_str = "Google.com"
# Set out an empty dictionary where all the letters will be referred to
dict_of_letters = {}
for i in sample_str:
    if i in dict_of_letters:
        dict_of_letters[i] += 1
    else:
        dict_of_letters[i] = 1
# The i variable will be considered in a for long for each character in the sample string. The counter in the
#  conditional statement will display the number of occurrence of each letter
print(str(dict_of_letters))
