from configparser import ConfigParser

# config = ConfigParser()
# config.read("..\\ConfigurationData\\conf.ini")
# print(config.get("locators", "phone_CSS"))

def readConfig(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\conf.ini")
    return config.get(section, key)
