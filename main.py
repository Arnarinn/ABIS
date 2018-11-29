from data import GetData
import datetime
import msvcrt


class UI:
    data = GetData()
    while True:
        print('Welcome to the ABIS manager program!')
        print('___________________________________')
        print('1. New order \n'
              '2. View order \n'
              '3. View cars \n'
              '4. New customer \n'
              '5. View customer \n'
              'q. Quit the program \n')
        c = msvcrt.getch()
        if c == b'1':
            employee = input('Type in employee name:')
            timeOfPickUp = input('Type in time of pick up:')
            timeOfReturn = input('Type in time of return:')
            carNumber = input('Type in car number:')
            data.orderInsert(employee, str(datetime.datetime.now())
                            , timeOfPickUp, timeOfReturn, carNumber)
            msvcrt.getch()
        if c == b'2':
            orderData = data.orderInit()
            print(orderData)
            msvcrt.getch()
        if c == b'3':
            carData = data.carInit()
            for v in carData:
                print('Type: ' + v[0] + '\n'
                      'Color: ' + v[1] + '\n'
                      'Price: ' + v[2] + '\n')
            msvcrt.getch()
        if c == b'q':
            break
