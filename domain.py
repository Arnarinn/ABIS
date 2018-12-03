from data import GetData


class Domain:
    def __init__(self):
        self.__data = GetData()

    def getCustomerData(self):
        return self.__data.customerData()

    def getCarData(self):
        return self.__data.carData()

    def getOrderData(self):
        return self.__data.orderData()

    def insertCustomer(self, name, age):
        self.__data.customerInsert(name, age)

    def insertOrder(self, employee, timeOfOrder, timeOfPickUp, timeOfReturn, carNumber):
        self.__data.orderInsert(employee, timeOfOrder, timeOfPickUp, timeOfReturn, carNumber)

    def checkLogin(self, username, password):
        employeeData = self.__data.emplyeeData()
        for e in employeeData:
            if e[0] == username:
                if e[1] == password:
                    return True
        return False
