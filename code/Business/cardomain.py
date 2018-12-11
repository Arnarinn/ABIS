from Repositories.getcars import GetCars


class CarDomain:


    def __init__(self):
        self.__cars = GetCars()
        self.__carList = self.__cars.carData()


    def __str__(self):
        return '{}'.format(self.__carList)


    # Returns a list of all available cars
    def availableCars(self):
        aCars = []
        for x in self.__carList:
            if x.getStatus() == '0':
                aCars.append(x)
        return aCars


    
    def setAsUnavailable(self, carPlate):
        for x in self.__carList:
            if x.getPlate() == str(carPlate):
                if x.getStatus == '1':
                    print('Car alredy unavailable')
                    return
                x.setStatus('1')
                break
        self.__cars.carInsert(self.__carList)


    # Returns a list of all unavailable cars
    def unavailableCars(self):
        uACars = []
        for x in self.__carList:
            if x.getStatus() == '1':
                uACars.append(x)
        return uACars


    def getNextAvailableCar(self, cType):
        available = self.availableCars()
        
        for x in available:
            if x.getType() == str(cType):
                return x
        print('No cars availabli in this class')

    # Mark car as returned
    #def returnedCars(self):

    # Mark car as delivered
     #def deliveredCars(self):
        