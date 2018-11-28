import data

class UI:
    print('Welcome to the ABIS manager program!')
    print('___________________________________')
    print('1. New order'
          '2. View order'
          '3. View cars'
          '4. New customer'
          '5. View customer')
    #option = input('Choose')
    carMatrix = data.carinit()
    print(carMatrix)
    customerMatrix = data.customerinit()
    print(customerMatrix)
