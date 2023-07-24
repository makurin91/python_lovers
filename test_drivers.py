import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def setup_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver_path = ChromeDriverManager(driver_version='114.0.5735.90').install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


driver = setup_chrome()
driver.get(url='https://www.selenium.dev/')
time.sleep(3)
driver.quit()


def setup_firefox():
    options = webdriver.FirefoxOptions()
    driver_path = GeckoDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

driver = setup_firefox()
driver.get(url='https://www.selenium.dev/')
time.sleep(3)
driver.quit()


def setup_safari():
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

driver = setup_safari()
driver.get(url='https://www.selenium.dev/')
time.sleep(3)
driver.quit()