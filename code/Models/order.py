# REMEMBER TO ADD EMPLOYEE
class Order:
    def __init__(self, customer, timeOfOrder,
                 timeOfPickup, timeOfReturn, carNumber, carType,
                 insurance, price):
        self.__customer = customer
        self.__timeOfOrder = timeOfOrder
        self.__timeOfPickup = timeOfPickup
        self.__timeOfReturn = timeOfReturn
        self.__carNumber = carNumber
        self.__carType = carType
        self.__insurance = insurance
        self.__price = price

    def __str__(self):
        return 'Customer: {}, Time of order: {}, Time of Pickup: '\
                '{}, Time of return: {}, Car number: {}, Car type: {}, Insurance: '\
                '{}, Price: {}'\
               .format(self.__customer,
                       self.__timeOfOrder,
                       self.__timeOfPickup,
                       self.__timeOfReturn,
                       self.__carNumber,
                       self.__carType,
                       self.__insurance,
                       self.__price)

    def __repr__(self):
        return 'Order({},{},{},{},{},{},{},{})'.format(self.__customer,
                                                       self.__timeOfOrder,
                                                       self.__timeOfPickup,
                                                       self.__timeOfReturn,
                                                       self.__carNumber,
                                                       self.__carType,
                                                       self.__insurance,
                                                       self.__price)

                            
    def dataList(self):
        dList = []

        dList.append(self.__customer)
        dList.append(self.__timeOfOrder)
        dList.append(self.__timeOfPickup)
        dList.append(self.__timeOfReturn)
        dList.append(self.__carNumber)
        dList.append(self.__carType)
        dList.append(self.__insurance)
        dList.append(self.__price)

        return dList

    def getCarPlate(self):
        return  self.__carNumber

    def getSsn(self):
        return self.__customer

    def getDateOfOrder(self):
        return self.__timeOfOrder

    def getCarType(self):
        return self.__carType

    def getReturn(self):
        return self.__timeOfReturn

    def getPickup(self):
        return self.__timeOfPickup