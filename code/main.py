import os
from UI.ui import Startup


def main():
    Ui = Startup()
    os.system('cls' if os.name == 'nt' else 'clear')
    Ui.login()


if __name__ == '__main__':
    main()

