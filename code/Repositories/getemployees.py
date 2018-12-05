from .formatdata import formatData
from Models.employee import Employee

class GetEmployees:
    def employeeData(self):
        formattedData = formatData(open('../data/employees.csv'))
        employeeObjectArray = []
        for line in formattedData:
            employeeObjectArray.append(Employee(line[0], line[1], line[2]))
        return employeeObjectArray
