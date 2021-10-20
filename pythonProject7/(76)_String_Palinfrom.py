##
# palindrome string
#
# read the dimension from the user
string = input("Enter the phrase: ")

# convert the all phrase into a one world
full_word = string.replace(' ', '')

# compare original world with reverse word and display the result
if full_word == full_word[::-1]:
    print('yes')
else:
    print('no')

