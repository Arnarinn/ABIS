from Business.customerdomain import CustomerDomain
from Models.customer import Customer


class CustomerUi:


    def __init__(self):

        self.__dom = CustomerDomain()
    

    def newCustomer(self):
        # appends customer info from user, into a list.
        newCustomerData = []
        newCustomerData.append(input('SSN: '))
        newCustomerData.append(input('First Name: '))
        newCustomerData.append(input('Last Name: '))
        newCustomerData.append(input('Age: '))
        newCustomerData.append(input('Phone: '))
        newCustomerData.append(input('Other: '))
        # Calls the Business function createCustomer with that data.
        self.__dom.createCustomer(newCustomerData)