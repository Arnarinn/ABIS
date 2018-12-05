from Repositories.getcars import GetCars
from Repositories.getemployees import GetEmployees
from Repositories.getorders import GetOrders
from Repositories.getcustomers import GetCustomers
from Models.customer import Customer
from Models.order import Order


class Domain:
    def getCustomerData(self):
        return GetCustomers().customerData()

    def getCarData(self):
        return GetCars().carData()

    def getOrderData(self):
        return GetOrders().orderData()

    def insertCustomer(self, ssn, name, age):
        getCustomers = GetCustomers()
        customer = Customer(ssn, name, age)
        getCustomers.customerInsert(customer)

    def insertOrder(self, employee, timeOfOrder, timeOfPickup, timeOfReturn, carNumber):
        getOrders = GetOrders()
        order = Order(employee, timeOfOrder, timeOfPickup, timeOfReturn, carNumber)
        getOrders.orderInsert(order)

    def checkLogin(self, username, password):
        employeeData = GetEmployees().emplyeeData()
        for e in employeeData:
            if e[0] == username:
                if e[1] == password:
                    return True
        return False
