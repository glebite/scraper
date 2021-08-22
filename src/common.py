"""
common.py
button class="lds__privacy-policy__btnClose"
       class="lds__privacy-policy__btnClose"
Ontario
"""
import time
from selenium import webdriver


LOCATION = 'https://www.yourindependentgrocer.ca/'
ONTARIO_BUTTON = "//button[contains(text(), 'Ontario')]"
PRIVACY_BUTTON = 'lds__privacy-policy__btnClose'


class Common(object):
    def __init__(self, config_file=None):
        """
        """
        self.driver = webdriver.Firefox()
        self.driver.get(LOCATION)

    def __del__(self):
        """
        """
        self.driver.close()

    def find(self, tag, tag_class):
        """
        """
        d = self.driver.find_element_by_class_name(PRIVACY_BUTTON)
        print(d)
        if d:
            d.click()


if __name__ == "__main__":
    x = Common()
    time.sleep(10)
    x.find('button', 'something')
    time.sleep(5)
    button = x.driver.find_element_by_xpath(ONTARIO_BUTTON)
    print(button)
    time.sleep(10)
    button.click()
    time.sleep(30)
