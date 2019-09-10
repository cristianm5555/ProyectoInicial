import unittest
from selenium import webdriver

class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:/Users/cristian.moyano/Documents/Personal/Globant/JMeterSeleniumZAP/Drivers/chromedriver.exe")
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")

    def tearDown(self):
        self.driver.quit()