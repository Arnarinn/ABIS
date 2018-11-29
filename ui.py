from domain import Domain
from data import GetData
import msvcrt
import datetime

class UI:
    def __init__(self):
        self.data = GetData()
        self.domain = Domain()

    def login(self):
        login = 5

    def home(self):
        while True:
            print('Welcome to the ABIS manager program!')
            print('___________________________________')
            print('1. New order \n'
                  '2. View orders \n'
                  '3. View cars \n'
                  '4. New customer \n'
                  '5. View customers \n'
                  'q. Quit the program \n')
            c = msvcrt.getch()
            if c == b'1':
                employee = input('Type in employee name:')
                timeOfPickUp = input('Type in time of pick up:')
                timeOfReturn = input('Type in time of return:')
                carNumber = input('Type in car number:')
                self.data.orderInsert(employee, str(datetime.datetime.now())
                                 , timeOfPickUp, timeOfReturn, carNumber)
                msvcrt.getch()
            if c == b'2':
                orderData = self.domain.getOrderData()
                print(orderData)
                msvcrt.getch()
            if c == b'3':
                carData = self.domain.getCarData()
                for v in carData:
                    print('Type: ' + v[0] + '\n'
                          'Color: ' + v[1] + '\n'
                          'Price: ' + v[2] + '\n')
                msvcrt.getch()
            if c == b'q':
                break
