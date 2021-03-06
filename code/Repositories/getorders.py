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

    # WRITES the DATA from the orderlist into the csv file
    def orderInsert(self, orderList):
        with open('../data/orders.csv', 'w', newline = '') as orderFile:
            orderFileWriter = csv.writer(orderFile)
            # This is the headder
            orderFileWriter.writerow(['client', 'date of order', 'date of pickup',\
                                         'date of return', 'license plate', 'car type',\
                                         'insurance', 'cost'])
            for obj in orderList:
                orderFileWriter.writerow(obj.dataList())