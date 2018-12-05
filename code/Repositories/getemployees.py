from .formatdata import formatData


class GetEmployees:
    def employeeData(self):
        return formatData(open('../../data/employees.csv'))
