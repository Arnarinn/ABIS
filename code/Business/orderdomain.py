from Repositories.getorders import GetOrders


class OrderDomain:

    def __init__(self):
        self.__orderRep = GetOrders()
        self.__orderList = self.__orderRep.orderData()

    def createOrder(self, orderData):
        self.__orderRep.orderInsert(orderData)
        self.__orderList = []
        self.__orderList = self.__orderRep.orderData()
        print(self.__orderList)

