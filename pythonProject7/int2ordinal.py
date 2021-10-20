##
# convert an integer(1-12) entered by the user to its ordinal number and display the result
#
NUMBERS2CONVERT = 12

# convert an integer (1-12) to its Ordinal number
def int2ordinal(integer):
    # determine the number and convert it
    string = ""
    if integer == 1:
        string = "First"
    elif integer == 2:
        string = "Second"
    elif integer == 3:
        string = "Third"
    elif integer == 4:
        string = "Fourth"
    elif integer == 5:
        string = "Fifth"
    elif integer == 6:
        string = "Sixth"
    elif integer == 7:
        string = "Seventh"
    elif integer == 8:
        string = "Eighth"
    elif integer == 9:
        string = "Ninth"
    elif integer == 10:
        string = "Tenth"
    elif integer == 11:
        string = "Eleventh"
    elif integer == 12:
        string = "Twelfth"

    # if the integer more than 12, the empty string will be return
    # otherwise return string
    return string

# demonstrate the function by displaying all ordinal numbers
def main():
    for i in range(1, NUMBERS2CONVERT + 1):
        print(f'{i} - {int2ordinal(i)}')

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()





