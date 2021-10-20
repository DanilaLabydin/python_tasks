##
# 81 binary to decimal
#

# read the dimension from the user
binary_input = input("Enter the number in binary:")

# create a loop to convert every bit in the dimension with correct order
# create a special variable to count the decimal as a sum
sm = 0
for bit in range(len(binary_input)):
    sm += int(binary_input[bit]) * (2 ** (len(binary_input) - 1 - bit))

# display the result
print(sm)



