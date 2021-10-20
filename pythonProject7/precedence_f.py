##
# create a program that returns an integer representing the precedence of a math. operator
# and displays the result
#

#
# create a function that reads a string and returns the precedence of a math. operator
# @param s the string was entered by the user
# @return result the precedence of a math operator
def precedence(s):
    # determine which math.operator is represented by the string
    result = -1
    if s == "+" or s == "-":
        result = 1
    if s == "*" or s == "/":
        result = 2
    if s == "^":
        result = 3
    return result

# create a main program to demonstrate the function
def main():
    string = input('Enter a string: ')
    print(precedence(string))

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()