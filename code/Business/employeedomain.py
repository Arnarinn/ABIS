from .domain import Domain

class EmployeeDomain():
    def __init__(self):
        self.employees = Domain.getEmployeeData(Domain())

    def checkLogin(self, username, password):
        for e in self.employees:
            if e.getUsername() == username:
                if e.getPassword() == password:
                    return True
        return False

    def getEmployee(self, username, password):
        for e in self.employees:
            if username == e.getUsername():
                if password == e.getPassword():

                    return e

    def returnType(self, employee):
        print(employee)
        for e in self.employees:
            if employee.getUsername() == e.getUsername():
                if employee.getPassword() == e.getPassword:
                    print(e.getType())
                    return e.getType()
