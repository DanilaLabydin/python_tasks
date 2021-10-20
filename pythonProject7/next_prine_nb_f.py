##
# create a program that reads a number and display the next prime number
#
from prime_number_f import PrimeNumberIf

# create a function that return the next prime number
# @param n the entered number
# @return next_nb the next prime number
def next_prime_number(n):
    # create an infinite loop to determine whether or not the next number is a prime number
    while True:
        # increase the number by 1
        n += 1

        # determine the nature of this number, use the PrimeNumberIf to do it
        if PrimeNumberIf(n) is True:
            next_nb = n
            return next_nb

# create a main program to demonstrate the function
def main():
    nb = int(input('Enter the number: '))
    print(f'The next prime number is {next_prime_number(nb)}')

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()


