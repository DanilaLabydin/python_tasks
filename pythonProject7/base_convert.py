##
# create the two functions hex2int and int2hex, that convert between hexadecimal digits
# and decimal integers
# ensure that the hex2int function works correctly for uppercase and lowercase letters
#

# create a function that convert any single hex digits to base-10 digits
# @param value the value to convert
# @return conv_value the converted value
def hex2int(value):
    # determine the nature of each character to convert it
    conv_value = ""
    if value == "0":
        conv_value = "0"
    elif value == "1":
        conv_value = "1"
    elif value == "2":
        conv_value = "2"
    elif value == "3":
        conv_value = "3"
    elif value == "4":
        conv_value = "4"
    elif value == "5":
        conv_value = "5"
    elif value == "6":
        conv_value = "6"
    elif value == "7":
        conv_value = "7"
    elif value == "8":
        conv_value = "8"
    elif value == "9":
        conv_value = "9"
    elif value == "A":
        conv_value = "10"
    elif value == "B":
        conv_value = "11"
    elif value == "C":
        conv_value = "12"
    elif value == "D":
        conv_value = "13"
    elif value == "E":
        conv_value = "14"
    elif value == "F":
        conv_value = "15"

    # return the result
    return conv_value

# create a function that convert any single hex digits to base-10 digits
# @param value the value to convert
# @return conv_value the converted value
def int2hex(value2):
    # determine the nature of each character to convert it
    conv_value2 = ""

    # create a loop to detected same characters in two bases

    for i in range(10):
        if i == value2:
            conv_value2 = i

    # determine the last digits
    if value2 == 10:
        conv_value2 = "A"
    elif value2 == 11:
        conv_value2 = "B"
    elif value2 == 12:
        conv_value2 = "C"
    elif value2 == 13:
        conv_value2 = "D"
    elif value2 == 14:
        conv_value2 = "E"
    elif value2 == 15:
        conv_value2 = "F"

    # return the result
    return conv_value2

# create a main program to demonstrate the functions
def main():
    # read the value from the user
    nb_str1 = input("Enter the single character in base-16 system: ")
    nb = int(input("Enter the single character in base-10 system: "))

    # display the result
    print(f'this character in base-10 system is {hex2int(nb_str1.upper())}')
    print(f'this character in base-16 system is {int2hex(nb)}\n')

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()








