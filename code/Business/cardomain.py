from Repositories.getcars import GetCars


class CarDomain:


    def __init__(self):
        cars = GetCars()
        self.__carList = cars.carData()


    def __str__(self):
        return '{}'.format(self.__carList)


    # Returns a list of all available cars
    def availableCars(self):
        aCars = []
        for x in self.__carList:
            if x.getStatus() == '0':
                aCars.append(x)
        return aCars


    # Made for testing
    def setSomeAsUnavailable(self):
        aCars = self.availableCars()
        for x in range(10):
            aCars[x].setStatus('1')


    # Returns a list of all unavailable cars
    def unavailableCars(self):
        uACars = []
        for x in self.__carList:
            if x.getStatus() == '1':
                uACars.append(x)
        return uACars
