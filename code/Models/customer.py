class Customer:
    def __init__(self, ssn, fname, lname, age, phone, cardnumber):
        self.__ssn = ssn
        self.__fname = fname
        self.__lname = lname
        self.__age = age
        self.__phone = phone
        self.__cardNumber = cardnumber

    def __str__(self):
        return 'First name: {}, Last name: {}, Age: {}, Phone: {}, SSN: {}, Card number: {}'\
            .format(self.__fname, self.__lname, self.__age, self.__phone, self.__ssn,\
             self.__cardNumber)

    def __repr__(self):
        return 'Customer({},{},{},{},{},{})'.format(self.__fname, self.__lname,\
            self.__age, self.__phone, self.__ssn, self.__cardNumber)

    def dataList(self):
        cList = []

        cList.append(self.__ssn)
        cList.append(self.__fname)
        cList.append(self.__lname)
        cList.append(self.__age)
        cList.append(self.__phone)
        cList.append(self.__cardNumber)
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

    def getCardNumber(self):
        return self.__cardNumber

    def setSsn(self, ssn):
        self.__ssn = ssn

    def setfName(self, fname):
        self.__fname = fname

    def setlName(self, lname):
        self.__lname = lname

    def setAge(self, age):
        self.__age = age

    def setPhone(self, phone):
        self.__phone = phone

    def setCardNumber(self, cardnumber):
        self.__cardNumber = cardnumber
