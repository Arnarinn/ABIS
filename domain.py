import data


class Domain:
    def getCustomerData(self):
        return data.GetCustomers().customerData()

    def getCarData(self):
        return data.GetCars().carData()

    def getOrderData(self):
        return data.GetOrders().orderData()

    def insertCustomer(self, ssn, name, age):
        customer = data.Customer(ssn, name, age)
        data.GetCustomers.customerInsert(customer)

    def insertOrder(self, employee, timeOfOrder, timeOfPickup, timeOfReturn, carNumber):
        order = data.Order(employee, timeOfOrder, timeOfPickup, timeOfReturn, carNumber)
        data.GetOrders.orderInsert(order)

    def checkLogin(self, username, password):
        employeeData = data.GetEmployees().emplyeeData()
        for e in employeeData:
            if e[0] == username:
                if e[1] == password:
                    return True
        return False
