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

    
    def deleteOrder(self, carPlate, pDate):
        for x in self.__orderList:
            if x.getCarPlate() == carPlate and x.getPickup()[:10] == pDate:
                self.__orderList.remove(x)
                self.__orderRep.orderInsert(self.__orderList)
                return 1
        return 0
            


    def calculateBasePrice(self, date1, date2, carType):
        time = timedelta()

        time = date2 - date1
        time = int(time.days)
        if time == 0:
            time = 1
        
        if carType == 'sedan':
            return self.__carTypes.getSedanPrice() * time
        elif carType == 'sport':
            return self.__carTypes.getSportPrice() * time
        elif carType == 'jeep':
            return self.__carTypes.getJeepPrice() * time
        else:
            print('Invalid input')


    def findOrdersByCarPlate(self, plate):
        oList = []
        for order in self.__orderList:
            if str(plate) in str(order.getCarPlate()):
                oList.append(order)
        return oList


    
    def findOrdersByCustomerSSN(self, ssn):
        oList = []
        for order in self.__orderList:
            if str(ssn) in str(order.getSsn()):
                oList.append(order)
        return oList

    
    def findOrdersByDate(self, date):
        oList = []
        for order in self.__orderList:
            if str(order.getDateOfOrder())[:10] == str(date):
                oList.append(order)
        return oList

    def returnOrderData(self):
        return self.__orderList

    def editReturnDate(self, order, returnDate):
        for e in self.__orderList:
            if order.getCarPlate() == e.getCarPlate() and order.getPickup() == e.getPickup():
                e.setReturn(returnDate)
                self.__orderRep.orderInsert(self.__orderList)

    def editPickupDate(self, order, pickupDate):
        for e in self.__orderList:
            if order.getCarPlate() == e.getCarPlate() and order.getPickup() == e.getPickup():
                e.setPickup(pickupDate)
                self.__orderRep.orderInsert(self.__orderList)
