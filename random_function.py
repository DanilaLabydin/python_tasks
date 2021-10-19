# generate and display a random password contaning 14 characters
#
# @return a random password(length of between 7 and 10 characters)

from secrets import randbelow
MIN_ASCII = 33
MAX_ASCII = 126
RANGE_UPPER_LOWER_CASE = 92
NUMBER_CHAR = 20

# generate a random password
# @return a random password with 14 characters 
def random_pasword():

    # create a loop to store each character of password
    password = ""
    for i in range(NUMBER_CHAR):
        # ASCII table contains the english alphabet from  33 to 126 numbers, so to represent its in
        # randbelow function (it takes only one argument)
        # you need to do this match (126 - 33) + 33 into a function
        # use the function chr() to represent a number in an ASCII table
        character = str(chr(randbelow(RANGE_UPPER_LOWER_CASE) + MIN_ASCII))

        # add each new character in password's sequence
        password += character

    # return the random password
    return password

# generate and display a random password
def main():
    print(random_pasword())

# call the main function only if the module is not imported
if __name__ == '__main__':
     main()
