class Underwear:
    def __init__(self, collection, year_of_production, color, price):
        self._collection = collection
        self._year_of_production = year_of_production
        self._color = color
        self._price = price

    def __str__(self):
        return f'collection = {self._collection} \n' \
               f'year of production = {self._year_of_production} \n' \
               f'color = {self._color} \n' \
               f'price in bucks=  {self._price} \n'

    def get_collection(self):
        return self._collection

    def get_year_of_production(self):
        return self._year_of_production

    def get_color(self):
        return self._color

    def get_price(self):
        return self._price

    def set_collection(self, collection):
        self._collection = collection

    def set_year_of_production(self, year_of_production):
        self._year_of_production = year_of_production

    def set_color(self, color):
        self._color = color

    def set_price(self, price):
        self._price = price
