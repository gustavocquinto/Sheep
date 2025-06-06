from config.settings import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverService():

    def __init__(self):
        serviceDriver_path = Service(driver_path)

        self.url_app = url_app

        self.driver = webdriver.Chrome(service=serviceDriver_path)
        self.driver.maximize_window()

        self.wait = WebDriverWait(self.driver, timeoutWait)

