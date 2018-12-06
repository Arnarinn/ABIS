from Repositories.getcars import GetCars


class CarDomain:


    def __init__(self):
        cars = GetCars()
        self.__carList = cars.carData()


    def __str__(self):
        return '{}'.format(self.__carList)


    # Returns a list of all available cars
    def availableCars(self):
        aCars = []
        for x in self.__carList:
            if x.getStatus() == '0':
                aCars.append(x)
        return aCars


    # Made for testing
    def setAllAsUnavailable(self):
        aCars = self.availableCars()
        for x in aCars:
            x.setStatus('1')


    # Returns a list of all unavailable cars
    def unavailableCars(self):
        uACars = []
        for x in self.__carList:
            if x.getStatus() == '1':
                uACars.append(x)
        return uACars


    # THE NEXT 3 FUNCTIONS MIGHT BELONG TO THE UI LAYER
    ##################################################################################
    # Prints a table with                                                            #
    def printTable(self, myCarList):                                                 #
        print('--------------------------------------------------')                  #
        print('%-15s%-15s%-10s%-10s' % ('|' + 'Type', '|' + 'Manufacturer', \        
            '|' + 'Plate Nr', '|' + 'Price   ' + '|'))                               #
        print('==================================================')                  #
        for x in myCarList:                                                          #
            print('%-15s%-15s%-10s%-10s' % ('|' + x.getType(),\                      
                 '|' + x.getManufacturer(),\ 
                 '|' + x.getPlate(), '|' + x.getCost() + '|'))                       #
            print('--------------------------------------------------')              #
                                                                                     #
    # Displays information about available cars relevant to customers                #
    def dispAvailableCars(self):                                                     #
        listOfAvailables = self.availableCars()                                      #
        self.printTable(listOfAvailables)                                            #
                                                                                     #
    # Displays information about unavailable cars relevant to customers              #
    def dispUnavailableCars(self):                                                   #
        listOfUnavailables = self.unavailableCars()                                  #
        self.printTable(listOfUnavailables)                                          #
    ##################################################################################

