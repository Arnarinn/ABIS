from .formatdata import formatData
import csv
from Models.order import Order


class GetOrders:
    def orderData(self):
        # Makes a ordersObjectArray which makes an empty array
        # and then it creates an object of the relevant type and inputs
        # it into the array and returns it.
        formattedData = formatData(open('../data/orders.csv'))
        ordersObjectArray = []
        for line in formattedData:
            ordersObjectArray.append(Order(line[0], line[1], line[2], line[3], line[4],
                                            line[5], line[6], line[7]))
        return ordersObjectArray

    # APPENDS the DATA for one new order to the customers.csv
    def orderInsert(self, order):
        with open('../data/orders.csv', 'a', newline = '') as orderFile:
            orderFileWriter = csv.writer(orderFile)
            orderFileWriter.writerow(order)
