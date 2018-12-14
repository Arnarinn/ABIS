import os
from .carui import CarUi

class CMUI:
    def __init__(self):
        self.carui = CarUi()
    
    # The main menu for Car Maintenance employees.
    def home(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            # The main menu
            print('Welcome to the ABIS, the Car Maintenance program!\n'
                  '___________________________________ \n'
                  'Press the according number or letter to navigate between pages \n')
            print('1. Show available cars \n'
                  '2. Show unavailable cars\n'
                  '3. Show all cars \n'
                  '4. Search car by number plate \n'
                  'q. Quit \n')
            # Detects a button press and which button was pressed
            c2 = input()
            
            # Checks input from user and calls a function from the menu
            if c2 == '1':
                self.availableCarsOptions()
            elif c2 == '2':
                self.unavailableCarsOptions()
            elif c2 == '3':
                self.carui.printCMTable(self.carui.retCarData(), 0, 'n')
                input('Press any key to Continue')
            elif c2 == '4':
                self.searchCarOptions()
            elif c2.upper() == 'Q':
                break

    # This contains the available car options and is called from carOptions
    def availableCarsOptions(self):
        # Gets a list of all available cars from carui
        index = 0
        while True:
            cars = self.carui.AvailableCars()
            os.system('cls' if os.name == 'nt' else 'clear')
            # prints a table with the cars list
            self.carui.printCMTable(cars, index, 'y')
            print('1. Change the car status to unavailable - delivered\n'
                  'w. Move the arrow up \n'
                  's. Move the arrow down \n'
                  'q. Back \n')
            # Gets input from user
            c3 = input() 
            if c3 == '1':
                # Changes a car status to unavailable
                self.carui.deliverCar(cars[index])
                # Lets the arrow move up / down
            elif c3.upper() == 'W' and index > 0 and len(cars) != 1:
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
        while True:
            cars = self.carui.UnavailableCars()
            os.system('cls' if os.name == 'nt' else 'clear')
            self.carui.printCMTable(cars, index, 'y')
            print('0. Change the car status to available - returned \n'
                  'w. Move the arrow up \n'
                  's. Move the arrow down \n'
                  'q. Back \n')
            # Gets input from user
            c4 = input()
            if c4 == '0':
                # Changes a car status to available
                self.carui.returnCar(cars[index])
                # Lets the arrow move up / down
            elif c4.upper() == 'W' and index > 0 and len(cars) != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index -= 1
            elif c4.upper() == 'S' and index < len(cars) - 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                index += 1        
            elif c4.upper() == 'Q':
                break
    def searchCarOptions(self):
        while True:
            # Gets input from user that contains car number plate number
            os.system('cls' if os.name == 'nt' else 'clear')
            car = input('Number plate (5 characters): ')
            self.carui.printCMTable(self.carui.findCars(car.upper()), 0, 'n')
            print('q. Back \n'
                  'Or press enter to search again \n')
            # Gets input from user
            c5 = input()
            if c5.upper() == 'Q':
                break
