class Clothes:

    def __init__(self, brand, color, price, types_for_wearing):
        self.brand = brand
        self.color = color
        self.price = price
        self.types_for_wearing = types_for_wearing

    def __del__(self):
        print("this was deleted: " + self.brand)

    def __str__(self):
        return "\n\nBrand: " + self.brand + \
            ",\n Color: " + self.color + \
            ",\n Price: " + str(self.price) + \
            ",\n TypesForWearing: " + str(self.types_for_wearing)