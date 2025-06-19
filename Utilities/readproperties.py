import configparser
import os

config=configparser.RawConfigParser()
path=os.path.abspath(os.path.abspath(os.curdir)+"/configuration/config.ini")

class ReadConfig:
    def get_ApplicationURL(self):
        url=config.get("CommonInfo","url")
        return url

    def get_Username(self):
        username=config.get("CommonInfo","email")
        return username

    def get_Password(self):
        password=config.get("CommonInfo","password")
        return password
