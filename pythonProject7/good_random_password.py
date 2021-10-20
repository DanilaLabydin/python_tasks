##
# create a program that generate a good password + displays the number of attempts
# the password is good if: it contains s at least 8 characters long, at least one uppercase letter,
# at least one lowercase letter and at least one number
#
from password_check_f import password_check
from Random_Password import random_pasword

##
# generate a good random password
# @return good_password the good password
#
def good_password_nb():
    # create a variable total to count the attempts
    total = 1

    # generate a random
    good_pass = random_pasword()

    # create a loop to create a right password and count the attempts
    while password_check(good_pass) is False:
        total += 1
        good_pass = random_pasword()

    # display the total and the result
    print(total)
    return good_pass

# create a main program to demonstrate the function
def main():
    print(good_password_nb())

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()

