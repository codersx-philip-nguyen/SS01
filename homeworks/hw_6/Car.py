class Car:
    def __init__(self, make, year_model):
        self.__make= make
        self.__year_model = year_model
        self.__speed = 0
     #speed up by 5
    def accelearate(self):
        self.__speed += 5
    #slow down by 5
    def brake(self):
        self.__speed -= 5
    # get speed
    def get_speed(self):
        return self.__speed

newCar = Car('Maybach', 'abcdefg')
for i in range (5):
    newCar.accelearate()
    speed = newCar.get_speed()
    print("Speed up ",i, ': ', speed)
for i in range (5):
    newCar.brake()
    speed = newCar.get_speed()
    print("Speed down",i, ': ', speed)