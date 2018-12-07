class Customer:


    def __init__(self, ssn, fname, lname, age, phone, other):
        self.__ssn = ssn
        self.__fname = fname
        self.__lname = lname
        self.__age = age
        self.__phone = phone
        self.__other = other


    def __str__(self):
        return 'First name: {}, Last name: {}, Age: {}, Phone: {}, SSN: {}, Other: {}'\
            .format(self.__fname, self.__lname, self.__age, self.__phone, self.__ssn,\
             self.__other)


    def __repr__(self):
        return 'Customer({},{},{},{},{},{})'.format(self.__fname, self.__lname,\
            self.__age, self.__phone, self.__ssn, self.__other)
