from domain import Domain
import msvcrt
import datetime
import os


class Login:
    def __init__(self):
        self.domain = Domain()
        self.csui = CSUI()

    def login(self):
        while True:
            print('          Login')
            username = input('Username: ')
            password = input('password: ')
            if self.domain.checkLogin(username, password):
                self.csui.home()
                break
            else:
                os.system('cls')
                print('Either the username or password was wrong')


class CSUI:
    def __init__(self):
        self.domain = Domain()

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
            c = msvcrt.getch()
            if c == b'1':
                os.system('cls')
                # loads of inputs to insert into the csv file
                employee = input('Type in employee name:')
                timeOfPickUp = input('Type in time of pick up:')
                timeOfReturn = input('Type in time of return:')
                carNumber = input('Type in car number:')
                self.domain.insertOrder(employee, str(datetime.datetime.now())
                                 , timeOfPickUp, timeOfReturn, carNumber)
                # Waits for any input on the keyboard
                # to give time for user to read their info
                print('press any key to go back')
                msvcrt.getch()
            if c == b'2':
                os.system('cls')
                orderData = self.domain.getOrderData()
                for v in orderData:
                    print(v.__str__())
                # Waits for any input on the keyboard
                # to give time for user to read their info
                print('press any key to go back')
                msvcrt.getch()
            if c == b'3':
                os.system('cls')
                carData = self.domain.getCarData()
                for v in carData:
                    print('Type: ' + v[0] + '\n'
                          'Color: ' + v[1] + '\n'
                          'Price: ' + v[2] + '\n')
                # Waits for any input on the keyboard
                # to give time for user to read their info
                print('press any key to go back')
                msvcrt.getch()
            if c == b'5':
                os.system('cls')
                customerData = self.domain.getCustomerData()
                for v in customerData:
                    print(v.__str__())
                # Waits for any input on the keyboard
                # to give time for user to read their info
                print('press any key to go back')
                msvcrt.getch()
            if c == b'q':
                os.system('cls')
                break
#class CMUI:





