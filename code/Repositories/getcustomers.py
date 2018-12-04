from .formatdata import formatData


class GetCustomers:
    def customerData(self):
        formattedData = formatData(open('data/customers.csv'))
        customerObjectArray = []
        for line in formattedData:
            customerObjectArray.append(Customer(line[0], line[1], line[2]))
        return customerObjectArray
        # return formatData(open('data/customers.csv'))

    def customerInsert(self, customer):
        with open('data/customers.csv', 'a+') as customerFile:
            customerFile.write(customer.__repr__() + '\n')
