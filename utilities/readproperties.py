import configparser
config = configparser.RawConfigParser()
config.read("/Users/ganeshkumar/PycharmProjects/Sauce_Demo/Configuration/saucedemo_config.ini")

class ReadConfig:

    @staticmethod
    def getAPPURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getusename1():
        Uname1 = config.get('common info', 'username_1')
        return Uname1

    @staticmethod
    def getusename2():
        Uname2 = config.get('common info', 'username_2')
        return Uname2

    @staticmethod
    def getpassword():
        Pword = config.get('common info', 'password')
        return Pword