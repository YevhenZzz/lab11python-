from ua.lviv.iot.models.Clothes import Clothes


class Trousers(Clothes):
    def __init__(self, brand, color, price, types_for_wearing):
        super().__init__(brand, color, price, types_for_wearing)

