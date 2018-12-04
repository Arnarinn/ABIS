class Order:
    def __init__(self, employee, timeOfOrder,
                 timeOfPickup, timeOfReturn, carNumber):
        self.__employee = employee
        self.__timeOfOrder = timeOfOrder
        self.__timeOfPickup = timeOfPickup
        self.__timeOfReturn = timeOfReturn
        self.__carNumber = carNumber

    def __str__(self):
        return 'Employee: {}, Time of order: {}, Time of Pickup: {}, Time of return: ' \
               '{}, Car number: {}'.format(self.__employee,
                                           self.__timeOfOrder,
                                           self.__timeOfPickup,
                                           self.__timeOfReturn,
                                           self.__carNumber)

    def __repr__(self):
        return 'Order({},{},{},{},{})'.format(self.__employee,
                                              self.__timeOfOrder,
                                              self.__timeOfPickup,
                                              self.__timeOfReturn,
                                              self.__carNumber)
