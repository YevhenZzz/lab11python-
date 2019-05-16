from ua.lviv.iot.Enums.material_types import MaterialTypes
from ua.lviv.iot.Enums.shoes_type import ShoesType
from ua.lviv.iot.Enums.size import Size
from ua.lviv.iot.Enums.style import Style
from ua.lviv.iot.Enums.types_for_wearing import TypesForWearing
from ua.lviv.iot.managers.ClothesManager import ClothesManager
from ua.lviv.iot.models.CereminalClothing import CeremonialClothing
from ua.lviv.iot.models.Dress import Dress
from ua.lviv.iot.models.Shoes import Shoes


class Main:

    @staticmethod
    def main():
        manager = ClothesManager()
        dress = Dress("Bershka", "Green", 4000, TypesForWearing.HOME,
                Size.L, MaterialTypes.FABRIC)
        clothing = CeremonialClothing("Zara", "Black", 5000,
                TypesForWearing.FASTIVE, "Frag", Style.CLASSICALSUIT)
        shoes = Shoes("Gucci", "Yellow", 7000,
                TypesForWearing.EVERYDAY, ShoesType.MOCS, True)

        clothes_list = [dress, clothing, shoes]

        print(*manager.sort_by_price(clothes_list, False))

        print(*manager.sort_by_brand(clothes_list, False))

        print(*manager.find_by_types_for_wearing(clothes_list, TypesForWearing.HOME))

        print("\nDestructors: ")


if __name__ == '__main__':
    Main.main()
