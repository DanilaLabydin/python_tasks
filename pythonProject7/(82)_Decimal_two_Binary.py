##
# covert decimal into binary
#

# read the dimension from the user
decimal = int(input(f'Enter the number: '))

# create a loop to convert every digit in the dimension with correct order
# create a special variable to divide the dimension by 2
result = ''
q = decimal
while q != 0:
    r = q % 2
    result += str(r)
    q = q // 2

# display the result
print(result[::-1])





