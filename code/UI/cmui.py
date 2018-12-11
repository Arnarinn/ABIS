import msvcrt
import os


class CMUI:
    def __init__(self, domain):
        self.domain = domain
    
    def home(self):
        while True:
            os.system('cls')
            print('Welcome to the ABIS manager program!')
            print('___________________________________')
            print('1. Mark car as delivered \n'
                '2. Mark car as returned \n'
                '3. View cars \n'
                'q. Quit the program \n')
            # Detects a button press and which button was pressed
            c = msvcrt.getch()
            if c == b'1':
                self.carDelivered()
            if c == b'2':
                self. carReturned()
            if c == b'3':
                self.viewCars()
            if c == b'q':
                os.system('cls')
                break
    def carDelivered(self):
        os.system('cls')
        # loads of inputs to insert into the csv file
        employee = input('Type in employee name:')
        carNumber = input('Type in car number:')
        # sends the info to the business layer
        # which inserts it into the relevant file
        self.domain.insertOrder(employee, carNumber)
        # Waits for any input on the keyboard
        # to give time for user to read their info
        print('press any key to go back')
        msvcrt.getch()

    def carReturned(self):
        os.system('cls')
        employee = input('Type in employee name:')
        carNumber = input('Type in car number:')
        self.domain.insertOrder(employee, carNumber)
        # Waits for any input on the keyboard
        # to give time for user to read their info
        print('press any key to go back')
        msvcrt.getch()

    def viewCars(self):
        os.system('cls')
        carData = self.domain.getCarData()
        for v in carData:
            print(v)
        # Waits for any input on the keyboard
        # to give time for user to read their info
        print('press any key to go back')
        msvcrt.getch()
        