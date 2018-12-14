import os
from .carui import CarUi

class CMUI:
    def __init__(self, domain):
        self.domain = domain
        self.carui = CarUi()
    
    def home(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print('Welcome to the ABIS, the Car Maintenance program!')
            print('___________________________________')
            print('1. Show available cars')
            print('2. Show unavailable cars')
            print('3. Show all cars')
            print('4. Search car by number plate')

            print('q. quit')
            c2 = input()

            # OPTION 1 SUB 1
            if c2 == '1':
                self.carui.printCMTable(self.carui.CMDispAvailableCars(), 0, 'n')
                print('Press any key to Continue')
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
