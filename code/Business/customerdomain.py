from Repositories.getcustomers import GetCustomers
from Models.customer import Customer


class CustomerDomain:
    def __init__(self):
        self.__customerRep = GetCustomers()
        self.__customerList = self.__customerRep.customerData()


    # Calls the customerInsert function from domain
    # Then reloads the customer list
    def createCustomer(self, customerData):
        self.__customerList.append(Customer(customerData[0], customerData[1],
                                            customerData[2], customerData[3],
                                            customerData[4], customerData[5]))
        self.__customerRep.customerInsert(self.__customerList)


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


    def editSsn(self, customer, ssn):
        for e in self.__customerList:
            if e.getSsn() == customer.getSsn():
                e.setSsn(ssn)
                self.__customerRep.customerInsert(self.__customerList)


    def editlName(self, customer, lname):
        for e in self.__customerList:
            if e.getSsn() == customer.getSsn():
                e.setlName(lname)
                self.__customerRep.customerInsert(self.__customerList)


    def editfName(self, customer, fname):
        for e in self.__customerList:
            if e.getSsn() == customer.getSsn():
                e.setfName(fname)
                self.__customerRep.customerInsert(self.__customerList)


    def editPhone(self, customer, phone):
        for e in self.__customerList:
            if e.getSsn() == customer.getSsn():
                e.setPhone(phone)
                self.__customerRep.customerInsert(self.__customerList)


    def editCardNumber(self, customer, cardnumber):
        for e in self.__customerList:
            if e.getSsn() == customer.getSsn():
                e.setCardNumber(cardnumber)
                self.__customerRep.customerInsert(self.__customerList)


    def deleteCustomer(self, customer):
        for e in self.__customerList:
            if e.getSsn() == customer.getSsn():
                self.__customerList.remove(e)
                self.__customerRep.customerInsert(self.__customerList)


    def checkSsn(self, SSN):
        for x in self.__customerList:
            if x.getSsn() == SSN:
                return True
        return False


