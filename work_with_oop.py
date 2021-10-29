class Apple():
    def __init__(self, color, flavor, size):
        """ This class represents apples """
        self.color = color
        self.flavor = flavor
        self.size = size
    def __str__(self):
        return f'This apple has these following parameters:{self.color},{self.size},{self.flavor}'

gold = Apple('red', 'sweet', 'big')
print(gold.size)
print(gold.flavor)
print(gold.color)

antonovka = Apple('red', 'sweet', 'big')
print(antonovka)

help(Apple)
