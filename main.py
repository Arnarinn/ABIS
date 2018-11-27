
def carinit():
    # Makes an arrays of the lines taken from the cars.txt file
    cars_whole = open('data/cars.txt').read().split('\n')
    # Gets the amount of cars in the file
    car_amount = len(cars_whole)
    # Gets the amount of variables a car has
    car_variables = cars_whole[0].count(' ')+1
    # Makes an empty car_variable x car_amount matrix of arrays.
    cars_matrix = [[0] * car_variables for i in range(car_amount)]
    # Inserts the values from the file into the array
    i: int = 0
    # Further splits each car line into its variables and inputs it into the empty matrix
    for car in cars_whole:
        c = car.split(' ')
        cars_matrix[i] = c
        i += 1
    return cars_matrix

def customerinit():
    # Makes an arrays of the lines taken from the customers.txt file
    customers_whole = open('data/customers.txt').read().split('\n')
    # gets the amount of customers in the file
    customer_amount = len(customers_whole)
    # Gets the amount of variables a customer has
    customer_variables = customers_whole[0].count(' ')+1
    # Makes an empty customer_variables X customer_amount matrix of arrays
    customers_matrix = [[0] * customer_variables for i in range(customer_amount)]
    i: int = 0
    # Further splits each customer line into its variables and inputs it into the empty matrix
    for customer in customers_whole:
        c = customer.split(' ')
        customers_matrix[i] = c
        i += 1
    return customers_matrix
