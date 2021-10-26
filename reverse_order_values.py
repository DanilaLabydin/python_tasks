##
# write a program that reads integers from the user and stores them in a list(0 to quit) and displays it
# with reverse order
#

# create a list and an infinity loop to store the integers in a list(0 to quit)
integers = []
while True:
    # read the dimension from the user
    nb = int(input(f'Enter the number(0 to quit): '))

    # if a value is equals to 0, quit the loop, otherwise you need to add the value in the list
    if nb == 0:
        break
    integers.append(nb)

# sort the values into reverse order
integers.sort()

# display the result that displays the integers in reverse order,
# with one value appearing on each line
print(f'The value, sorted into reverse order, are:')
for integer in range(len(integers) - 1, -1, -1):
    print(integers[integer])


