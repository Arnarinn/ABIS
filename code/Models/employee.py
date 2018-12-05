class Employee:
    def __init__(self, username, password, type):
        self.__username = username
        self.__password = password
        self.__type = type

    def __str__(self):
        return 'username: {}, password: secret, type {}'.format(self.__username,
                                                                self.__type)

    def __repr__(self):
        return 'Employee({},{},{})'.format(self.__username,
                                           self.__password,
                                           self.__type)

    def getType(self):
        return self.__type

    def getUsername(self):
        return self.__username
