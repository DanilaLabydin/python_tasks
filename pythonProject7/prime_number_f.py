##
# create a program that checks and displays if the number is prime
#

# create a function that reads the number and determines the number is prime or not
# @param number the number that is entered by the user
# @return TRUE or FALSE

def PrimeNumberIf(number):
    # if the number = 1, return False. The prime number cannot be = 1
    if number == 1:
        return False

    # create a for loop to determine the number is divided by the sequence(2,number)
    # if it does (nb % i = 0), it is not a prime number and return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# create a main program to demonstrate the function
def main():
    nb = int(input('Enter the number: '))
    print(PrimeNumberIf(nb))
    print()
    for i in range(1, nb):
        if PrimeNumberIf(i) is True:
            print(f'{i} - Prime number')

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()


