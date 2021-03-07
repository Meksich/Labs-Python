import classes


def main():
    small_bra = classes.bra.Bra(classes.enums.StalesOfBras.TOP, classes.enums.CupsSize.A,
                                classes.enums.LiningLevel.LIGHTLY_LINED, 0,
                                classes.enums.Collections.INCREDIBLE, 2018,
                                classes.enums.Color.RED, 20.99)
    medium_bra = classes.bra.Bra(classes.enums.StalesOfBras.DEMI,
                                 classes.enums.CupsSize.C,
                                 classes.enums.LiningLevel.UNLINED, 1,
                                 classes.enums.Collections.DREAM_ANGELS, 2021,
                                 classes.enums.Color.MULTICOLORED, 300)
    large_bra = classes.bra.Bra(classes.enums.StalesOfBras.BALCONETTE,
                                classes.enums.CupsSize.G_PLUS,
                                classes.enums.LiningLevel.PUSH_UP, 3,
                                classes.enums.Collections.BODY_BY_VICTORIA, 2020,
                                classes.enums.Color.MULTICOLORED, 124)
    small_pants = classes.pants.Pants(classes.enums.StalesOfPants.MULTI_PACK,
                                      classes.enums.PantsSize.XS, 60,
                                      classes.enums.Fabrics.STEAMLESS,
                                      classes.enums.Collections.INCREDIBLE, 2021,
                                      classes.enums.Color.FLORAL, 13)
    medium_pants = classes.pants.Pants(classes.enums.StalesOfPants.BRIEFS,
                                       classes.enums.PantsSize.M, 90,
                                       classes.enums.Fabrics.LACIE,
                                       classes.enums.Collections.DREAM_ANGELS, 2021,
                                       classes.enums.Color.MULTICOLORED, 50.30)
    large_pants = classes.pants.Pants(classes.enums.StalesOfPants.SHAPEWEAR,
                                      classes.enums.PantsSize.XL, 140,
                                      classes.enums.Fabrics.COTTON,
                                      classes.enums.Collections.BODY_BY_VICTORIA, 2017,
                                      classes.enums.Color.GREEN, 228)
    small_lingerie = classes.lingerie.Lingerie(False, classes.enums.LingerieStyles.CAMIS,
                                               classes.enums.PantsSize.S,
                                               classes.enums.Collections.INCREDIBLE, 2019,
                                               classes.enums.Color.WHITE, 30.30)
    medium_lingerie = classes.lingerie.Lingerie(True, classes.enums.LingerieStyles.CORSETS,
                                                classes.enums.PantsSize.M,
                                                classes.enums.Collections.DREAM_ANGELS, 2021,
                                                classes.enums.Color.MULTICOLORED, 1488)
    large_lingerie = classes.lingerie.Lingerie(True, classes.enums.LingerieStyles.BABYDOLLS,
                                               classes.enums.PantsSize.L,
                                               classes.enums.Collections.BODY_BY_VICTORIA, 2020,
                                               classes.enums.Color.GREY, 23.37)
    manager = classes.underwear_manager.UnderwearManager()
    manager.add_underwear(small_bra)
    manager.add_underwear(medium_bra)
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
    for u in manager.search_by_collection(classes.enums.Collections.BODY_BY_VICTORIA):
        print(u)
    print("--------------------------------")
    manager.sort_by_price(classes.enums.SortOrder.ASC)
    for i in manager.get_underwear_list():
        print(i.get_price())


if __name__ == '__main__':
    main()
