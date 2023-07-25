import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains


def setup_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver_path = ChromeDriverManager(driver_version='114.0.5735.90').install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


DOWNLOAD_BTN = '//*[contains(text(), "Downloads")]'
HEAD_TEXT = '//h1[contains(text(), "Downloads")]'
SUPPORT_BTN = '/html/body/div/main/div[8]/div/div/ul/li[2]/p/a'
RELEASES_BTN = '//a[contains(text(), "releases")]'

if __name__ == "__main__":
    driver = setup_chrome()
    driver.get(url='https://www.selenium.dev/')

    time.sleep(3)
    find_download_btn = driver.find_element(By.XPATH, DOWNLOAD_BTN)
    find_download_btn.click()

    get_text = driver.find_element(By.XPATH, HEAD_TEXT)
    check_text = get_text.text
    assert check_text == "Downloads", f"Wrong text {check_text}"
    print("Assert Passed")

    time.sleep(3)

    find_support_btn = driver.find_element(By.XPATH, SUPPORT_BTN)

    if find_support_btn:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});",
                              find_support_btn)
    else:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    find_support_btn.click()
    # actions = ActionChains(driver)
    # actions.move_to_element(find_support_btn).perform()

    time.sleep(3)
