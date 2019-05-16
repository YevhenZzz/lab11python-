from ua.lviv.iot.models.Clothes import Clothes


class CeremonialClothing(Clothes):

    def __init__(self, brand, color, price, types_for_wearing, sets, style):
        super().__init__(brand, color, price, types_for_wearing,)
        self.sets = sets
        self.style = style

    def __str__(self):
        return super().__str__() + \
            "\n Sets: " + str(self.sets) + \
            ",\n Style: " + str(self.style)