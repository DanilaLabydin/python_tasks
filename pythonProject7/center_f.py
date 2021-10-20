##
# create a program that reads the string and displays it on the middle of the display
#

# create a function that displays a string on the middle of the display
# @param s the string entered by the user
# @param w the width of the display
# @return middle_string the new string
#
def center(s, w):
    # if the length of s is greater than or equal to the width of the window than s, s should be returned
    if len(s) >= w:
        return s

    # compute the number of spaces needed and generate the result
    space = ((len(s) - w) // 2) * - 1
    s = ' ' * space + s

    # return the new string that contains the "space" and the s
    return s

# create a main program to demonstrate the function
def main():
    # read the dimension from the user
    string = input("Enter the string: ")
    width = int(input("Enter the width: "))

    # compute the new string and display the result
    print(center(string, width))

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()



