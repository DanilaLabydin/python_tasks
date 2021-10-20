##
# create a program that checks whether the password is good or not
# the password is good if: it contains s at least 8 characters long, at least one uppercase letter,
# at least one lowercase letter and at least one number
#
MIN_LEN = 8
UPPER_LETTER_MIN = 65
UPPER_LETTER_MAX = 90
LOWER_LETTER_MIN = 97
LOWER_LETTER_MAX = 122
DIGIT_MIN = 48
DIGIT_MAX = 57

# create a function that checks the password
# @return string the password
# @return TRUE/FALSE
def password_check(string):
    # check the len of the password
    if len(string) < MIN_LEN:
        return False

    # create a for loop to compare the string with ours criteria
    upper_score = 0
    lower_score = 0
    digit_score = 0
    for i in range(len(string)):
        if ord(string[i]) in range(UPPER_LETTER_MIN, UPPER_LETTER_MAX + 1):
            upper_score = 1
        if ord(string[i]) in range(LOWER_LETTER_MIN, LOWER_LETTER_MAX + 1):
            lower_score = 1
        if ord(string[i]) in range(DIGIT_MIN, DIGIT_MAX + 1):
            digit_score = 1

    # if all criteria is 1, return True, otherwise - False
    if upper_score and lower_score and digit_score != 0:
        return True
    else:
        return False

# create a main program to demonstrate the function
def main():
    password = input('Enter the password: ')
    result = ''
    if password_check(password) is True:
        result = 'good'
    else:
        result = 'bad'
    print(f'This is a {result} password')

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()

