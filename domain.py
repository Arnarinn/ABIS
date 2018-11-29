from data import GetData


class Domain:
    def __init__(self):
        self.data = GetData()

    def getCustomerData(self):
        return self.data.customerData()

    def getCarData(self):
        return self.data.carData()

    def getOrderData(self):
        return self.data.orderData()
