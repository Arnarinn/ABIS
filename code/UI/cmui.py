import os
from .carui import CarUi

class CMUI:
    def __init__(self, domain):
        self.domain = domain
        self.carui = CarUi()
    
    # The main menu for Car Maintenance employees.
    def home(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            # The main menu
            print('Welcome to the ABIS, the Car Maintenance program!')
            print('___________________________________')
            print('1. Show available cars \n'
                  '2. Show unavailable cars\n'
                  '3. Show all cars \n'
                  '4. Search car by number plate \n'
                  'q. quit \n')
            # Detects a button press and which button was pressed
            c2 = input()
            
            # Checks input from user and calls a function from the menu

            if c2 == '1':
                self.availableCarsOptions()
            elif c2 == '2':
                self.unavailableCarsOptions()
            elif c2 == '3':
                self.carui.printCSTable(self.carui.retCarData(), 0, 'n')
                input()
            elif c2 == '4':
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
            print('q. back \n')
            # Gets input from user
            c3 = input()        
            if c3.upper() == 'Q':
                break
    # This contains the unavailable car options and is called from carOptions
    # Prints out a table of unavailable cars.
    def unavailableCarsOptions(self):
        index = 0
        while True:
            cars = self.carui.UnavailableCars()
            self.carui.printCSTable(cars, index, 'n')
            print('q. back \n')
            # Gets input from user
            c4 = input()
            if c4.upper() == 'Q':
                break
'''
            # OPTION 1 SUB 1
            if c2 == '1':
                self.carui.printCMTable(self.carui.CMDispAvailableCars(), 0, 'n')
                input()

            # OPTION 2 SUB 1
            elif c2 == '2':
                index = 0
                cars = self.carui.CMDispUnavailableCars()
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.carui.printCMTable(cars, index, 'y')
                    print('1. Mark selected car as available')
                    c3 = input()

                    # OPTION 1 SUB 2
                    if c3 == '1':
                        self.carui.returnCar(cars[index])

                    # OPTION W SUB 2
                    if c3.upper() == 'W' and index > 0 and len(cars) != 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        index -= 1

                    # OPTION S SUB 2
                    elif c3.upper() == 'S' and index < len(cars) - 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        index += 1

                    # OPTION Q SUB 2
                    elif c3.upper() == 'Q':
                        break

            # OPTION 3 SUB 1
            elif c2 == '3':
                self.carui.printCMTable(self.carui.retCarData(), 0, 'n')
                input()

            # OPTION 4 SUB 1
            elif c2 == '4':
                while True:
                    car = input('Number plate: ')
                    self.carui.printCMTable(self.carui.findCars(car.upper()), 0, 'n')
                    input()

            # OPTION Q SUB 1
            elif c2.upper() == 'Q':
                break
'''