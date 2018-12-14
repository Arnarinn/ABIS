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
        if (not newCustomerData[0].isdigit()) or (len(newCustomerData[0]) != 10):
            print('SSN not valid')
            return
        if self.__dom.checkSsn(newCustomerData[0]):
            print('This SSN has already been recorded')
            input()
            return

        newCustomerData.append(input('First Name: '))
        if not newCustomerData[1].isalpha():
            print('First name not valid')
            return

        newCustomerData.append(input('Last Name: '))
        if not newCustomerData[2].isalpha():
            print('Last name not valid')
            return

        newCustomerData.append(input('Age: '))
        if (not newCustomerData[3].isdigit()) or (int(newCustomerData[3]) < 20):
            print('Age not valid')
            return

        newCustomerData.append(input('Phone: '))
        if (not newCustomerData[4].isdigit()) or (len(newCustomerData[4]) != 7):
            print('Phone not valid')
            return
        if self.__dom.checkPhone(newCustomerData[4]):
            print('This phone has already been recorded')
            input()
            return
        newCustomerData.append(input('Credit Card: '))
        if (not newCustomerData[5].isdigit()) or (len(newCustomerData[5]) != 16):
            print('Credit Card not valid')
            return

        # Calls the Business function createCustomer with that data.
        self.__dom.createCustomer(newCustomerData)


        # Creates new customer with ssn already filled out
    def newCustomerWithSsn(self, SSN):
        # appends customer info from user, into a list.
        newCustomerData = []

        newCustomerData.append(SSN)
        if (not newCustomerData[0].isdigit()) or (len(newCustomerData[0]) != 10):
            print('SSN not valid')
            return False
        if self.__dom.checkSsn(newCustomerData[0]):
            print('This SSN has already been recorded')
            return False

        newCustomerData.append(input('First Name: '))
        if not newCustomerData[1].isalpha():
            print('First name not valid')
            return False

        newCustomerData.append(input('Last Name: '))
        if not newCustomerData[2].isalpha():
            print('Last name not valid')
            return False

        newCustomerData.append(input('Age: '))
        if (not newCustomerData[3].isdigit()) or (int(newCustomerData[3]) < 20):
            print('Age not valid')
            return False

        newCustomerData.append(input('Phone: '))
        if (not newCustomerData[4].isdigit()) or (len(newCustomerData[4]) != 7):
            print('Phone not valid')
            return False
        if self.__dom.checkPhone(newCustomerData[4]):
            print('This Phone has already been recorded')
            return False
        newCustomerData.append(input('Credit Card: '))
        if (not newCustomerData[5].isdigit()) or (len(newCustomerData[5]) != 16):
            print('Credit Card not valid')
            return False

        # Calls the Business function createCustomer with that data.
        self.__dom.createCustomer(newCustomerData)

        return True

    
    #Prints a table with the contents of myCustomerList
    def printSelectionTable(self, myCustomerList, index):
        print(' -------------------------------------------------------------- ')               
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
            print('1. Search by SSN\n2. Search by Phone\n3. Search by Full Name\nq. Go back')
            listOfCustomers = []
            inp = input()

            if inp == '1':
                listOfCustomers.append(self.__dom.findCustomerSSN(str(input('SSN: '))))
                os.system('cls' if os.name == 'nt' else 'clear')
                return listOfCustomers
            elif inp == '2':
                listOfCustomers.append(self.__dom.findCustomerPhone(str(input('Phone: '))))
                os.system('cls' if os.name == 'nt' else 'clear')
                return listOfCustomers

            elif inp == '3':
                listOfCustomers = self.__dom.findCustomerName(str(input('First Name: ')),
                                         str(input('Last Name: ')))
                os.system('cls' if os.name == 'nt' else 'clear')
                return listOfCustomers

            elif inp == 'q':
                break


    def retCustomers(self):
        return self.__dom.returnCustomerData()


    def editSsn(self, customer, ssn):
        if (not ssn.isdigit()) or (len(ssn) != 10):
            print('SSN not valid')
            input()
            return
        if self.__dom.checkSsn(ssn):
            print('This SSN has already been recorded')
            input()
            return
        self.__dom.editSsn(customer, ssn)

    def editlName(self, customer, lname):
        if not lname.isalpha():
            print('First name not valid')
            input()
            return
        self.__dom.editlName(customer, lname)

    def editfName(self, customer, fname):
        if not fname.isalpha():
            print('First name not valid')
            input()
            return
        self.__dom.editfName(customer, fname)

    def editPhone(self, customer, phone):
        if (not phone.isdigit()) or (len(phone) != 7):
            print('Phone not valid')
            input()
            return
        if self.__dom.checkPhone(phone):
            print('This phone has already been recorded')
            input()
            return
        self.__dom.editPhone(customer, phone)

    def editCardNumber(self, customer, cardnumber):
        if (not cardnumber.isdigit()) or (len(cardnumber) != 16):
            print('Credit Card not valid')
            input()
            return
        self.__dom.editCardNumber(customer, cardnumber)

    def deleteCustomer(self, customer):
        self.__dom.deleteCustomer(customer)
