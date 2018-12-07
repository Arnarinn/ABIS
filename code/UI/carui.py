from Business.cardomain import CarDomain

class CarUi:


    def __init__(self):
        self.__dom = CarDomain()


    #Prints a table with the contents of myCarList
    def printTable(self, myCarList):                                                 
        print('--------------------------------------------------')
        #Table has 4 colums with size: 15, 15, 10, 10 respectively
        # columns are filled with strings
        # columns are aligned to the left                  
        print('%-15s%-15s%-10s%-10s' % ('|' + 'Type', '|' + 'Manufacturer', \
            '|' + 'Plate Nr', '|' + 'Price   ' + '|'))                               
        print('==================================================')                  
        for x in myCarList:                                                          
            print('%-15s%-15s%-10s%-10s' % ('|' + x.getType(),\
                 '|' + x.getManufacturer(),\
                 '|' + x.getPlate(), '|' + x.getCost() + '|'))                       
            print('--------------------------------------------------')


    #Calls the printTable function on all available cars
    def dispAvailableCars(self):                                                                                        
        self.printTable(self.__dom.availableCars()) 
        

    #Calls the printTable function on all unavailable cars
    def dispUnavailableCars(self):                                                                        
        self.printTable(self.__dom.unavailableCars())