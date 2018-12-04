import data


class Domain:
    def getCustomerData(self):
        return data.GetCustomers().customerData()

    def getCarData(self):
        return data.GetCars().carData()

    def getOrderData(self):
        return data.GetOrders().orderData()

    def insertCustomer(self, ssn, name, age):
        getCustomers = data.GetCustomers()
        customer = data.Customer(ssn, name, age)
        getCustomers.customerInsert(customer)

    def insertOrder(self, employee, timeOfOrder, timeOfPickup, timeOfReturn, carNumber):
        getOrders = data.GetOrders()
        order = data.Order(employee, timeOfOrder, timeOfPickup, timeOfReturn, carNumber)
        getOrders.orderInsert(order)

    def checkLogin(self, username, password):
        employeeData = data.GetEmployees().emplyeeData()
        for e in employeeData:
            if e[0] == username:
                if e[1] == password:
                    return True
        return False
