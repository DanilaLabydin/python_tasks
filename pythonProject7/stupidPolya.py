##
# create a program that converts a number in an arbitrary base system to another arbitrary base system
#

# create a function that converts an arbitrary base number to 10-base
# @param n(format - string) a number that was entered by the user
# @param base a current base system
# @return result the input number in 10-base system
def ten2arbitrary(n: str, base):
    # create a empty result string to store the base-10 number
    result = ""

    # create a loop to convert the number
    while n != 0:
        result += str(int(n) % base)
        n = n // base
    return result[::-1]

# create a function that converts a base-10 number to an arbitrary base system
# @param n(format - string) a number that was entered by the user
# @param base a current base system
# @return result the input number in 10-base system
def arbitrary2ten(n: str, base):
    # create a special variable to store the result
    sm = 0

    # create a loop to convert the number
    for i in range(len(n)):
        sm += int(n[i]) * (base ** (len(n) - 1 - i))
    return sm

# create a main program to demonstrate the function
def main():
    # read the dimensions from the user
    base_input = int(input(f'Enter the input base: '))
    base_output = int(input(f'Enter the output base: '))
    nb_input = input(f'Enter the number to convert: ')

    # if the base_input = base_output, display the entered number
    if base_input == base_output:
        print(nb_input)

    #
    if base_input == 10:
        print(ten2arbitrary(nb_input, base_output))

    if base_output == 10:
        print(arbitrary2ten(nb_input, base_output))


    #use the arbitrary2ten function to convert a number to base-10 system
    middle_number = arbitrary2ten(nb_input, base_input)

    nb_output = ten2arbitrary(middle_number, base_output)

    print(nb_output)


# call the main function only if the module is not imported
if __name__ == '__main__':
    main()