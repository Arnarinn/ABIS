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


    # Returns the customer with matching ssn.
    def findCustomerSSN(self, ssn):
        for x in self.__customerList:
            if x.getSsn() == ssn:
                return x

    
    # Returns the customer with matching phone.
    def findCustomerPhone(self, phone):
        for x in self.__customerList:
            if x.getPhone() == phone:
                return x


    # Returns a list of customers with matching names.
    def findCustomerName(self, fname, lname):
        listOfCustomers = []
        for x in self.__customerList:
            if x.getFName() == fname and x.getLName() == lname:
                listOfCustomers.append(x)
        return listOfCustomers

    def returnCustomerData(self):
        return self.__customerList
    



