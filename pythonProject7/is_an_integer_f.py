##
# create a program that reads a string and determine whether or not a string is represent an integer
#

# 
# create a function that reads the string and determines its nature
# @param string the string was entered by the user
# @return True if string represents an integer and False if it doesn't
def isInteger(s):
    # skip any leading or trailing white space
    s = str(s.strip())

    # determine the nature of the string and return the result
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

# create a main program to demonstrate the function
def main():
    string = input('Enter a string: ')
    if isInteger(string):
        print('This string represents an integer.')
    else:
        print("This string doesn't represent an integer.")

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()



