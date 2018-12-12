import datetime
import os
from .customerui import CustomerUi
from .orderui import OrderUi
from .carui import CarUi


class CSUI:
    def __init__(self, domain):
        self.domain = domain
        self.carui = CarUi()
        self.customerui = CustomerUi()
        self.orderui = OrderUi()

    def home(self):
        while True:
            os.system('cls')
            print('Welcome to the ABIS manager program!')
            print('___________________________________')
            print('1. New order \n'
                  '2. View/edit orders \n'
                  '3. View cars \n'
                  '4. New customer \n'
                  '5. View/edit customers \n'
                  'q. Quit the program \n')
            # Detects a button press and which button was pressed
            c = input()
            # OPTION 1 SUB 1
            if c == '1':
                print('out of order')

            # OPTION 2 SUB 1
            elif c == '2':
                print('out of order')

            # OPTION 3 SUB 1
            elif c == '3':
                while True:
                    os.system('cls')
                    print('1. show available cars')
                    print('2. show unavailable cars')
                    print('q. back')
                    c2 = input()
                    # OPTION 1 SUB 2
                    if c2 == '1':
                        self.carui.CSDispAvailableCars()
                        input()
                        # OPTION 2 SUB 2
                    if c2 == '2':
                        self.carui.CSDispUnavailableCars()
                        input()
                    if c2 == 'q':
                        break

            # OPTION 4 SUB 1
            elif c == '4':
                self.customerui.newCustomer()

            # OPTION 5 SUB 1
            elif c == '5':
                while True:
                    os.system('cls')
                    print('1. See all customers')
                    print('2. Find specific customer')
                    print('q. back')
                    c2 = input()

                    # OPTION 1 SUB 2
                    if c2 == '1':
                        index = 0
                        while True:
                            os.system('cls')
                            customers = self.customerui.retCustomers()
                            self.customerui.printSelectionTable(customers, index)
                            print('1. Edit SSN')
                            print('2. Edit first name')
                            print('3. Edit last name')
                            print('4. Edit phone name')
                            print('5. Edit card number')
                            print('6. Delete customer')
                            print('q. back')
                            print('input W or S to move the arrow up and down')

                            c3 = input()
                            # OPTION 1 SUB 3
                            if c3 == '1':
                                ssn = input('SSN:')
                                self.customerui.editSsn(customers[index], ssn)

                            # OPTION 2 SUB 3
                            elif c3 == '2':
                                firstname = input('First name:')
                                self.customerui.editfName(customers[index], firstname)

                            # OPTION 3 SUB 3
                            elif c3 == '3':
                                lastname = input('Last name:')
                                self.customerui.editlName(customers[index], lastname)

                            # OPTION 4 SUB 3
                            elif c3 == '4':
                                phone = input('Phone:')
                                self.customerui.editPhone(customers[index], phone)

                            # OPTION 5 SUB 3
                            elif c3 == '5':
                                cardnumber = input('Card number:')
                                self.customerui.editCardNumber(customers[index], cardnumber)

                            # OPTION 6 SUB 3
                            elif c3 == '6':
                                self.customerui.deleteCustomer(customers[index])

                            # OPTION W SUB 3
                            elif c3.upper() == 'W' and index > 0:
                                os.system('cls')
                                index -= 1

                            # OPTION S SUB 3
                            elif c3.upper() == 'S' and index < len(customers)-1:
                                os.system('cls')
                                index += 1

                            # OPTION Q SUB 3
                            elif c3.upper() == 'Q':
                                break

                    # OPTION 2 SUB 2
                    elif c2 == '2':
                        # Make and index for the arrow functionality and going through a list
                        index = 0
                        customers = self.customerui.findCustomer()
                        while customers:
                            os.system('cls')
                            # makes a list of customers that fit specification
                            self.customerui.printSelectionTable(customers, index)
                            print('1. Edit SSN')
                            print('2. Edit first name')
                            print('3. Edit last name')
                            print('4. Edit phone name')
                            print('5. Edit card number')
                            print('6. Delete customer')
                            print('q. back')
                            print('input W or S to move the arrow up and down')

                            c3 = input()
                            # OPTION 1 SUB 3
                            if c3 == '1':
                                ssn = input('SSN:')
                                self.customerui.editSsn(customers[index], ssn)

                            # OPTION 2 SUB 3
                            elif c3 == '2':
                                firstname = input('First name:')
                                self.customerui.editfName(customers[index], firstname)

                            # OPTION 3 SUB 3
                            elif c3 == '3':
                                lastname = input('Last name:')
                                self.customerui.editlName(customers[index], lastname)

                            # OPTION 4 SUB 3
                            elif c3 == '4':
                                phone = input('Phone:')
                                self.customerui.editPhone(customers[index], phone)

                            # OPTION 5 SUB 3
                            elif c3 == '5':
                                cardnumber = input('Card number:')
                                self.customerui.editCardNumber(customers[index], cardnumber)

                            # OPTION 6 SUB 3
                            elif c3 == '6':
                                self.customerui.deleteCustomer(customers[index])

                            # OPTION W SUB 3
                            elif c3.upper() == 'W':
                                os.system('cls')
                                index -= 1

                            # OPTION S SUB 3
                            elif c3.upper() == 'W' and index > 0:
                                os.system('cls')
                                index -= 1

                            # OPTION S SUB 3
                            elif c3.upper() == 'S' and index < len(customers)-1:
                                os.system('cls')
                                index += 1

                            # OPTION Q SUB 3
                            elif c3.upper() == 'Q':
                                break

                    # OPTION Q SUB 2
                    elif c2 == 'q':
                        break

                    # OPTION REST SUB 2
                    else:
                        os.system('cls')
                        print(c2 + ' is not a valid command')

            # OPTION Q SUB 1
            elif c == 'q':
                os.system('cls')
                break

            # OPTION REST SUB 1
            else:
                os.system('cls')
                print(c + ' is not a valid command')
