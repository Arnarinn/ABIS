from Business.domain import Domain
from Business.employeedomain import EmployeeDomain
import os
from .csui import CSUI
from .cmui import CMUI


class Startup:
    def __init__(self):
        self.domain = Domain()
        self.employeedomain = EmployeeDomain()

    def login(self):
        while True:
            print('          Login')
            username = input('Username: ').upper()
            password = input('password: ')
            if self.employeedomain.checkLogin(username, password):
                employee = self.employeedomain.getEmployee(username, password)
                if employee.getType() == 'CS':
                    csui = CSUI(self.domain)
                    csui.home()
                    break
                else:
                    cmui = CMUI(self.domain)
                    print('entered CM UI')
                    break
            else:
                os.system('cls')
                print('Either the username or password was wrong')
