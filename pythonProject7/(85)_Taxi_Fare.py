# compute the Taxi Fare
# @param base_fare the base fare
# @param variable_portion the constantly pay per km
# @return cost the sum of fare
BASE_FARE = 4.00
VARIABLE_PORTION = 0.25
RANGE_OF_DISTANCE = 140

def taxi_fare(distance):
    # the taxi fare consist of a base fare of $4.00, plus $0.25 for every 140m travelled
    # convert the distance(km) into metres
    distance = distance * 1000

    # compute the taxi fare
    sm = BASE_FARE + VARIABLE_PORTION * (distance // RANGE_OF_DISTANCE)

    # return the cost of taxi fare
    return sm

# display the cost of taxi fare entered by the user
def main():
    # read the dimension from the user
    distance = float(input('Enter the distance in km: '))

    # compute the Taxi Fare and display the result
    cost_of_fare = taxi_fare(distance)
    print(f'The taxi fare for the {distance} km is {cost_of_fare}')

# call the main function
main()



