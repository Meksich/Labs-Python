from microcontroller import Microcontroller


first_microcontroller = Microcontroller()

second_microcontroller = Microcontroller(3.6, 64, year_of_production = 2017, name ="i3 8100", memory = 6144 )

third_microcontroller = Microcontroller(5.7, 32, "Renesas")

print("-------Microcontroller 1-------\n")
print(first_microcontroller)
print("-------------------------------\n")
print("-------Microcontroller 1-------\n")
print(second_microcontroller)
print("-------------------------------\n")
print("-------Microcontroller 1-------\n")
print(third_microcontroller)
print("-------------------------------\n")

Microcontroller.static()