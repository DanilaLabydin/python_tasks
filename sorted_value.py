##
# write a program that reads integers from the user and stores them in a list(0 to quit)
#

# create a list and an infinity loop to store the integers in a list(0 to quit)
integers = []
while True:
    # read the dimension from the user
    nb = int(input(f'Enter the number(0 to quit): '))

    # if value equals to 0, quit the loop, otherwise you need to add the value in the list
    if nb == 0:
        break
    integers.append(nb)

# display the result that displays the integers in ascending order,
# with one value appearing on each line
print(f'The value, sorted into ascending order, are:')
for integer in sorted(integers):
    print(integer)


