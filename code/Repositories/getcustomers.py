from .formatdata import formatData
from Models.customer import Customer
import csv


class GetCustomers:


    def customerData(self):
        # Uses formatData to load the customers.csv into a list
        formattedData = formatData(open('../data/customers.csv', 'r'))
        customerObjectArray = []
        # List from formatData used to fill Customer objects.
        # The objects are then stored in a list.
        for line in formattedData:
            customerObjectArray.append(Customer(line[0], line[1], line[2],
                                                line[3], line[4], line[5]))
        return customerObjectArray


    # APPENDS the DATA for one new customer to the customers.csv
    def customerInsert(self, customer):
        with open('../data/customers.csv', 'a', newline = '') as customerFile:
            customerFileWriter = csv.writer(customerFile)
            customerFileWriter.writerow(customer)
