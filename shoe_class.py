# creates the class and methods within the class
class Shoe:
    # initialises country, code, product, cost and quantity as part of Shoe class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # method to return the cost of the shoe
    def get_cost(self):
        return self.cost()

    # method to return the quantity of shoes in stock
    def get_quantity(self):
        return self.get_quantity()

    # method to write object to text file in consistent format
    def to_file(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    # method to write objects to table
    def to_table(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]

    # method to return string representation of class
    def __str__(self):
        return f'''\t***************************************************
    Country of manufacture: \t\t{self.country}
    Bar code: \t\t\t\t\t\t{self.code}
    Name of product: \t\t\t\t{self.product}
    Cost of product: \t\t\t\t{self.cost}
    Quantity of product in stock: \t{self.quantity}
    ***************************************************\n'''
