from .formatdata import formatData
from Models.order import Order

class GetOrders:
    def orderData(self):
        # Makes a ordersObjectArray which makes an empty array
        # and then it creates an object of the relevant type and inputs
        # it into the array and returns it.
        formattedData = formatData(open('../data/orders.csv'))
        ordersObjectArray = []
        for line in formattedData:
            ordersObjectArray.append(Order(line[0], line[1], line[2], line[3], line[4]))
        return ordersObjectArray

    def orderInsert(self, order):
        with open('../data/orders.csv', 'a+') as orderFile:
            orderFile.write(order.__repr__() + '\n')
