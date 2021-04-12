class Microcontroller:
    static_variable = "static"

    @staticmethod
    def static():
        print(f'static variable is "{Microcontroller.static_variable}"')

    def __init__(self, CPU_clock_speed = 0.011, bit_rate = 8, producer = "Intel",
                 year_of_production = 1980, name = "", memory = "64"):
        self.CPU_clock_speed = CPU_clock_speed # clock speed in GHz
        self.bit_rate = bit_rate
        self.producer = producer
        self.year_of_production = year_of_production
        self.name = name
        self.memory = memory # memory in KB

    def __del__(self):
        print("Destructor of Microcontroller")

    def __str__(self):
        if self.name:
            return f'CPU clock speed in GHz = {self.CPU_clock_speed} \n' \
                   f'bit rate = {self.bit_rate} \n' \
                   f'producer = {self.producer} \n' \
                   f'name = {self.name} \n' \
                   f'year of production =  {self.year_of_production} \n' \
                   f'memory in KB = {self.memory}'
        return f'CPU clock speed in GHz = {self.CPU_clock_speed} \n' \
               f'bit rate = {self.bit_rate} \n' \
               f'producer = {self.producer} \n' \
               f'year of production =  {self.year_of_production} \n' \
               f'memory in KB = {self.memory}'
