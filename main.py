from data import getData


class UI:
    data = getData()
    print('Welcome to the ABIS manager program!')
    print('___________________________________')
    print('1. New order \n'
          '2. View order \n'
          '3. View cars \n'
          '4. New customer \n'
          '5. View customer \n')
    option = input('Choose')
    if option == 3:
        carData = data.carInit()
        for v in carData:
            print('Type: ' + v[0] + '\n'
                  'Color: ' + v[1] + '\n'
                  'Price: ' + v[2])
