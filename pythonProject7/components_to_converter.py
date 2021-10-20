x = input("Enter the number: ")
base = int(input("Enter the base: "))

#
# from base-10 to arbitrary(1 <= base<=10)
# digit = ""
# while x > 0:
#    digit += str(x % base)
#    x //= base
# result = int(digit[::-1])
# print(type(result))
# print(result)
#

#
# from base-10 to arbitrary(1 < base <= 16)
# result = ""
# x = int(x)
# while x > 0:
#   digit = x % base
#    if digit == 10:
#        digit = "A"
#    elif digit == 11:
#        digit = "B"
#    elif digit == 12:
#        digit = "C"
#    elif digit == 13:
#        digit = "D"
#    elif digit == 14:
#        digit = "E"
#    elif digit == 15:
#        digit = "F"
#    result += str(digit)
#    x //= base
# print(result[::-1])
# print(type(result))
#

#
# from arbitrary(1 < base < 10)
# sm = 0
# digit = int(x)
# for i in range(len(x)):
#    sm += int(x[i]) * base ** (len(x) - i - 1)
# print(sm)
#

lists = []
for i in range(len(x)):
    if x[i] == "A":
        lists.append(10)
    elif x[i] == "B":
        lists.append(11)
    elif x[i] == "C":
        lists.append(12)
    elif x[i] == "D":
        lists.append(13)
    elif x[i] == "E":
        lists.append(14)
    elif x[i] == "F":
        lists.append(15)
    else:
        lists.append(int(x[i]))
print(lists)
print()

sm = 0
for i in range(len(lists)):
    sm += lists[i] * base ** (len(lists) - i - 1)
print(sm)


