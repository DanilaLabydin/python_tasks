##
# display the complete lyrics for the song "The Twelve Days of Christmas"
#
from int2ordinal import int2ordinal

# display all gifts in these song
# @param n the number of version
# @result s the string with gift
def gift_in_lyrics(n):
    # display first and second strings of song
    # use the following function to convert int to ordinal number
    print(f'On the {int2ordinal(n)} day of Christmas')
    print(f'My true love sent to me')

    # determine which gift has to be displayed
    s = ""
    if n >= 12:
        s = "Twelve drummers drumming"
        print('Twelve drummers drumming')
    if n >= 11:
        s = ""
        print('Eleven pipers piping,')
    if n >= 10:
        s = "Ten lords a-leaping"
        print('Ten lords a-leaping')
    if n >= 9:
        s = "Nine ladies dancing"
        print('Nine ladies dancing')
    if n >= 8:
        s = "Eight maids a-milking"
        print('Eight maids a-milking')
    if n >= 7:
        s = "Seven swans a-swimming"
        print('Seven swans a-swimming')
    if n >= 6:
        s = "Six geese a-laying"
        print('Six geese a-laying')
    if n >= 5:
        s = "Five golden rings"
        print('Five golden rings')
    if n >= 4:
        s = "Four calling birds"
        print('Four calling birds')
    if n >= 3:
        s = "Three French hens"
        print('Three French hens')
    if n >= 2:
        s = "Two turtle doves \nA partridge in a pear tree"
        print('Two turtle doves,')
    if n == 1:
        print("A", end="")
    else:
        print('partridge in a pear tree.')
        print()

def main():
    for i in range(1,13):
        print(f'{gift_in_lyrics(i)}')



if __name__ == '__main__':
    main()



