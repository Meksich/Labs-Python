from . import underwear


class Pants(underwear.Underwear):
    def __init__(self, style, pants_size, circumference, fabrics, collection, year_of_production, color, price,
                 bra="None"):
        super().__init__(collection, year_of_production, color, price)
        self.__style = style
        self.__pants_size = pants_size
        self.__waist_circumference = circumference
        self.__fabrics = fabrics
        self.__perfect_pair_of_bra = bra

    def __str__(self):
        return f'collection = {self._collection} \n' \
               f'year of production = {self._year_of_production} \n' \
               f'color = {self._color} \n' \
               f'price in bucks=  {self._price} \n'\
               f'style = {self.__style} \n' \
               f'pants size = {self.__pants_size} \n' \
               f'waist circumference = {self.__waist_circumference} \n' \
               f'fabrics =  {self.__fabrics} \n' \
               f'perfect pair of bra = {self.__perfect_pair_of_bra} \n'

    def get_style(self):
        return self.__style

    def get_pants_size(self):
        return self.__pants_size

    def get_waist_circumference(self):
        return self.__waist_circumference

    def get_fabrics(self):
        return self.__fabrics

    def get_perfect_pair_of_bra(self):
        return self.__perfect_pair_of_bra

    def set_style(self, style):
        self.__style = style

    def set_pants_size(self, pants_size):
        self.__pants_size = pants_size

    def set_fabrics(self, fabrics):
        self.__fabrics = fabrics

    def set_waist_circumference(self, waist_circumference):
        self.__waist_circumference = waist_circumference

    def set_perfect_pair_of_bra(self, bra):
        self.__perfect_pair_of_bra = bra
