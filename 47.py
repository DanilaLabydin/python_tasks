##
# determine the season of a year with month and day
#

# read the month and the day from the user
month = input("Enter the name of a month: ")
day = int(input("Enter the number of a day: "))

# display the error message if the user entered the incorrect data
if day < 1 or day > 31:
    print("ERROR! YOU ENTERED AN INCORRECT DATA (day can't be less than 1 or more than 31")

# now check every month and day
season = ""
if month == "March":
    if 20 <= day <=31:
        season = "Spring"
    else:
        season = "Winter"
if month == "April" or month == "May":
    season = "Spring"
if month == "June":
    if 21 <= day <= 30:
        season = "Summer"
    else:
        season = "Spring"
if month == "July" or month == "August":
    season = "Summer"
if month == "September":
    if 22 <= day <= 30:
        season = "Fall"
    else:
        season = "Summer"
if month == "October" or month == "November":
    season = "Fall"
if month == "December":
    if 21 <= day <= 31:
        season = "Winter"
if month == "January" or month == "February":
    season = "Winter"

# display the message
print(day, month, "That's a ", season)







