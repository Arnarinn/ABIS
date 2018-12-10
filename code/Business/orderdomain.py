from Repositories.getorders import GetOrders
from Models.order import Order


class OrderDomain:


    def __init__(self):
        self.__orderRep = GetOrders()
        self.__orderList = self.__orderRep.orderData()

    
    def createOrder(self, orderData):
        self.__orderList.append(Order(orderData[0], orderData[1], orderData[2], orderData[3], 
                                orderData[4], orderData[5], orderData[6], orderData[7]))
                                
        self.__orderRep.orderInsert(self.__orderList)
