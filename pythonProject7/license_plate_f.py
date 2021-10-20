##
# create a program that generates and displays the License Plate
#
from random import randint
DIGIT_MIN_ASCII = 48
DIGIT_MAX_ASCII = 57
LETTER_MIN_ASCII = 65
LETTER_MAX_ASCII = 90

# create a function that generates a license plate
# return a license plate
def license_plate():
    # determine the type of license: old(3 letters and 3 digits) or new (4 digits and 3 letters)
    len_letter = 3
    first_part = ""
    second_part = ""
    if randint(0,1) == 0:
        len_digit = 3
        for i in range(len_letter):
            character = str(chr(randint(LETTER_MIN_ASCII, LETTER_MAX_ASCII)))
            first_part += character
        for k in range(len_digit):
            character= str(chr(randint(DIGIT_MIN_ASCII, DIGIT_MAX_ASCII)))
            second_part += character

    else:
        len_digit = 4
        for i in range(len_letter):
            character = str(chr(randint(LETTER_MIN_ASCII, LETTER_MAX_ASCII)))
            second_part += character
        for k in range(len_digit):
            character= str(chr(randint(DIGIT_MIN_ASCII, DIGIT_MAX_ASCII)))
            first_part += character

    # return the result
    return first_part + second_part

# create a main program to demonstrate the function
def main():
    print(license_plate())

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()


