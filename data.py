
class GetCars:
    def __init__(self):
        self.__getData = GetData()
        # Get the data from the car csv file
        self.__carsWholeR = open('data/cars.csv')

    def carData(self):
        return self.__getData.__fileData__(self.__carsWholeR)

class GetCustomers:
    def __init__(self):
        self.__getData = GetData()
        # Gets the data from the customer csv file
        self.__customersWholeR = open('data/customers.csv')
        self.__customersWholeA = open('data/customers.csv', 'a')

    def customerData(self):
        return self.__getData.__fileData__(self.__customersWholeR)

    def customerInsert(self, name, age):
        string = '\n' + name + ',' + age
        self.__customersWholeA.write(string)
        self.__customersWholeA.close()


class GetOrders:
    def __init__(self):
        self.__getData = GetData()
        # Gets the data from the order csv file
        self.__ordersWholeR = open('data/orders.csv')
        self.__ordersWholeA = open('data/orders.csv', 'a')

    def orderData(self):
        return self.__getData.__fileData__(self.__ordersWholeR)

    def orderInsert(self, employee, timeOfOrder,
                    timeOfPickUp, timeOfReturn, carNumber):

        string = '\n ' + employee + ',' + timeOfOrder + ',' \
              + timeOfPickUp + ',' + timeOfReturn + ',' + carNumber

        self.__ordersWholeA.write(string)
        self.__ordersWholeA.close()


class GetEmployees:
    def __init__(self):
        self.__getData = GetData()
        # Gets the data from the employees csv file
        self.__employeesWholeR = open('data/employees.csv')

    def emplyeeData(self):
        return self.__getData.__fileData__(self.__employeesWholeR)


class GetData:
    def __fileData__(self, file):
        # Makes an arrays of the lines taken from the cars.csv file
        with file as l:
            fileWhole = l.readlines()
        # Gets the amount of cars in the file
        fileAmount = len(fileWhole)
        # Gets the amount of variables a car has
        fileVariables = fileWhole[0].count(' ')+1
        # Makes an empty fileVariable x fileAmount matrix of arrays.
        fileMatrix = [[0] * fileVariables for i in range(fileAmount)]
        # Inserts the values from the file into the array
        i = 0
        # Further splits each car line into its
        # variables, and inputs it into the empty matrix
        for car in fileWhole:
            c = car.split(',')
            fileMatrix[i] = c
            i += 1
        file.close()
        return fileMatrix
