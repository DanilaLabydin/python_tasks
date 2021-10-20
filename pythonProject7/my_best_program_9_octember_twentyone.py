##
# create a program that converts from arbitrary base-system to another arbitrary base-system
# the program converts by the following algorithm: arbitrary base to base-10, base-10 to arbitrary base
# the original base and base to convert are entered by the user
#


# create a function that converts hex_digits to 10-base system digits and stores them in the list
# @param nb the entered number
# @return lists the list with numbers
#
def hex_nb_to_list(nb):
    # create an empty list
    lists = []

    # create a loop to convert each digits to the right form and to determine which type of digit we have
    for i in range(len(nb)):
        if nb[i] == "A":
            lists.append(10)
        elif nb[i] == "B":
            lists.append(11)
        elif nb[i] == "C":
            lists.append(12)
        elif nb[i] == "D":
            lists.append(13)
        elif nb[i] == "E":
            lists.append(14)
        elif nb[i] == "F":
            lists.append(15)
        else:
            lists.append(int(nb[i]))
    # return the result
    return lists


# create a function that convert an arbitrary base to base-10
# @param nb the number that was entered by the user
# @param base the base of number
# @return new_nb the converted number
#
def arbitrary_to_ten(nb, base):
    # convert the number to the list and create a variable to store the new number
    digits = hex_nb_to_list(nb)
    sm = 0

    # create a loop to convert each digit to the new base and return the sm
    for i in range(len(digits)):
        sm += digits[i] * base ** (len(digits) - i - 1)
    return sm


# create a function that convert a base-10 to an arbitrary base system
# @param nb the number that was entered by the user
# @param base the base of number
# @return new_nb the converted number
#

def ten_to_arbitrary(nb, base):
    # create a variable to store the digits and transform the user's dimension to int format
    result = ""
    nb = int(nb)

    # create a loop to store each reminder from division(reminder) by the base
    while nb > 0:
        digit = nb % base

        # if the reminder is more than 9, convert it according to hex-system digits
        if digit == 10:
            digit = "A"
        elif digit == 11:
            digit = "B"
        elif digit == 12:
            digit = "C"
        elif digit == 13:
            digit = "D"
        elif digit == 14:
            digit = "E"
        elif digit == 15:
            digit = "F"

        # store the result into a special variables and divide(floor) the nb by base
        result += str(digit)
        nb //= base

    # reverse the "result" variable to correct order and return it
    new_nb = result[::-1]
    return new_nb


# create a main program to demonstrate the functions
def main():
    print("THE CONVERTER OF NUMBERS")
    while True:
        # read the dimension from the user
        x = input("Enter the positive number to convert(0 to quit): ")
        if x == "0":
            break
        base_old = int(input("Enter the current base: "))
        base_new = int(input("Enter the new base: "))

        middle_nb = arbitrary_to_ten(x.upper(), base_old)
        new_nb = ten_to_arbitrary(middle_nb, base_new)

        print(f'The number {x} from base-{base_old} system to base-{base_new} system is {new_nb}')
        print()

# call the main program only if the module is not imported
if __name__ == '__main__':
    main()
