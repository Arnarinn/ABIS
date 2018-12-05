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

    def getEmployeeData(self):
        return GetEmployees().employeeData()

    def insertCustomer(self, ssn, name, age):
        getCustomers = GetCustomers()
        customer = Customer(ssn, name, age)
        getCustomers.customerInsert(customer)

    def insertOrder(self, employee, timeOfOrder, timeOfPickup, timeOfReturn, carNumber):
        getOrders = GetOrders()
        order = Order(employee, timeOfOrder, timeOfPickup, timeOfReturn, carNumber)
        getOrders.orderInsert(order)
