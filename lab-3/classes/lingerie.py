from . import underwear


class Lingerie(underwear.Underwear):
    def __init__(self, sleeveless, style, size, collection, year_of_production, color, price):
        super().__init__(collection, year_of_production, color, price)
        self.__style = style
        self.__lingerie_size = size
        self.__sleeveless = sleeveless

    def __str__(self):
        return f'collection = {self._collection} \n' \
               f'year of production = {self._year_of_production} \n' \
               f'color = {self._color} \n' \
               f'price in bucks =  {self._price} \n'\
               f'style = {self.__style} \n' \
               f'lingerie size = {self.__lingerie_size} \n' \
               f'is sleeveless = {self.__sleeveless} \n'

    def get_style(self):
        return self.__style

    def get_lingerie_size(self):
        return self.__lingerie_size

    def get_sleeveless(self):
        return self.__sleeveless

    def set_style(self, style):
        self.__style = style

    def set_lingerie_size(self, size):
        self.__lingerie_size = size

    def set_sleeveless(self, sleeveless):
        self.__sleeveless = sleeveless

