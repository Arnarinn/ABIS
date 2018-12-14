from Business.cardomain import CarDomain
import os

class CarUi:


    def __init__(self):
        self.__dom = CarDomain()


    #Prints a table with the contents of myCarList
    def printCSTable(self, myCarList,index, search):
        print(' ------------------------------------------------')
        #Table has 4 colums with size: 15, 15, 10, 10 respectively
        # columns are filled with strings
        # columns are aligned to the left                  
        print('%-10s%-13s%-9s%-9s%-7s' % ('|' + 'Type', '|' + 'Manufacturer',
            '|' + 'Plate Nr', '|' + 'Price   ' + '|', 'Status' + '|'))
        print(' ================================================')
        i = 0
        for x in myCarList:
            if i == index and search == 'y':
                print('%-10s%-13s%-9s%-9s%-7s' % ('|' + x.getType(),
                     '|' + x.getManufacturer(),
                     '|' + x.getPlate(), '|' + x.getCost() + '|',
                      x.getStatus() + '      |') + '<---')
                print(' ------------------------------------------------')
            else:
                print('%-10s%-13s%-9s%-9s%-7s' % ('|' + x.getType(),
                                                  '|' + x.getManufacturer(),
                                                  '|' + x.getPlate(), '|' + x.getCost() + '|',
                                                  x.getStatus() + '     |'))
                print(' ------------------------------------------------')
            i += 1


    def printCMTable(self, myCarList, index, search):
        print('--------------------------------------------------')
        #Table has 4 colums with size: 15, 15, 10, 10 respectively
        # columns are filled with strings
        # columns are aligned to the left
        print('%-10s%-13s%-7s%-10s%-5s%-9s%-12s%-12s%-10s%-9s%-18s%-17s%-7s%-9s' % ('|' + 'Type', '|' + 'Manufacturer',
            '|'+ 'Color','|'+ 'Distance','|' + 'Year','|' +'Plate Nr',
            '|'+ 'Nr of seats', '|' + 'Nr of doors',
            '|'+ 'Inspected', '|' + 'Fuel', '|' + 'Wheel drive',
            '|'+ 'Shifting option','|'+ 'Status','|' + 'Price   ' +'|'))
        print(' =================================================================================================================================================== ')
        i = 0
        for x in myCarList:
            if i == index and search == 'y':
                print('%-10s%-13s%-7s%-10s%-5s%-9s%-12s%-12s%-10s%-9s%-18s%-17s%-7s%-9s' % ('|' + x.getType(),
                    '|' + x.getManufacturer(),
                    '|' + x.getColor(), '|' + x.getDistance(), '|' + x.getYear(),
                    '|' + x.getPlate(),  '|' + x.getSeats(), '|' + x.getDoors(),
                    '|' + x.getInspected(), '|' + x.getFuel(), '|' + x.getWheelDrive(),
                    '|' + x.getShifting(), '|' + x.getStatus(), '|' + x.getCost() + '|') + '<---')
                print(' --------------------------------------------------------------------------------------------------------------------------------------------------- ')
            else:
                print('%-10s%-13s%-7s%-10s%-5s%-9s%-12s%-12s%-10s%-9s%-18s%-17s%-7s%-9s' % ('|' + x.getType(),
                      '|' + x.getManufacturer(),
                      '|' + x.getColor(), '|' + x.getDistance(), '|' + x.getYear(),
                      '|' + x.getPlate(), '|' + x.getSeats(), '|' + x.getDoors(),
                      '|' + x.getInspected(), '|' + x.getFuel(), '|' + x.getWheelDrive(),
                      '|' + x.getShifting(), '|' + x.getStatus(), '|' + x.getCost() + '|'))
                print(
                    ' --------------------------------------------------------------------------------------------------------------------------------------------------- ')
            i += 1
    def retCarData(self):
        return self.__dom.retCarData()

    def findCars(self, plate):
        cars = []
        for c in self.retCarData():
            if plate in c.getPlate():
                cars.append(c)
        return cars


    def AvailableCars(self):
        return self.__dom.availableCars()
        

    #Calls the printTable function on all unavailable cars
    def UnavailableCars(self):
        return self.__dom.unavailableCars()


    def returnCar(self, car):
        self.__dom.setAsAvailable(car.getPlate())

        comp = self.__dom.setAsAvailable(car.getPlate())
        if comp == 1:
            print('Car has been returned')
        else:
            print('Something went wrong')

    def deliverCar(self, car):
        self.__dom.setAsUnavailable(car.getPlate())


