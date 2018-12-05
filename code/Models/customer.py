class Customer:
    def __init__(self, ssn, firstname, lastname, age, phone, other):
        self.__ssn = ssn
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__phone = phone
        self.__other = other
    def __str__(self):
        return 'First name: {}, Last name: {}, Age: {}, Phone: {}, SSN: {}, Other: {}'.format(self.__firstname, self.__lastname, self.__age, self.__phone, self.__ssn, self.__other)

    def __repr__(self):
        return 'Customer({},{},{},{},{},{})'.format(self.__firstname, self.__lastname, self.__age, self.__phone, self.__ssn, self.__other)
