class Car:
    def __init__(self, manufacturer, color, cost, licensePlate,
                 distance, year, carType, numberOfSeats, numberOfDoors,
                 inspected, fuel, wheelDrive, shiftingOption, status):
        self.__manufacturer = manufacturer
        self.__color = color
        self.__cost = cost
        self.__licensePlate = licensePlate
        self.__distance = distance
        self.__year = year
        self.__carType = carType
        self.__numberOfSeats = numberOfSeats
        self.__numberOfDoors = numberOfDoors
        self.__inspected = inspected
        self.__fuel = fuel
        self.__wheelDrive = wheelDrive
        self.__shiftingOption = shiftingOption
        self.__status = status

    def __str__(self):
        return 'manufacturer: {}, color: {}, cost: {}, licensePlate: {}, ' \
               'distance: {}, year: {}, carType: {}, numberOfSeats: {}, ' \
               'numberOfDoors: {}, inspected: {}, fuel: {}, wheelDrive: ' \
               '{}, shiftingOption: {}, status: {}'.format(self.__manufacturer, self.__color,
                                                           self.__cost, self.__licensePlate,
                                                           self.__distance, self.__year, self.__carType,
                                                           self.__numberOfSeats, self.__numberOfDoors,
                                                           self.__inspected, self.__fuel, self.__wheelDrive,
                                                           self.__shiftingOption, self.__status)

    def __repr__(self):
        return 'Car:({},{},{},{},{},{},{},' \
               '{},{},{},{},{},{},{})'.format(self.__manufacturer, self.__color,
                                              self.__cost, self.__licensePlate,
                                              self.__distance, self.__year, self.__carType,
                                              self.__numberOfSeats, self.__numberOfDoors,
                                              self.__inspected, self.__fuel, self.__wheelDrive,
                                              self.__shiftingOption, self.__status)


    def getManufacturer(self):
        return self.__manufacturer

    def getColor(self):
        return self.__color
    
    def getCost(self):
        return self.__cost

    def getPlate(self):
        return self.__licensePlate

    def getDistance(self):
        return self.__distance

    def getYear(self):
        return self.__year

    def getType(self):
        return self.__carType

    def getSeats(self):
        return self.__numberOfSeats

    def getDoors(self):
        return self.__numberOfDoors

    def getInspected(self):
        return self.__inspected

    def getFuel(self):
        return self.__fuel

    def getWheelDrive(self):
        return self.__wheelDrive

    def getShifting(self):
        return self.__shiftingOption
    
    def getStatus(self):
        return self.__status
    
    def setStatus(self, newStatus):
        if newStatus == '1' or newStatus == '0':
            self.__status = newStatus
        else:
            print('Invalid Input')

    def dataList(self):
        dList = []
        dList.append(self.__manufacturer)
        dList.append(self.__color)
        dList.append(self.__cost)
        dList.append(self.__licensePlate)
        dList.append(self.__distance)
        dList.append(self.__year)
        dList.append(self.__carType)
        dList.append(self.__numberOfSeats)
        dList.append(self.__numberOfDoors)
        dList.append(self.__inspected)
        dList.append(self.__fuel)
        dList.append(self.__wheelDrive)
        dList.append(self.__shiftingOption)
        dList.append(self.__status)
        return dList
