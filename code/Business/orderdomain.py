from Repositories.getorders import GetOrders
from Models.order import Order


class OrderDomain:

    def __init__(self):
        self.__orderRep = GetOrders()
        self.__orderList = self.__orderRep.orderData()

    def createOrder(self, client, dateOfOrder, dateOfPickup, dateOfReturn, licensePlate, carType, insurance, cost):
        orderData = Order(client, dateOfOrder, dateOfPickup, dateOfReturn, licensePlate, carType, insurance, cost)
        self.__orderRep.orderInsert(orderData)
        self.__orderList = []
        self.__orderList = self.__orderRep.orderData()
        print(self.__orderList)

