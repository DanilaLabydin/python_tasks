##
# determine prime factors of integer
#
number = int(input("Enter an integer (2 or greater): "))

# check whether a number is greater than 2 or not, if not display
# appropriate error message
if number < 2:
    print('Error! you entered a wrong data')
# create a loop to determine the factors
factor = 2
print(f'The prime factors of {number} are:')
while factor <= number:
    if number % factor == 0:
        number = number // factor
        print(factor)
    else:
        factor += 1



