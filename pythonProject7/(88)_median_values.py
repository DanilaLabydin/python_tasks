##
# create a program that reads three values and outputs the median of these values
#

# determine the median of values
# @param a the first value
# @param b the second value
# @param c the third value
# @result m the median
def median_three_values(a, b, c):
    # determine the middle value
    m = (a + b + c) - max(a, b, c) - min(a, b, c)

    # return the middle value
    return m

# display the median of three values that are entered by the user
def main():
    # read the dimension from the user
    nb1 = float(input(f'Enter the first value: '))
    nb2 = float(input(f'Enter the second value: '))
    nb3 = float(input(f'Enter the third value: '))

    # compute and display the median
    print(f'The median of these values is {median_three_values(nb1, nb2, nb3)}')

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()





