import data

class Domain:
    def getCustomerData(self):
        return data.GetCustomers().customerData()

    def getCarData(self):
        return data.GetCars().carData()

    def getOrderData(self):
        return data.GetOrders().orderData()

    def insertCustomer(self, name, age):
        data.GetCustomers.customerInsert(name, age)

    def insertOrder(self, employee, timeOfOrder, timeOfPickUp, timeOfReturn, carNumber):
        data.GetOrders.orderInsert(employee, timeOfOrder, timeOfPickUp, timeOfReturn, carNumber)

    def checkLogin(self, username, password):
        employeeData = data.GetEmployees().emplyeeData()
        for e in employeeData:
            if e[0] == username:
                if e[1] == password:
                    return True
        return False
