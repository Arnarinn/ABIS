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
            print('1. Mark car as delivered \n'
                '2. Mark car as returned \n'
                '3. View all cars \n'
                'q. Quit the program \n')

            # Detects a button press and which button was pressed
            c = input()
            if c == '1':
                self.carui.returnCar()
            elif c == '2':
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')

                    print('1. Show available cars')
                    print('2. Show unavailable cars')
                    print('3. Show all cars')

                    print('q. go backwards')
                    c2 = input()
                    if c2 == '1':
                        self.carui.CMDispAvailableCars()
                        input()
                    elif c2 == '2':
                        self.carui.CMDispUnavailableCars()
                        input()
                    elif c2 == '3':
                        self.carui.printCMTable(self.carui.retCarData())
                    elif c2 == 'q':
                        break
            elif c == 'q':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
