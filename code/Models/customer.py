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

    def dataList(self):
        cList = []

        cList.append(self.__ssn)
        cList.append(self.__fname)
        cList.append(self.__lname)
        cList.append(self.__age)
        cList.append(self.__phone)
        cList.append(self.__other)
        return cList

    def getSsn(self):
        return self.__ssn

    def getFName(self):
        return self.__fname

    def getLName(self):
        return self.__lname

    def getAge(self):
        return self.__age

    def getPhone(self):
        return self.__phone

    def getOther(self):
        return self.__other
