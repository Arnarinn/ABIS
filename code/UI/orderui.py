from Business.orderdomain import OrderDomain
from Business.cardomain import CarDomain
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
        newOrderData.append(datetime(yy, mm, dd))

        print('Return Date (YYYY/MM/DD: ')
        yy = int(input('YYYY: '))
        mm = int(input('MM: '))
        dd = int(input('DD: '))
        newOrderData.append(datetime(yy, mm, dd))

        typ = int(input('Car type:\n1. Sedan\n2. Sport\n3. Jeep\n'))
        

        




        newOrderData.append(input('Car License plate: '))






        newOrderData.append(input('Car type: '))
        newOrderData.append(input('Insurance lvl: '))
        newOrderData.append(input('Price: '))
        self.__dom.createOrder(newOrderData)