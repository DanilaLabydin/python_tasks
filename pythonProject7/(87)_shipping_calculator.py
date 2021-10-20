##
# create a program that calculates and display the cost of express shipping of an online-retailer
#
FIRST_ITEM_COST = 10.95
NEXT_ITEM_COST = 2.95

## compute the cost of items
# @param number the number of items
# @return cost the cost of shipping
#
def shipping_cost(number):
    # if the number of items = 1, the cost will be = 10.95
    if number == 1:
        cost = FIRST_ITEM_COST

    # if the number of items not = 1, use the following formula
    if number > 1:
        cost = FIRST_ITEM_COST + NEXT_ITEM_COST * (number - 1)

    # return the cost of shipping
    return cost

# display the cost of shipping using this function
def main():
    nb = int(input('Enter the number of items: '))
    print('The total cost of the shipping delivery will be $%.2f' % shipping_cost(nb))

# call the main function only if the module is not imported
if __name__ == "__main__":
    main()