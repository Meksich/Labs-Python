import unittest
from classes import *


class TestUnderwearManager(unittest.TestCase):
    def setUp(self):
        self.small_bra = bra.Bra(enums.StalesOfBras.TOP, enums.CupsSize.A, enums.LiningLevel.LIGHTLY_LINED, 0,
                                 enums.Collections.INCREDIBLE, 2018, enums.Color.RED, 20.99)
        self.medium_bra = bra.Bra(enums.StalesOfBras.DEMI, enums.CupsSize.C, enums.LiningLevel.UNLINED, 1,
                                  enums.Collections.DREAM_ANGELS, 2021, enums.Color.MULTICOLORED, 300)
        self.small_pants = pants.Pants(enums.StalesOfPants.MULTI_PACK, enums.PantsSize.XS, 60, enums.Fabrics.STEAMLESS,
                                       enums.Collections.INCREDIBLE, 2021, enums.Color.FLORAL, 13)
        self.medium_pants = pants.Pants(enums.StalesOfPants.BRIEFS, enums.PantsSize.M, 90, enums.Fabrics.LACIE,
                                        enums.Collections.DREAM_ANGELS, 2021, enums.Color.MULTICOLORED, 50.30)
        self.small_lingerie = lingerie.Lingerie(False, enums.LingerieStyles.CAMIS, enums.PantsSize.S,
                                                enums.Collections.INCREDIBLE, 2019, enums.Color.WHITE, 30.30)
        self.medium_lingerie = lingerie.Lingerie(True, enums.LingerieStyles.CORSETS, enums.PantsSize.M,
                                                 enums.Collections.DREAM_ANGELS, 2021, enums.Color.MULTICOLORED, 1488)
        list_of_underwear = [self.small_lingerie, self.medium_lingerie, self.small_pants, self.medium_pants,
                             self.small_bra, self.medium_bra]
        self.year = 2021
        self.collection = enums.Collections.BODY_BY_VICTORIA

        self.underwear_manager = underwear_manager.UnderwearManager(list_of_underwear)
        # self.maxDiff = None

    def test_search_by_year(self):
        self.assertEqual(self.underwear_manager.search_by_year(self.year),
                         [self.medium_bra, self.small_pants, self.medium_pants, self.medium_lingerie])

    def test_search_by_collection(self):
        self.assertEqual(self.underwear_manager.search_by_collection(self.collection), [])

    def test_sort_by_price(self):
        self.assertEqual(self.underwear_manager.sort_by_price(enums.SortOrder.ASC),
                         [self.small_pants, self.small_bra, self.small_lingerie, self.medium_pants, self.medium_bra,
                          self.medium_lingerie])


if __name__ == "__main__":
    unittest.main()
