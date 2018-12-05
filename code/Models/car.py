class Car:
    def __init__(self, manufacturer, color, cost, licensePlate,
                 distance, year, carType, numberOfSeats, numberOfDoors,
                 inspected, fuel, wheelDrive, shiftingOption, status):
        self.manufacturer = manufacturer
        self.color = color
        self.cost = cost
        self.licensePlate = licensePlate
        self.distance = distance
        self.year = year
        self.carType = carType
        self.numberOfSeats = numberOfSeats
        self.numberOfDoors = numberOfDoors
        self.inspected = inspected
        self.fuel = fuel
        self.wheelDrive = wheelDrive
        self.shiftingOption = shiftingOption
        self.status = status

    def __str__(self):
        return 'manufacturer: {}, color: {}, cost: {}, licensePlate: {}, ' \
               'distance: {}, year: {}, carType: {}, numberOfSeats: {}, ' \
               'numberOfDoors: {}, inspected: {}, fuel: {}, wheelDrive: ' \
               '{}, shiftingOption: {}, status: {}'.format(self.manufacturer, self.color,
                                                           self.cost, self.licensePlate,
                                                           self.distance, self.year, self.carType,
                                                           self.numberOfSeats, self.numberOfDoors,
                                                           self.inspected, self.fuel, self.wheelDrive,
                                                           self.shiftingOption, self.status)

    def __repr__(self):
        return 'Car:({},{},{},{},{},{},{},' \
               '{},{},{},{},{},{},{})'.format(self.manufacturer, self.color,
                                              self.cost, self.licensePlate,
                                              self.distance, self.year, self.carType,
                                              self.numberOfSeats, self.numberOfDoors,
                                              self.inspected, self.fuel, self.wheelDrive,
                                              self.shiftingOption, self.status)
