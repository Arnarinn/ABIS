from Repositories.getcars import GetCars

class CarDomain:

    def __init__(self):
        cars = GetCars()
        self.__carList = cars.carData()


    def availableCars(self):
        aCars = []
        for x in self.__carList:
            if x.getStatus() == 0:
                aCars.append(x)


    def unavailableCars(self):
        uACars = []
        for x in self.__carList:
            if x.getStatus() == 1:
                uACars.append(x)
    