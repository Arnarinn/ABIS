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

        inp = input('1. Search by SSN\n2. Search by Phone\n3. Search by Full Name\n')
        listOfCustomers = []

        if inp == '1':
            listOfCustomers.append(self.__dom.findCustomerSSN(str(input('SSN: '))))
        elif inp == '2':
            listOfCustomers.append(self.__dom.findCustomerPhone(str(input('Phone: '))))
        elif inp == '3':
            listOfCustomers.append(self.__dom.findCustomerName(str(input('First Name: ')),
                                     str(input('Last Name: '))))
        else:
            print('Invalid Input')

        self.printTable(listOfCustomers)