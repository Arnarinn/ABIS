from Repositories.getcustomers import GetCustomers


class CustomerDomain:


    def __init__(self):
        self.__customerRep = GetCustomers()
        self.__customerList = self.__customerRep.customerData()


    # Calls the customerInsert function from domain
    # Then reloads the customer list
    def createCustomer(self, customer):
        self.__customerRep.customerInsert(customer)
        self.__customerList = []
        self.__customerList = self.__customerRep.customerData()
