from Business.orderdomain import OrderDomain
from Business.cardomain import CarDomain
from Models.insurance import Insurance
from datetime import datetime
from datetime import timedelta


class OrderUi:


    def __init__(self):
        self.__dom = OrderDomain()
        self.__carDom = CarDomain()


    def newOrder(self):
        newOrderData = []
        newOrderData.append(input('Customer SSN: '))
        newOrderData.append(datetime(int(datetime.today().year), \
                                     int(datetime.today().month), \
                                     int(datetime.today().day), \
                                     int(datetime.today().hour), \
                                     int(datetime.today().minute), \
                                     int(datetime.today().second)))
        print('Pickup Date (YYYY/MM/DD): ')    
        yy = int(input('YYYY: '))
        mm = int(input('MM: '))
        dd = int(input('DD: '))
        pDate = datetime(yy, mm, dd)
        newOrderData.append(pDate)

        print('Return Date (YYYY/MM/DD: ')
        yy = int(input('YYYY: '))
        mm = int(input('MM: '))
        dd = int(input('DD: '))
        rDate = datetime(yy, mm, dd)
        newOrderData.append(rDate)

        diff = timedelta()

        diff = rDate - pDate

        diff = int(diff.days) 

        typ = int(input('Car type:\n1. Sedan\n2. Sport\n3. Jeep\n'))
        
        price = 0
        if typ == 1:
            newOrderData.append('sedan')
            car = self.__carDom.getNextAvailableCar('sedan')
            self.__carDom.setAsUnavailable(car.getPlate())
            newOrderData.append(str(car.getPlate()))
            price += 12000 * diff
        elif typ == 2:
            newOrderData.append('sport')
            car = self.__carDom.getNextAvailableCar('sport')
            self.__carDom.setAsUnavailable(car.getPlate())
            newOrderData.append(str(car.getPlate()))
            price += 19000 * diff
        elif typ == 3:
            newOrderData.append('jeep')
            car = self.__carDom.getNextAvailableCar('jeep')
            self.__carDom.setAsUnavailable(car.getPlate())
            newOrderData.append(str(car.getPlate()))
            price += 33000 * diff
        else:
            print('invalid input')

        ins = int(input('Insurance lvl:\n1. Lvl1\n2. Lvl2\n3.Lvl3\n'))
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