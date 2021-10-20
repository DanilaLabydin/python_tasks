##
# create a program that reads 3 lengths from the user and display a Boolean result
# whether or not a triangle is valid triangle
#

# create a function that reads 3 lengths from the user and compute the nature of a triangle
# @param ln1 the first length
# @param ln2 the second length
# @param ln3 the third length
# @return the Boolean result
def isValidTriangle(ln1, ln2, ln3):
    # if one of the lengths is = 0 or less, return False
    valid_triangle = False
    if ln1 <= 0 or ln2 <= 0 or ln3 <= 0:
        return valid_triangle

    # determine whether or not a triangle is a valid triangle
    # the triangle is valid only if each length is less than sum of the other two lengths
    if ln1 < ln2 + ln3 and ln2 < ln1 + ln3 and ln3 < ln1 + ln2:
        valid_triangle = True

    # return the result
    return valid_triangle

# create a main program to demonstrate the function
def main():
    # read the dimension from the user
    len1 = float(input('Enter the first length: '))
    len2 = float(input('Enter the second length: '))
    len3 = float(input('Enter the third length: '))

    # compute the result
    print(isValidTriangle(len1, len2, len3))

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()



