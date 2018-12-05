import os
import sys
#sys.path.append('..')
from UI.ui import Startup


def main():
    Ui = Startup()
    os.system('cls')
    Ui.login()


if __name__ == '__main__':
    main()

