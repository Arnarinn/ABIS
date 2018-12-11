from Business.cardomain import CarDomain

class CarUi:


    def __init__(self):
        self.__dom = CarDomain()


    #Prints a table with the contents of myCarList
    def printCSTable(self, myCarList):                                                 
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

     def printCMTable(self, myCarList):                                                 
        print('--------------------------------------------------')
        #Table has 4 colums with size: 15, 15, 10, 10 respectively
        # columns are filled with strings
        # columns are aligned to the left                  
        print('%-15s%-15s%-15s%-15s%-15s-15s%-15s%-10s%-10s%-10s-15s%-10s-10s%' % ('|' + 'Type', '|' + 'Manufacturer', \
            '|' + 'Color', '|' + 'Distance', '|' + 'Year', '|' + 'Plate Nr', \ 
            '|' + 'Number of seats', '|' + 'Number of doors', \ 
            '|' + 'Inspected', '|' + 'Fuel', '|' + 'Wheel drive', \
            '|' + 'Shifting option', '|' + 'Status', '|' + 'Price ' + '|'))                               
        print('==================================================')                  
        for x in myCarList:                                                          
            print('%-15s%-15s%-15s%-15s%-15s-15s%-15s%-10s%-10s%-10s-15s%-10s-10s%' % ('|' + x.getType(),\
                '|' + x.getManufacturer(),\
                '|' + x.getColor(), '|' + x.getDistance(), '|' + x.getYear(), \ 
                '|' + x.getPlate(),  '|' + x.getSeats(), '|' + x.getDoors(), \
                '|' + x.getInspected(), '|' + x.getFuel(), '|' + x.getWheel(), \
                '|' + x.getShifting(), '|' + x.getSatus(), '|' + x.getCost() + '|'))                       
            print('--------------------------------------------------')
    #Calls the printTable function on all available cars
    def dispAvailableCars(self):                                                                                        
        self.printTable(self.__dom.availableCars()) 
        

    #Calls the printTable function on all unavailable cars
    def dispUnavailableCars(self):                                                                        
        self.printTable(self.__dom.unavailableCars())
    
    #Calls the printTable function on all returned cars
    def dispReturnedCars(self):
        self.printTable(self.__dom.returnedCars())
    
    #Calls the printTable function on all delivered cars
    def dispDeliveredCars(self):
        self.printTable(self.__dom.deliveredCars())