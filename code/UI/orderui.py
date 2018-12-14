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


    def getDateInput(self):
        trueVal = True

        while trueVal:
            yy = str(input('YYYY: '))
            if yy.isdigit() and len(yy) == 4:
                yy = int(yy)
                trueVal = False
            else:
                print('Year not valid.\nExample: 2018')

        while not trueVal:
            mm = str(input('MM: '))
            if mm.isdigit() and len(mm) == 2:
                mm = int(mm)
                trueVal = True
            else:
                print('Month not valid.\nFor example: December is 12')

        while trueVal:
            dd = str(input('DD: '))
            if dd.isdigit() and len(dd) == 2:
                dd = int(dd)
                trueVal = False
            else:
                print('Day not valid.')

        return datetime(yy, mm, dd)


    def newOrder(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        # Truth value used for input error handling
        trueVal = True

        # List that gathers the info required to create an instance of order
        newOrderData = []

        newOrderData.append(input('Customer SSN: '))

        # Checks if Customer exists, if not it calls create new customer
        if not self.__customerDom.checkSsn(newOrderData[0]):
            while not self.__customerUI.newCustomerWithSsn(newOrderData[0]):
                newOrderData[0] = input('Customer SSN: ')
                if self.__customerDom.checkSsn(newOrderData[0]):
                    break

        # Gets the date / time today.
        newOrderData.append(datetime(int(datetime.today().year), \
                                     int(datetime.today().month), \
                                     int(datetime.today().day), \
                                     int(datetime.today().hour), \
                                     int(datetime.today().minute), \
                                     int(datetime.today().second)))
        
        os.system('cls' if os.name == 'nt' else 'clear')

        # Asks for a pickup date from the user and validates it
        while trueVal:    
            print('Pickup Date (YYYY/MM/DD): ')
            pDate = self.getDateInput()
            tDay = datetime(int(datetime.today().year), \
                            int(datetime.today().month), \
                            int(datetime.today().day))
            if pDate >= tDay:
                trueVal = False
            else:
                print('Pickup date not valid')
                input()
                os.system('cls' if os.name == 'nt' else 'clear')

        newOrderData.append(pDate)
        trueVal = True


        os.system('cls' if os.name == 'nt' else 'clear')

        # Asks for a return date from the user and validates it
        while trueVal:
            print('Return Date (YYYY/MM/DD: ')
            rDate = self.getDateInput()
            if rDate > pDate:
                trueVal = False
            else:
                print('Return date not valid')
                input()
                os.system('cls' if os.name == 'nt' else 'clear')

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
        self.__dom.createOrder(newOrderData)


    #Prints a table with the contents of orderList
    def printSelectionTable(self, myOrderList, index):
        print(' --------------------------------------------------------------------------------------------------- ')
        print('%-11s%-12s%-9s%-21s%-21s%-21s%-12s' % ('|' + 'SSN', '|' + 'Car Plate',
              '|' + 'Car Type', '|' + 'Date of Order', '|' + 'Pickup', '|' + 'Return' + '             |', 'Price' + '|'))
        print(' =================================================================================================== ')
        i = 0
        for x in myOrderList:
            if i == index:
                print('%-11s%-12s%-9s%-21s%-21s%-21s%-12s' % ('|' + x.getSsn(),
                                                         '|' + x.getCarPlate(),
                                                         '|' + x.getCarType(),
                                                         '|' + str(x.getDateOfOrder()),
                                                         '|' + str(x.getPickup()),
                                                         '|' + str(x.getReturn()) + '|',
                str(self.__dom.calculateBasePrice(datetime.strptime(str(x.getPickup()),'%Y-%m-%d %H:%M:%S'),
                                                  datetime.strptime(str(x.getReturn()),'%Y-%m-%d %H:%M:%S'),
                                                  x.getCarType())) + '|' )
                      + '<---')
                print(' --------------------------------------------------------------------------------------------------- ')
            else:
                print('%-11s%-12s%-9s%-21s%-21s%-21s%-12s' % ('|' + x.getSsn(),
                                                         '|' + x.getCarPlate(),
                                                         '|' + x.getCarType(), '|' + str(x.getDateOfOrder()),
                                                         '|' + str(x.getPickup()), '|' + str(x.getReturn()) + '|',
                str(self.__dom.calculateBasePrice(datetime.strptime(str(x.getPickup()), '%Y-%m-%d %H:%M:%S'),
                                                  datetime.strptime(str(x.getReturn()), '%Y-%m-%d %H:%M:%S'),
                                                  x.getCarType())) + '|'))
                print(' --------------------------------------------------------------------------------------------------- ')
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
        pDate = datetime.strptime(order.getPickup(), '%Y-%m-%d %H:%M:%S')
        if pDate >= returnDate:
            print('Invalid return date')
            input()
            return
        self.__dom.editReturnDate(order, returnDate)


    def editPickup(self, order, pickupDate):
        rDate = datetime.strptime(order.getReturn(), '%Y-%m-%d %H:%M:%S')
        tDay = datetime(int(datetime.today().year), \
                            int(datetime.today().month), \
                            int(datetime.today().day))
        if tDay > pickupDate or rDate <= pickupDate:
            print('Invalid pickup date')
            input()
            return
        self.__dom.editPickupDate(order, pickupDate)


    def cancelOrder(self, plate, pDate):
        check = self.__dom.deleteOrder(str(plate), str(pDate))
        self.__carDom.setAsAvailable(plate) 
        if check == 1:
            print('Order Cancelled')
        else:
            print('Something went wrong')     
