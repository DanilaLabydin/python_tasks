
def ten2arbitrary(n: str, base):
    result = ""
    while n != 0:
        result += str(int(n) % base)
        n = n // base
    return result[::-1]

def arbitrary2ten(n: str, base):
    sm = 0
    for bit in range(len(n)):
        sm += int(n[bit]) * (base ** (len(n) - 1 - bit))
    return sm


# create a main program to demonstrate the function
def main():
    base_input = int(input(f'Enter the input base: '))
    base_output = int(input("Enter the output base: "))
    nb_input = input(f'Enter the number to convert: ')

    middle_number = arbitrary2ten(nb_input, base_input)

    nb_output = ten2arbitrary(middle_number, base_output)

    print(nb_output)


# call the main function only if the module is not imported
if __name__ == '__main__':
    main()