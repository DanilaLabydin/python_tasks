# compute the hypotenuse using Pythagorean theorem
# @param first_length the first cathet of a right triangle
# @param second_length the second cathet of a right triangle
# @return the hypotenuse
from math import pow
from math import sqrt
def hypo_triangle(first_length, second_length):
    # compute the hypotenuse using this formula: c^2 = a^2 = b^2
    c = sqrt(pow(first_length, 2) + pow(second_length, 2))

    # return the hypotenuse
    return c

def main():
    # read the dimension from the user(two cathets)
    first_cathet = float(input('Enter the length of first cathet: '))
    second_cathet = float(input('Enter the length of second cathet: '))

    # compute the hypotenuse using special function
    ln_hypo = hypo_triangle(first_cathet, second_cathet)

    # display the result
    print(f'The length of the hypotenuse is {ln_hypo}')

# call the main function
main()
