# create a random password
# @return a random password(length of between 7 and 10 characters)
from random import randint
MIN_LENGTH = 7
MAX_LENGTH = 10
MIN_ASCII = 33
MAX_ASCII = 126

def random_pasword():
    # determine the length of password using the random function
    ln = randint(MIN_LENGTH, MAX_LENGTH)

    # create a loop to store each character of password
    password = ""
    for i in range(ln):
        character = str(chr(randint(MIN_ASCII, MAX_ASCII)))
        password += character

    # return the random password
    return password

# generate and display a random password
def main():
    print(random_pasword())
    print()
# call the main function only if the module is not imported
if __name__ == '__main__':
     main()
