"""
common.py
button class="lds__privacy-policy__btnClose"
       class="lds__privacy-policy__btnClose"
Ontario
"""
import time
from selenium import webdriver


URL = 'https://www.yourindependentgrocer.ca/'
ONTARIO_BUTTON = "//button[contains(text(), 'Ontario')]"
PRIVACY_BUTTON = 'lds__privacy-policy__btnClose'
LOCATION_CRULLER = 'data-cruller="current-location"'


class Common(object):
    def __init__(self, config_file=None):
        """
        """
        self.driver = webdriver.Firefox()
        self.driver.get(URL)

    def __del__(self):
        """__del__ - perform any needed cleanup action
        """
        self.driver.close()

    def find(self, tag, tag_class):
        """find - find a specific element by classname
        """
        d = self.driver.find_element_by_class_name(PRIVACY_BUTTON)
        if d:
            d.click()

    def goto(self, url=None):
        """goto - retrieve the URL location
        """
        try:
            self.driver.get(url)
        except Exception as e:
            print(f'Exception: {e}')


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
