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
                  '2. View orders \n'
                  '3. View cars \n'
                  '4. New customer \n'
                  '5. View customers \n'
                  'q. Quit the program \n')
            # Detects a button press and which button was pressed
            c = input()
            if c == '1':
                self.newOrders()
            elif c == '2':
                self.viewOrders()
            elif c == '3':
                while True:
                    os.system('cls')
                    print('1. show available cars')
                    print('2. show unavailable cars')
                    print('q. go backwards')
                    c2 = input()
                    if c2 == '1':
                        self.carui.CSDispAvailableCars()
                        input()
                    if c2 == '2':
                        self.carui.CSDispUnavailableCars()
                        input()
                    if c2 == 'q':
                        break

            elif c == b'4':
                self.customerui.newCustomer()
            elif c == b'5':
                while True:
                    os.system('cls')
                    print('1. See all customers')
                    print('2. Find specific customer')
                    print('q. go backwards')
                    c2 = input()
                    if c2 == '1':
                        os.system('cls')
                        self.customerui.dispCustomers()
                        input()
                    elif c2 == '2':
                        os.system('cls')
                        self.customerui.findCustomer()
                        input()
                    elif c2 == 'q':
                        break
            elif c == 'q':
                os.system('cls')
                break
    def newOrders(self):
        os.system('cls')
        # loads of inputs to insert into the csv file
        employee = input('Type in employee name:')
        timeOfPickUp = input('Type in time of pick up:')
        timeOfReturn = input('Type in time of return:')
        carNumber = input('Type in car number:')
        # sends the info to the business layer
        # which inserts it into the relevant file
        self.domain.insertOrder(employee, str(datetime.datetime.now())
                                , timeOfPickUp, timeOfReturn, carNumber)
        # Waits for any input on the keyboard
        # to give time for user to read their info
        print('press any key to go back')
        input()

    def viewOrders(self):
        os.system('cls')
        orderData = self.domain.getOrderData()
        for v in orderData:
            print(v.__str__())
        # Waits for any input on the keyboard
        # to give time for user to read their info
        print('press any key to go back')
        input()

    def newCustomer(self):
        print('not yet implemented')
        input()
        os.system('cls')

    def viewCustomer(self):
        os.system('cls')
        customerData = self.domain.getCustomerData()
        for v in customerData:
            print(v.__str__())
        # Waits for any input on the keyboard
        # to give time for user to read their info
        print('press any key to go back')
        input()
