

class ClothesManager:

    def __init__(self, clothes_list=[]):
        self.clothes_list = clothes_list

    def find_by_types_for_wearing(self, clothes_list, types_for_wearing):
        return list(filter(lambda clothes: clothes.types_for_wearing == types_for_wearing, clothes_list))

    def sort_by_price(self, clothes_list, is_reversed):
        return sorted(clothes_list, key=lambda clothes: clothes.price, reverse=is_reversed)

    def sort_by_brand(self, clothes_list, is_reversed):
        return sorted(clothes_list, key=lambda clothes: clothes.brand, reverse=is_reversed)

