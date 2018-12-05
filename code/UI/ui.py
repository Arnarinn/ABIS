from Business.domain import Domain
import os
from .csui import CSUI
from .cmui import CMUI


class Startup:
    def __init__(self):
        self.domain = Domain()

    def login(self):
        while True:
            print('          Login')
            username = input('Username: ').upper()
            password = input('password: ')
            if self.domain.checkLogin(username, password):
                csui = CSUI(self.domain)
                csui.home()
                break
            else:
                os.system('cls')
                print('Either the username or password was wrong')







