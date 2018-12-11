import msvcrt
import os
from Business.customerdomain import CustomerDomain
from Models.customer import Customer


class CustomerUi:


    def __init__(self):

        self.__dom = CustomerDomain()
    

    def newCustomer(self):
        # appends customer info from user, into a list.
        ssn = input('SSN: ')
        fn = input('First Name: ')
        ln = input('Last Name: ')
        age = input('Age: ')
        pho = input('Phone: ')
        oth = input('Other: ')
        newCustomerData = Customer(ssn, fn, ln, age, pho, oth)
        # Calls the Business function createCustomer with that data.
        self.__dom.createCustomer(newCustomerData)

    
    #Prints a table with the contents of myCustomerList
    def printTable(self, myCustomerList):                                                 
        print(' ------------------------------------------------- ')
        #Table has 4 colums with size: 11, 15, 15, 10 respectively
        # columns are filled with strings
        # columns are aligned to the left                  
        print('%-11s%-15s%-15s%-10s' % ('|' + 'SSN', '|' + 'Last Name', \
            '|' + 'First Name', '|' + 'Phone   ' + '|'))                               
        print(' ================================================= ')                  
        for x in myCustomerList:                                                          
            print('%-11s%-15s%-15s%-10s' % ('|' + x.getSsn(),\
                 '|' + x.getLName(),\
                 '|' + x.getFName(), '|' + x.getPhone() + ' |'))                       
            print(' ------------------------------------------------- ')

    def findCustomer(self):
        while True:
            print('1. Search by SSN\n2. Search by Phone\n3. Search by Full Name\nq. Go backwards')
            listOfCustomers = []
            inp = msvcrt.getch()

            if inp == b'1':
                listOfCustomers.append(self.__dom.findCustomerSSN(str(input('SSN: '))))
                os.system('cls')
            elif inp == b'2':
                listOfCustomers.append(self.__dom.findCustomerPhone(str(input('Phone: '))))
                os.system('cls')
            elif inp == b'3':
                listOfCustomers.append(self.__dom.findCustomerName(str(input('First Name: ')),
                                         str(input('Last Name: '))))
                os.system('cls')
            elif inp == b'q':
                break

            self.printTable(listOfCustomers)

    def dispCustomers(self):
        self.printTable(self.__dom.returnCustomerData())
