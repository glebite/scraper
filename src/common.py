"""
common.py
"""
import time
from selenium import webdriver


LOCATION = 'https://www.yourindependentgrocer.ca/'


class Common(object):
    def __init__(self, config_file=None):
        self.driver = webdriver.Firefox()
        self.driver.get(LOCATION)


    def __del__(self):
        self.driver.close()


if __name__=="__main__":
    x = Common()
    del x
