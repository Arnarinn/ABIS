from Business.orderdomain import OrderDomain
from Business.cardomain import CarDomain
from Models.insurance import Insurance
from datetime import datetime
import os


class OrderUi:


    def __init__(self):
        self.__dom = OrderDomain()
        self.__carDom = CarDomain()


    def newOrder(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        newOrderData = []
        newOrderData.append(input('Customer SSN: '))
        newOrderData.append(datetime(int(datetime.today().year), \
                                     int(datetime.today().month), \
                                     int(datetime.today().day), \
                                     int(datetime.today().hour), \
                                     int(datetime.today().minute), \
                                     int(datetime.today().second)))

        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('Pickup Date (YYYY/MM/DD): ')    
        yy = int(input('YYYY: '))
        mm = int(input('MM: '))
        dd = int(input('DD: '))
        pDate = datetime(yy, mm, dd)
        newOrderData.append(pDate)

        os.system('cls' if os.name == 'nt' else 'clear')

        print('Return Date (YYYY/MM/DD: ')
        yy = int(input('YYYY: '))
        mm = int(input('MM: '))
        dd = int(input('DD: '))
        rDate = datetime(yy, mm, dd)
        newOrderData.append(rDate)

        os.system('cls' if os.name == 'nt' else 'clear')

        typ = int(input('Car type:\n1. Sedan\n2. Sport\n3. Jeep\n'))
        
        price = 0
        if typ == 1:
            car = self.__carDom.getNextAvailableCar('sedan')
            self.__carDom.setAsUnavailable(car.getPlate())
            newOrderData.append(str(car.getPlate()))
            newOrderData.append('sedan')
            price += self.__dom.calculateBasePrice(pDate, rDate, typ)
        elif typ == 2:
            car = self.__carDom.getNextAvailableCar('sport')
            self.__carDom.setAsUnavailable(car.getPlate())
            newOrderData.append(str(car.getPlate()))
            newOrderData.append('sport')
            price += self.__dom.calculateBasePrice(pDate, rDate, typ)
        elif typ == 3:
            car = self.__carDom.getNextAvailableCar('jeep')
            self.__carDom.setAsUnavailable(car.getPlate())
            newOrderData.append(str(car.getPlate()))
            newOrderData.append('jeep')
            price += self.__dom.calculateBasePrice(pDate, rDate, typ)
        else:
            print('invalid input')

        os.system('cls' if os.name == 'nt' else 'clear')

        ins = int(input('Insurance lvl:\n1. Lvl1\n2. Lvl2\n3. Lvl3\n'))
        insurancelvl = Insurance()
        if ins == 1:
            newOrderData.append('lvl1')
            price += insurancelvl.getLvl1()
        elif ins == 2:
            newOrderData.append('lvl2')
            price += insurancelvl.getLvl2()
        elif ins == 3:
            newOrderData.append('lvl3')
            price += insurancelvl.getLvl3()
        else:
            print('invalid input')
        
        newOrderData.append(price)
        self.__dom.createOrder(newOrderData)


        #Prints a table with the contents of orderList
    def printTable(self, myOrderList):                                                 
        print(' --------------------------------------------------------------------------------------------- ')                 
        print('%-11s%-12s%-9s%-21s%-21s%-21s' % ('|' + 'SSN', '|' + 'Car Plate', \
            '|' + 'Car Type', '|' + 'Date of Order', '|' + 'Pickup', '|' + 'Return' + '             |'))                               
        print(' ============================================================================================= ')                  
        for x in myOrderList:                                                          
            print('%-11s%-12s%-9s%-21s%-21s%-21s' % ('|' + x.getSsn(),\
                 '|' + x.getCarPlate(),\
                 '|' + x.getCarType(), '|' + x.getDateOfOrder(), '|' + x.getPickup(), '|' + x.getReturn() + '|'))                       
            print(' --------------------------------------------------------------------------------------------- ')
    

    def findOrder(self):
        inp = int(input('Search by\n1. Car plate\n2. Customer SSN\n3. Date of order\n'))
        os.system('cls' if os.name == 'nt' else 'clear')
        oList = []
        if inp == 1:
            oList = self.__dom.findOrdersByCarPlate(str(input('Type in car plate number: ')))
        elif inp == 2:
             oList = self.__dom.findOrdersByCustomerSSN(str(input('Type in SSN: ')))
        elif inp == 3:
             oList = self.__dom.findOrdersByDate(str(input('Type in date of order: ')))
        else:
            print('Invalid input')

        self.printTable(oList)

        
