from Repositories.getorders import GetOrders
from Models.order import Order
from datetime import timedelta
from Models.cartype import CarType


class OrderDomain:


    def __init__(self):
        self.__orderRep = GetOrders()
        self.__orderList = self.__orderRep.orderData()
        self.__carTypes = CarType()

    
    def createOrder(self, orderData):
        self.__orderList.append(Order(orderData[0], orderData[1], orderData[2], orderData[3], 
                                orderData[4], orderData[5], orderData[6], orderData[7]))
                                
        self.__orderRep.orderInsert(self.__orderList)


    def calculateBasePrice(self, date1, date2, carType):
        time = timedelta()

        time = date2 - date1
        time = int(time.days)
        if time == 0:
            time = 1
        
        if carType == 1:
            return self.__carTypes.getSedanPrice() * time
        elif carType == 2:
            return self.__carTypes.getSportPrice() * time
        elif carType == 3:
            return self.__carTypes.getJeepPrice() * time
        else:
            print('Invalid input')