from Business.orderdomain import OrderDomain
from Business.customerdomain import CustomerDomain
from Business.cardomain import CarDomain
from Models.insurance import Insurance
from Repositories.getorders import GetOrders
from UI.customerui import CustomerUi
from datetime import datetime
import os


class OrderUi:


    def __init__(self):
        self.__dom = OrderDomain()
        self.__carDom = CarDomain()
        self.__customerDom = CustomerDomain()
        self.__customerUI = CustomerUi()


    def newOrder(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        newOrderData = []
        newOrderData.append(input('Customer SSN: '))
        # Checks if Customer exists, if not it calls create new customer
        if not self.__customerDom.checkSsn(newOrderData[0]):
            while not self.__customerUI.newCustomerWithSsn(newOrderData[0]):
                newOrderData[0] = input('Customer SSN: ')
                if self.__customerDom.checkSsn(newOrderData[0]):
                    break

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
            price += self.__dom.calculateBasePrice(pDate, rDate, 'sedan')
        elif typ == 2:
            car = self.__carDom.getNextAvailableCar('sport')
            self.__carDom.setAsUnavailable(car.getPlate())
            newOrderData.append(str(car.getPlate()))
            newOrderData.append('sport')
            price += self.__dom.calculateBasePrice(pDate, rDate, 'sport')
        elif typ == 3:
            car = self.__carDom.getNextAvailableCar('jeep')
            self.__carDom.setAsUnavailable(car.getPlate())
            newOrderData.append(str(car.getPlate()))
            newOrderData.append('jeep')
            price += self.__dom.calculateBasePrice(pDate, rDate, 'jeep')
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
        #self.__dom.createOrder(newOrderData)


        #Prints a table with the contents of orderList
    def printSelectionTable(self, myOrderList, index):
        print(' -------------------------------------------------------------------------------------------------- ')
        print('%-11s%-12s%-9s%-21s%-21s%-21s%-12s' % ('|' + 'SSN', '|' + 'Car Plate',
              '|' + 'Car Type', '|' + 'Date of Order', '|' + 'Pickup', '|' + 'Return' + '              |', 'Price' + '|'))
        print(' ================================================================================================== ')
        i = 0
        for x in myOrderList:
            if i == index:
                print('%-11s%-12s%-9s%-21s%-21s%-21s%-12s' % ('|' + x.getSsn(),
                                                         '|' + x.getCarPlate(),
                                                         '|' + x.getCarType(),
                                                         '|' + x.getDateOfOrder(),
                                                         '|' + x.getPickup(),
                                                         '|' + x.getReturn() + '|',
                str(self.__dom.calculateBasePrice(datetime.strptime(x.getPickup(),'%Y-%m-%d %H:%M:%S'),
                                                  datetime.strptime(x.getReturn(),'%Y-%m-%d %H:%M:%S'),
                                                  x.getCarType())) + '|' )
                      + '<---')
                print(' -------------------------------------------------------------------------------------------------- ')
            else:
                print('%-11s%-12s%-9s%-21s%-21s%-21s%-12s' % ('|' + x.getSsn(),
                                                         '|' + x.getCarPlate(),
                                                         '|' + x.getCarType(), '|' + x.getDateOfOrder(),
                                                         '|' + x.getPickup(), '|' + x.getReturn() + '|',
                str(self.__dom.calculateBasePrice(datetime.strptime(x.getPickup(), '%Y-%m-%d %H:%M:%S'),
                                                  datetime.strptime(x.getReturn(), '%Y-%m-%d %H:%M:%S'),
                                                  x.getCarType())) + '|'))
                print(' -------------------------------------------------------------------------------------------------- ')
            i += 1

    # Finds order by either Car plate, SSN or date the order was made.
    # Prints out all relevant orders
    def findOrder(self):
        inp = int(input('Search by\n1. Car plate\n2. Customer SSN\n3. Date of order\n'))
        os.system('cls' if os.name == 'nt' else 'clear')
        oList = []
        if inp == 1:
            oList = self.__dom.findOrdersByCarPlate(str(input('Type in car plate number: ')))
            return oList
        elif inp == 2:
             oList = self.__dom.findOrdersByCustomerSSN(str(input('Type in SSN: ')))
             return oList
        elif inp == 3:
             oList = self.__dom.findOrdersByDate(str(input('Type in date of order: ')))
             return oList
        else:
            print('Invalid input')


    def retOrders(self):
        return self.__dom.returnOrderData()


    def editReturn(self, order, returnDate):
        self.__dom.editReturnDate(order, returnDate)


    def editPickup(self, order, pickupDate):
        self.__dom.editPickupDate(order, pickupDate)


    def cancelOrder(self, plate, pDate):
        check = self.__dom.deleteOrder(plate, pDate)
        self.__carDom.setAsAvailable(plate) 
        if check == 1:
            print('Order Cancelled')
        else:
            print('Something went wrong')     
