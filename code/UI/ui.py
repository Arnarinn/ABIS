from Business.employeedomain import EmployeeDomain
import os
import getpass
from .csui import CSUI
from .cmui import CMUI


class Startup:
    def __init__(self):
        self.employeedomain = EmployeeDomain()

    def login(self):
        while True:
            print('Welcome to ABIS!')
            print('___________________________________\n')
            print('Login\n')
            username = input('Username: ').upper()
            password = getpass.getpass('password: ')
            if self.employeedomain.checkLogin(username, password):
                employee = self.employeedomain.getEmployee(username, password)
                if employee.getType() == 'CS':
                    csui = CSUI()
                    csui.home()
                    break
                else:
                    cmui = CMUI()
                    cmui.home()
                    break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Either the username or password was wrong')
