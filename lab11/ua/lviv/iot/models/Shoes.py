from ua.lviv.iot.models.Clothes import Clothes


class Shoes(Clothes):

    def __init__(self, brand, color, price, types_for_wearing, shoes_type, has_laces):
        super().__init__(brand, color, price, types_for_wearing)
        self.shoes_type = shoes_type
        self.has_laces = has_laces
        
    def __str__(self):
        return super().__str__() + \
            "\n Shoes_type: " + str(self.shoes_type) + \
            ",\n Has laces: " + str(self.has_laces)
