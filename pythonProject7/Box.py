# draw a box outlined with asterisks and filled with spaces
# @param width the width of the box
# @param height the height of the box
def drawBox(width, height):
    # a box that is smaller than 2x2 cannot be drawn by this function
    if height < 2 or width < 2:
        print('Error: The width or height is too small')

    # draw the top of the box
    print("*" * width)

    # draw the sides of the box
    for i in range(height - 2):
        print('*' + " " * (width - 2) + '*')

    # draw the bottom of the bottom
    print("*" * width)
    return quit()


a = int(input(f'Enter the height:'))
b = int(input(f'Enter the width:'))

print(drawBox(b, a))


