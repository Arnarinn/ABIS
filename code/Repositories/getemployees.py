from .formatdata import formatData


class GetEmployees:
    def emplyeeData(self):
        return formatData(open('../../data/employees.csv'))
