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
        print('%-10s%-13s%-7s%-10s%-5s%-9s%-12s%-12s%-10s%-9s%-18s%-17s%-7s%-9s' % ('|' + 'Type', '|' + 'Manufacturer',\
            '|'+ 'Color','|'+ 'Distance','|' + 'Year','|' +'Plate Nr',\
            '|'+ 'Nr of seats', '|' + 'Nr of doors',\
            '|'+ 'Inspected', '|' + 'Fuel', '|' + 'Wheel drive',\
            '|'+ 'Shifting option','|'+ 'Status','|' + 'Price   ' +'|'))
        print(' =================================================================================================================================================== ')
        for x in myCarList:
            print('%-10s%-13s%-7s%-10s%-5s%-9s%-12s%-12s%-10s%-9s%-18s%-17s%-7s%-9s' % ('|' + x.getType(),\
                '|' + x.getManufacturer(),\
                '|' + x.getColor(), '|' + x.getDistance(), '|' + x.getYear(), \
                '|' + x.getPlate(),  '|' + x.getSeats(), '|' + x.getDoors(), \
                '|' + x.getInspected(), '|' + x.getFuel(), '|' + x.getWheelDrive(), \
                '|' + x.getShifting(), '|' + x.getStatus(), '|' + x.getCost() + '|'))
            print(' --------------------------------------------------------------------------------------------------------------------------------------------------- ')


    #Calls the printTable function on all available cars
    def CSDispAvailableCars(self):                                                                                        
        self.printCSTable(self.__dom.availableCars()) 
        

    #Calls the printTable function on all unavailable cars
    def CSDispUnavailableCars(self):                                                                        
        self.printCSTable(self.__dom.unavailableCars())
    

    def CMDispAvailableCars(self):                                                                                        
        self.printCMTable(self.__dom.availableCars()) 
        

    #Calls the printTable function on all unavailable cars
    def CMDispUnavailableCars(self):                                                                        
        self.printCMTable(self.__dom.unavailableCars())