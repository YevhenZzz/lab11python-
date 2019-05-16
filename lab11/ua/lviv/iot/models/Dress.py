from ua.lviv.iot.models.Clothes import Clothes


class Dress(Clothes):

    def __init__(self, brand, color, price, types_for_wearing, size, material_types):
        super().__init__(brand, color, price, types_for_wearing)
        self.size = size
        self.material_types = material_types

    def __str__(self):
        return super().__str__() + \
            "\n Size: " + str(self.size) + \
            ",\n Material types: " + str(self.material_types)
