from . import enums


class UnderwearManager:

    __underwear_list = []

    def get_underwear_list(self):
        return self.__underwear_list

    def set_underwear_list(self, list_of_underwear):
        self.__underwear_list = list_of_underwear

    def add_underwear(self, underwear):
        self.__underwear_list.append(underwear)

    def search_by_collection(self, collection):
        searched_collection = []
        for i in self.__underwear_list:
            if i.get_collection() == collection:
                searched_collection.append(i)
        return searched_collection

    def search_by_year(self, year):
        searched_year = []
        for i in self.__underwear_list:
            if i.get_year_of_production() == year:
                searched_year.append(i)
        return searched_year

    def sort_by_price(self, order):
        if order == enums.SortOrder.ASC:
            self.__underwear_list.sort(key=lambda c: c.get_price())
        else:
            self.__underwear_list.sort(key=lambda c: c.get_price(), reverse=True)
