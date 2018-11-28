class getData:
    def __init__(self):
        # Get the data from the car csv file
        self.carsWholeR = open('data/cars.csv')
        # Gets the data from the customer csv file
        self.customersWholeR = open('data/customers.csv')
        self.customersWholeA = open('data/customers.csv', 'a')

    def carInit(self):
        # Makes an arrays of the lines taken from the cars.csv file
        with self.carsWholeR as c:
            carsWhole = c.readlines()
        # Gets the amount of cars in the file
        carAmount = len(carsWhole)
        # Gets the amount of variables a car has
        carVariables = carsWhole[0].count(' ')+1
        # Makes an empty car_variable x car_amount matrix of arrays.
        cars_matrix = [[0] * carVariables for i in range(carAmount)]
        # Inserts the values from the file into the array
        i: int = 0
        # Further splits each car line into its variables and inputs it into the empty matrix
        for car in carsWhole:
            c = car.split(',')
            cars_matrix[i] = c
            i += 1
        self.carsWholeR.close()
        return cars_matrix

    def customerInit(self):
        # Makes an arrays of the lines taken from the customers.csv file
        with self.customersWholeR as c:
            customersWhole = c.readlines()
        # gets the amount of customers in the file
        customer_amount = len(customersWhole)
        # Gets the amount of variables a customer has
        customer_variables = customersWhole[0].count(' ')+1
        # Makes an empty customer_variables X customer_amount matrix of arrays
        customers_matrix = [[0] * customer_variables for i in range(customer_amount)]
        i: int = 0
        # Further splits each customer line into its variables and inputs it into the empty matrix
        for customer in customersWhole:
            c = customer.split(',')
            customers_matrix[i] = c
            i += 1
        self.customersWholeR.close()
        return customers_matrix

    def customerInsert(self, name, age):
        str = '\n'+name+','+age
        self.customersWholeA.write(str)
        self.customersWholeA.close()
