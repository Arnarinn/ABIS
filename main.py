class startup:
    car_pure = open('cars')
    car_info = car_pure.read().split('\n')
    for ci in car_info:
        car = ci.split(' ')
        print('Type: ' + car[0])
        print('Color: ' + car[1])
        print('Price: ' + car[2])
        print('_________________')