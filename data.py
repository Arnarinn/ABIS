import datetime

class getData:
    def __init__(self):
        # Get the data from the car csv file
        self.carsWholeR = open('data/cars.csv')
        # Gets the data from the customer csv file
        self.customersWholeR = open('data/customers.csv')
        self.customersWholeA = open('data/customers.csv', 'a')
        # Gets the data from the order csv file
        self.ordersWholeR = open('data/orders.csv')
        self.ordersWholeA = open('data/orders.csv', 'a')

    def __fileInit__(self, file):
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
        i: int = 0
        # Further splits each car line into its
        # variables, and inputs it into the empty matrix
        for car in fileWhole:
            c = car.split(',')
            fileMatrix[i] = c
            i += 1
        self.carsWholeR.close()
        return fileMatrix

    def carInit(self):
        return self.__fileInit__(self.carsWholeR)

    def customerInit(self):
        return self.__fileInit__(self.customersWholeR)

    def orderInit(self):
        return self.__fileInit__(self.ordersWholeR)

    def orderInsert(self, employee, timeOfOrder,
                    timeofPickUp, timeOfReturn, carNumber):
        str = '\n'+employee+','+timeOfOrder+','\
              +timeofPickUp+','+timeOfReturn+','+carNumber
        self.ordersWholeA.write(str)
        self.ordersWholeA.close()

    def customerInsert(self, name, age):
        str = '\n'+name+','+age
        self.customersWholeA.write(str)
        self.customersWholeA.close()
