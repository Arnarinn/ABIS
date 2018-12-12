import os
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
        newCustomerData.append(input('Credit Card: '))
        # Calls the Business function createCustomer with that data.
        self.__dom.createCustomer(newCustomerData)

    
    #Prints a table with the contents of myCustomerList
    def printSelectionTable(self, myCustomerList, index):
        print(' -------------------------------------------------------------- ')
        #Table has 4 colums with size: 11, 15, 15, 10 respectively
        # columns are filled with strings
        # columns are aligned to the left                  
        print('%-11s%-15s%-11s%-8s%-20s' % ('|' + 'SSN', '|' + 'Last Name',
              '|' + 'First Name', '|' + 'Phone   ' + '|', 'Card number      ' + '|'))
        print(' ============================================================== ')
        i = 0
        for x in myCustomerList:
            if index == i:
                print('%-11s%-15s%-11s%-8s%-20s' % ('|' + x.getSsn(),
                      '|' + x.getLName(),'|' + x.getFName(),
                      '|' + x.getPhone() + ' |', x.getCardNumber() + ' |') + '<---')
                print(' -------------------------------------------------------------- ')
            else:
                print('%-11s%-15s%-11s%-8s%-20s' % ('|' + x.getSsn(),
                      '|' + x.getLName(), '|' + x.getFName(),
                      '|' + x.getPhone() + ' |', x.getCardNumber() + ' |'))
                print(' -------------------------------------------------------------- ')
            i += 1


    def findCustomer(self):
        while True:
            print('1. Search by SSN\n2. Search by Phone\n3. Search by Full Name\nq. Go backwards')
            listOfCustomers = []
            inp = input()

            if inp == '1':
                listOfCustomers.append(self.__dom.findCustomerSSN(str(input('SSN: '))))
                os.system('cls')
                return listOfCustomers
            elif inp == '2':
                listOfCustomers.append(self.__dom.findCustomerPhone(str(input('Phone: '))))
                os.system('cls')
                return listOfCustomers
            elif inp == '3':
                listOfCustomers.append(self.__dom.findCustomerName(str(input('First Name: ')),
                                         str(input('Last Name: '))))
                os.system('cls')
                return listOfCustomers
            elif inp == 'q':
                break


    def retCustomers(self):
        return self.__dom.returnCustomerData()


    def editSsn(self, customer, ssn):
        self.__dom.editSsn(customer, ssn)

    def editlName(self, customer, lname):
        self.__dom.editlName(customer, lname)

    def editfName(self, customer, fname):
        self.__dom.editfName(customer, fname)

    def editPhone(self, customer, phone):
        self.__dom.editPhone(customer, phone)

    def editCardNumber(self, customer, cardnumber):
        self.__dom.editCardNumber(customer, cardnumber)

    def deleteCustomer(self, customer):
        self.__dom.deleteCustomer(customer)
