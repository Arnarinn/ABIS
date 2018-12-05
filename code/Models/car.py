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
