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

    # WRITES the DATA from the customerList into the csv file
    def customerInsert(self, customerList):
        with open('../data/customers.csv', 'w', newline = '') as customerFile:
            customerFileWriter = csv.writer(customerFile)
            # This is the header
            customerFileWriter.writerow(['ssn', 'first name', 'last name',
                                         'age', 'phone', 'other'])
            for obj in customerList:
                customerFileWriter.writerow(obj.dataList())
