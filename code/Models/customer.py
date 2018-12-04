class Customer:
    def __init__(self, ssn, name, age):
        self.__ssn = ssn
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'Name: {}, Age: {}, SSN: {}'.format(self.__name, self.__age, self.__ssn)

    def __repr__(self):
        return 'Customer({},{},{})'.format(self.__name, self.__age, self.__ssn)
