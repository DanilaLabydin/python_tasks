# draw a box outlined with asterisks and filled with spaces
# @param width the width of the box
# @param height the height of the box
# @param outline the character that used for the outline the box
# @param fill the character that used for the fill the box
def drawBox(width, height, outline='g', fill='d'):
    # a box that is smaller than 2x2 cannot be drawn by this function
    if height < 2 or width < 2:
        print('Error: The width or height is too small')

    # draw the top of the box
    print(outline * width)

    # draw the sides of the box
    for i in range(height - 2):
        print(outline + fill * (width - 2) + outline)

    # draw the bottom of the bottom
    print(outline * width)

# demonstrate the drawbox function
drawBox(14, 5, '@')



