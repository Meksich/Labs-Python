from classes import *


def main():
    small_bra = bra.Bra(enums.StalesOfBras.TOP, enums.CupsSize.A, enums.LiningLevel.LIGHTLY_LINED, 0,
                        enums.Collections.INCREDIBLE, 2018, enums.Color.RED, 20.99)
    medium_bra = bra.Bra(enums.StalesOfBras.DEMI, enums.CupsSize.C, enums.LiningLevel.UNLINED, 1,
                         enums.Collections.DREAM_ANGELS, 2021, enums.Color.MULTICOLORED, 300)
    large_bra = bra.Bra(enums.StalesOfBras.BALCONETTE, enums.CupsSize.G_PLUS, enums.LiningLevel.PUSH_UP, 3,
                        enums.Collections.BODY_BY_VICTORIA, 2020, enums.Color.MULTICOLORED, 124)
    small_pants = pants.Pants(enums.StalesOfPants.MULTI_PACK, enums.PantsSize.XS, 60, enums.Fabrics.STEAMLESS,
                              enums.Collections.INCREDIBLE, 2021, enums.Color.FLORAL, 13)
    medium_pants = pants.Pants(enums.StalesOfPants.BRIEFS, enums.PantsSize.M, 90, enums.Fabrics.LACIE,
                               enums.Collections.DREAM_ANGELS, 2021, enums.Color.MULTICOLORED, 50.30)
    large_pants = pants.Pants(enums.StalesOfPants.SHAPEWEAR, enums.PantsSize.XL, 140, enums.Fabrics.COTTON,
                              enums.Collections.BODY_BY_VICTORIA, 2017, enums.Color.GREEN, 228)
    small_lingerie = lingerie.Lingerie(False, enums.LingerieStyles.CAMIS, enums.PantsSize.S,
                                       enums.Collections.INCREDIBLE, 2019, enums.Color.WHITE, 30.30)
    medium_lingerie = lingerie.Lingerie(True, enums.LingerieStyles.CORSETS, enums.PantsSize.M,
                                        enums.Collections.DREAM_ANGELS, 2021, enums.Color.MULTICOLORED, 1488)
    large_lingerie = lingerie.Lingerie(True, enums.LingerieStyles.BABYDOLLS, enums.PantsSize.L,
                                       enums.Collections.BODY_BY_VICTORIA, 2020, enums.Color.GREY, 23.37)
    list_of_underwear = [small_bra, medium_bra]
    manager = underwear_manager.UnderwearManager(list_of_underwear)
    manager.add_underwear(large_bra)
    manager.add_underwear(small_pants)
    manager.add_underwear(medium_pants)
    manager.add_underwear(large_pants)
    manager.add_underwear(small_lingerie)
    manager.add_underwear(medium_lingerie)
    manager.add_underwear(large_lingerie)
    # for i in manager.get_underwear_list():
    #     print(i)
    for u in manager.search_by_year(2021):
        print(u)
    print("--------------------------------")
    for u in manager.search_by_collection(enums.Collections.BODY_BY_VICTORIA):
        print(u)
    print("--------------------------------")
    manager.sort_by_price(enums.SortOrder.ASC)
    for i in manager.get_underwear_list():
        print(i.get_price())


if __name__ == '__main__':
    main()
