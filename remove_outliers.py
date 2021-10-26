##
# write a program that reads the user's list and remove from it the n largest elements and
# the n smallest elements
#

#
# create a function that return the a list without n largest and n smallest values from it
# @param list the user's list of values
# @param n the non-negative integer
# @return new_list the new copy of list with properly order
#
def remove_outliers(data, num_outliers):
    # sort a list into ascending order
    copy_list = sorted(data)

    # remove the n largest values and the n smallest values
    for i in range(num_outliers):
        copy_list.pop()
    for i in range(num_outliers):
        copy_list.pop(0)

    # return the result
    return copy_list


# call the main program to demonstrate the function
def main():
    # create an empty list
    numbers = []

    # create an infinity loop to store values in the list
    while True:
        value = int(input(f'Enter the value to sort in a list(0 to quit): '))
        if value == 0:
            break
        numbers.append(value)

    n = int(input(f'Enter the number of outliers that will be remove from the list: '))
    if n * 2 < len(numbers):
        print(f'With the outliers removed: {remove_outliers(numbers, n)}')
        print(f'The original list: {numbers}')
    else:
        print(f"ERROR! You didn't enter enough values.")

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()





