class Temperature:
    def __init__(self, temperature):
        self.__temperature = temperature

    # convert celcius to farenheight
    def set_to_farenheight(self, temperature):
        self.__temperature = (temperature * 9/5) + 32

    def get_farenheight(self):
        return self.__temperature

    # convert celcius to kelvin

    def set_to_kelvin(self, temperature):
        self.__temperature = temperature + 273.15

    def get_kelvin(self):
        return self.__temperature


    # creating an instance
temp1 = Temperature(0)
temp1.set_to_farenheight(37)
print(temp1.get_farenheight())
