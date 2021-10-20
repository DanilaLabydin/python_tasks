##
# create a program that display the lyrics of "The Twelve Days of Christmas" song
# using the int2ordinal function, the user entered the number of verse and the program should
# display the right verse of the song
#
from int2ordinal import int2ordinal
NB_OF_VERSES = 12

# create a function that display the verse of lyrics
# @param nb the number of verse
# @return s the lyrics of entered number of verse
def christmas_verse_nb(nb):
    # display the common strings of all song
    print(f'On the {int2ordinal(nb)} day of Christmas')
    print(f'my true love sent to me:')

    # determine the number of verse and display the lyrics
    if nb >= 12:
        print(f'Twelve drummers drumming')
    if nb >= 11:
        print(f'Eleven pipers piping')
    if nb >= 10:
        print(f'Ten lords a-leaping')
    if nb >= 9:
        print(f'Nine ladies dancing')
    if nb >= 8:
        print(f'Eight maids a-milking')
    if nb >= 7:
        print(f'Seven swans a-swimming')
    if nb >= 6:
        print(f'Six geese a-laying')
    if nb >= 5:
        print(f'Five golden rings')
    if nb >= 4:
        print(f'Four calling birds')
    if nb >= 3:
        print(f'Three french hens')
    if nb >= 2:
        print(f'Two turtle doves, and')
        print(f'A partridge in a pear tree\n')
    else:
        print(f'A partridge in a pear tree\n')

# demonstrate the function by displaying all verses of song
def main():
    for i in range(1, NB_OF_VERSES + 1):
        christmas_verse_nb(i)

# call the main function only if the module is not imported
if __name__ == '__main__':
    main()






