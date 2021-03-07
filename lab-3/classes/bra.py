from . import underwear


class Bra(underwear.Underwear):
    def __init__(self, style, cups_size, lining_level, number_of_hooks, collection, year_of_production, color, price,
                 pants="None"):
        super().__init__(collection, year_of_production, color, price)
        self.__style = style
        self.__cups_size = cups_size
        self.__lining_level = lining_level
        self.__number_of_hooks = number_of_hooks
        self.__perfect_pair_of_pants = pants

    def __str__(self):
        return f'collection = {self._collection} \n' \
               f'year of production = {self._year_of_production} \n' \
               f'color = {self._color} \n' \
               f'price in bucks =  {self._price} \n'\
               f'style = {self.__style} \n' \
               f'cups size = {self.__cups_size} \n' \
               f'lining level = {self.__lining_level} \n' \
               f'number of hooks =  {self.__number_of_hooks} \n' \
               f'perfect pair of pants = {self.__perfect_pair_of_pants} \n'

    def get_style(self):
        return self.__style

    def get_cups_size(self):
        return self.__cups_size

    def get_lining_level(self):
        return self.__lining_level

    def get_number_of_hooks(self):
        return self.__number_of_hooks

    def get_perfect_pair_of_pants(self):
        return self.__perfect_pair_of_pants

    def set_style(self, style):
        self.__style = style

    def set_cups_size(self, cups_size):
        self.__cups_size = cups_size

    def set_lining_level(self, lining_level):
        self.__lining_level = lining_level

    def set_number_of_hooks(self, number_of_hooks):
        self.__number_of_hooks = number_of_hooks

    def set_perfect_pair_of_pants(self, pants):
        self.__perfect_pair_of_pants = pants
