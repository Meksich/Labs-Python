class Microcontroller():
    static_variable = "static"

    __CPU_clock_speed = None
    __bit_rate = None
    __producer = None
    __year_of_production = None
    __name = None
    __memory = None
    @staticmethod
    def static():
        print(f'static variable is "{Microcontroller.static_variable}"')

    def __init__(self, CPU_clock_speed = 0.011, bit_rate = 8, producer = "Intel",
                 year_of_production = 1984, name = "", memory = "64"):
        self.__CPU_clock_speed = CPU_clock_speed # clock speed in GHz
        self.__bit_rate = bit_rate
        self.__producer = producer
        self.__year_of_production = year_of_production
        self.__name = name
        self.__memory = memory # memory in KB

    def __del__(self):
        print("Destructor of Microcontroller")

    def __str__(self):
        if self.__name:
            return f'CPU clock speed in GHz = {self.__CPU_clock_speed} \n' \
                   f'bit rate = {self.__bit_rate} \n' \
                   f'producer = {self.__producer} \n' \
                   f'name = {self.__name} \n' \
                   f'year of production =  {self.__year_of_production} \n' \
                   f'memory in KB = {self.__memory}'
        return f'CPU clock speed in GHz = {self.__CPU_clock_speed} \n' \
               f'bit rate = {self.__bit_rate} \n' \
               f'producer = {self.__producer} \n' \
               f'year of production =  {self.__year_of_production} \n' \
               f'memory in KB = {self.__memory}'


def main():
    first_microcontroller = Microcontroller()

    second_microcontroller = Microcontroller(3.6, 64, year_of_production = 2017, name ="i3 8100", memory = 6144 )

    third_microcontroller = Microcontroller(5.7, 32, "Renesas")

    print("-------Microcontroller 1-------\n")
    print(first_microcontroller)
    print("-------------------------------\n")
    print("-------Microcontroller 2-------\n")
    print(second_microcontroller)
    print("-------------------------------\n")
    print("-------Microcontroller 3-------\n")
    print(third_microcontroller)
    print("-------------------------------\n")

    Microcontroller.static()


if __name__ == '__main__':
    main()