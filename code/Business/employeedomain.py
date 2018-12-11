from .domain import Domain


class EmployeeDomain:
    def __init__(self):
        self.employees = Domain.getEmployeeData(Domain())

    # returns true if the employee exists, very similar to the
    # getEmployee function, the other just returns the employee found
    def checkLogin(self, username, password):
        for e in self.employees:
            if e.getUsername() == username:
                if e.getPassword() == password:
                    return True
        return False

    # Returns the employee object that fits the inserted username and password
    def getEmployee(self, username, password):
        for e in self.employees:
            if username == e.getUsername():
                if password == e.getPassword():
                    return e

