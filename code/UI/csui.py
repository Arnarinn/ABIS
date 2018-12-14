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

    # The main menu for Customer Service employees.
    def home(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            # The main menu:
            print('Welcome to ABIS, the Customer Service program!')
            print('___________________________________')
            print('1. New order \n'
                  '2. View/edit orders \n'
                  '3. View/edit cars \n'
                  '4. New customer \n'
                  '5. View/edit customers \n'
                  'q. Quit the program \n')
            # Detects a button press and which button was pressed
            c = input()

            # Checks input from user and calls a function from the menu
            if c == '1':
                self.orderui.newOrder()
            elif c == '2':
                self.orderOptions()                
            elif c == '3':
                self.carOptions()
            elif c == '4':
                self.customerui.newCustomer()
            elif c == '5':
                self.customerOptions()
            elif c.upper() == 'Q':
                os.system('cls' if os.name == 'nt' else 'clear')
                break


    # This contains the order options and is called from the home function
    def orderOptions(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            # The orders menu:
            print('1. View/edit all orders')
            print('2. find specific order')
            print('q. back')
            # Gets input from user
            c = input()
            # Checks input from user and calls a function from the orders menu
            if c == '1':
                self.viewAndEditAllOrders()
            if c == '2':
                self.findOrderAndEdit()
            if c.upper() == 'Q':
                break
    

    # Prints all orders in a table and gives the user options on editing them
    # This function is called from orderOptions
    def viewAndEditAllOrders(self):
        index = 0
        # Gets a list of orders from orderui
        orders = self.orderui.retOrders()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            # The edit / navigation menu
            self.orderui.printSelectionTable(orders, index)
            print('1. Edit pickup date')
            print('2. Edit return date')
            print('3. Delete order')
            print('q. back')
            print('input W or S to move the arrow up and down')
            # Gets input from user
            c = input()
            # Checks input from user and calls a function from the edit / navigation menu
            if c == '1':
                # Uses the same function as orderui to get date input
                pickDate = self.orderui.getDateInput()
                self.orderui.editPickup(orders[index], pickDate)
            if c == '2':
                retDate = self.orderui.getDateInput()
                self.orderui.editReturn(orders[index], retDate)
            if c == '3':
                self.orderui.cancelOrder(orders[index].getCarPlate(), orders[index].getPickup())
            elif c.upper() == 'W' and index > 0  and len(orders) != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index -= 1
            elif c.upper() == 'S' and index < len(orders) - 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index += 1
            elif c.upper() == 'Q':
                break


    # Prints all apropriate orders and gives the user options on editing them
    # This function is called from orderOptions
    def findOrderAndEdit(self):
        index = 0
        # Gets a list of orders from orderui
        orders = self.orderui.findOrder()
        if orders == []:
            print('Quit d:')
            return
        while orders:
            os.system('cls' if os.name == 'nt' else 'clear')
            # The edit / navigation menu
            self.orderui.printSelectionTable(orders, index)
            print('1. Edit pickup date')
            print('2. Edit return date')
            print('3. Delete order')
            print('q. back')
            print('input W or S to move the arrow up and down')
            # Gets input from user
            c = input()
            # Checks input from user and calls a function from the edit / navigation menu
            if c == '1':
                pickDate = input('Pickup date(YYYY-MM-DD HH:MM:SS):')
                self.orderui.editPickup(orders[index], pickDate)
            if c == '2':
                retDate = input('Return date(YYYY-MM-DD HH:MM:SS):')
                self.orderui.editReturn(orders[index], retDate)
            if c == '3':
                self.orderui.cancelOrder(orders[index].getPlate, orders[index].getPickup)
                if index == len(orders):
                    index -= 1
            elif c.upper() == 'W' and index > 0 and len(orders) != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index -= 1
            elif c.upper() == 'S' and index < len(orders) - 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index += 1
            elif c.upper() == 'Q':
                break
        
    
    # This contains the car options and is called from the home function
    def carOptions(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            # The car menu:
            print('1. Show available cars')
            print('2. Show unavailable cars')
            print('3. Show all cars')
            print('4. Search car by number plate')
            print('q. back')
            # Gets input from user
            c = input()
            # Checks input and calls a function from the car menu
            if c == '1':
                self.availableCarsOptions()
            elif c == '2':
                self.unavailableCarsOptions()
            elif c == '3':
                self.carui.printCSTable(self.carui.retCarData(), 0, 'n')
                input()
            elif c == '4':
                car = input('Number plate: ')
                self.carui.printCSTable(self.carui.findCars(car.upper()), 0, 'n')
                input()
            elif c.upper() == 'Q':
                break

            
    # This contains the available car options and is called from carOptions
    def availableCarsOptions(self):
        # Gets a list of all available cars from carui
        cars = self.carui.AvailableCars()
        index = 0
        while True:
            # prints a table with the cars list
            self.carui.printCSTable(cars, index, 'y')
            print('1. Mark car as available')
            print('input W or S to move the arrow up and down')
            # Gets input from user
            c3 = input()
          
            if c3 == '1':
                # Changes a car status to unavailable
                self.carui.deliverCar(cars[index])
            if c3.upper() == 'W' and index > 0 and len(cars) != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index -= 1
            elif c3.upper() == 'S' and index < len(cars) - 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index += 1            
            elif c3.upper() == 'Q':
                break


    # This contains the unavailable car options and is called from carOptions
    # Prints out a table of unavailable cars.
    def unavailableCarsOptions(self):
        index = 0
        cars = self.carui.UnavailableCars()
        self.carui.printCSTable(cars, index, 'n')
        input()


    # This contains the customer options and is called from the home function
    def customerOptions(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print('1. View/edit all customers')
            print('2. Find specific customer')

            print('q. back')
            c = input()

            if c == '1':
                self.viewAndEditAllCustomers()
            elif c == '2':
                self.viewAndEditCustomer()            
            elif c.upper() == 'Q':
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(c + ' is not a valid command')

    
    # This prints out all customers in a table and gives the user the option
    # to edit them
    def viewAndEditAllCustomers(self):
        index = 0
        customers = self.customerui.retCustomers()
        while True:
            # os.system('cls' if os.name == 'nt' else 'clear')
            self.customerui.printSelectionTable(customers, index)
            print('1. Edit SSN')
            print('2. Edit first name')
            print('3. Edit last name')
            print('4. Edit phone')
            print('5. Edit card number')
            print('6. Delete customer')
            print('q. back')
            print('input W or S to move the arrow up and down')

            c3 = input()
            
            if c3 == '1':
                ssn = input('SSN:')
                self.customerui.editSsn(customers[index], ssn)
            elif c3 == '2':
                firstname = input('First name:')
                self.customerui.editfName(customers[index], firstname)
            elif c3 == '3':
                lastname = input('Last name:')
                self.customerui.editlName(customers[index], lastname)
            elif c3 == '4':
                phone = input('Phone:')
                self.customerui.editPhone(customers[index], phone)
            elif c3 == '5':
                cardnumber = input('Card number:')
                self.customerui.editCardNumber(customers[index], cardnumber)
            elif c3 == '6':
                self.customerui.deleteCustomer(customers[index])
                if index == len(customers):
                    index -= 1
            elif c3.upper() == 'W' and index > 0  and len(customers) != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index -= 1
            elif c3.upper() == 'S' and index < len(customers)-1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index += 1
            elif c3.upper() == 'Q':
                break

    
    # This prints out a list of customers that fit the search pattern
    # Gives the user an option to edit rows
    def viewAndEditCustomer(self):
        # Make and index for the arrow functionality and going through a list
        index = 0
        customers = self.customerui.findCustomer()
        while customers[0] is not None:
            # os.system('cls' if os.name == 'nt' else 'clear')
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
            
            if c3 == '1':
                ssn = input('SSN:')
                self.customerui.editSsn(customers[index], ssn)
            elif c3 == '2':
                firstname = input('First name:')
                self.customerui.editfName(customers[index], firstname)
            elif c3 == '3':
                lastname = input('Last name:')
                self.customerui.editlName(customers[index], lastname)
            elif c3 == '4':
                phone = input('Phone:')
                self.customerui.editPhone(customers[index], phone)
            elif c3 == '5':
                cardnumber = input('Card number:')
                self.customerui.editCardNumber(customers[index], cardnumber)
            elif c3 == '6':
                self.customerui.deleteCustomer(customers[index])
                if index == len(customers):
                    index -= 1
            elif c3.upper() == 'W':
                os.system('cls' if os.name == 'nt' else 'clear')
                index -= 1
            elif c3.upper() == 'W' and index > 0 and len(customers) != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index -= 1
            elif c3.upper() == 'S' and index < len(customers)-1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index += 1
            elif c3.upper() == 'Q':
                break