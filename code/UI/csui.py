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
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Welcome to the ABIS, the Customer Service program!')
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
                print('out of order')
            elif c == '2':
                print('out of order')
            elif c == '3':
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('1. show available cars')
                    print('2. show unavailable cars')
                    print('q. back')
                    c2 = input()
                    if c2 == '1':
                        self.carui.CSDispAvailableCars()
                        input()
                    if c2 == '2':
                        self.carui.CSDispUnavailableCars()
                        input()
                    if c2 == 'q':
                        break

            elif c == '4':
                self.customerui.newCustomer()
            elif c == '5':
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('1. See all customers')
                    print('2. Find specific customer')
                    print('q. back')
                    c2 = input()
                    if c2 == '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.customerui.dispCustomers()
                        input()
                    elif c2 == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.customerui.findCustomer()
                        print('1. Edit SSN')
                        print('2. Edit first name')
                        print('2. Edit last name')
                        print('2. Edit phone name')
                        print('2. Edit first name')

                        input()
                    elif c2 == 'q':
                        break
            elif c == 'q':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
