import csv


def formatData(file):
    array = []
    with file as dataFile:
        data = csv.reader(dataFile)
        next(data)
        for line in data:
            array.append(line)
    return array


class Car:
    def __init__(self):
        self.__color = 'red'


class GetCars:
    def carData(self):
        return formatData(open('data/cars.csv'))


class Customer:
    def __init__(self, ssn, name, age):
        self.__ssn = ssn
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'Name: {}, Age: {}, SSN: {}'.format(self.__name, self.__age, self.__ssn)

    def __repr__(self):
        return 'Customer({},{},{})'.format(self.__name, self.__age, self.__ssn)


class GetCustomers:
    def customerData(self):
        formattedData = formatData(open('data/customers.csv'))
        customerObjectArray = []
        for line in formattedData:
            customerObjectArray.append(Customer(line[0], line[1], line[2]))
        return customerObjectArray
        # return formatData(open('data/customers.csv'))

    def customerInsert(self, customer):
        with open('data/customers.csv', 'a+') as customerFile:
            customerFile.write(customer.__repr__() + '\n')


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


class GetOrders:
    def orderData(self):
        # Makes a ordersObjectArray which makes an empty array
        # and then it creates an object of the relevant type and inputs
        # it into the array and returns it.
        formattedData = formatData(open('data/orders.csv'))
        ordersObjectArray = []
        for line in formattedData:
            ordersObjectArray.append(Order(line[0], line[1], line[2], line[3], line[4]))
        return ordersObjectArray

    def orderInsert(self, order):
        with open('data/orders.csv', 'a+') as orderFile:
            orderFile.write(order.__repr__() + '\n')


class GetEmployees:
    def emplyeeData(self):
        return formatData(open('data/employees.csv'))

