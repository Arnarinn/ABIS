from .formatdata import formatData
from Models.customer import Customer

class GetCustomers:
    def customerData(self):
        formattedData = formatData(open('../data/customers.csv'))
        customerObjectArray = []
        for line in formattedData:
            customerObjectArray.append(Customer(line[0], line[1], line[2]))
        return customerObjectArray

    def customerInsert(self, customer):
        with open('../data/customers.csv', 'a+') as customerFile:
            customerFile.write(customer.__repr__() + '\n')
