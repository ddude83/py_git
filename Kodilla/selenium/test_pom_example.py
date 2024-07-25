import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class POM:
    @staticmethod
    def init(driver):
        POM.driver = driver

    email_field = lambda: POM.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    password_field = lambda: POM.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    login_button = lambda: POM.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

def main():
    chrome_options = Options()
    chrome_options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Chrome(options=chrome_options)
    url = "https://kodilla.com/pl/test/login"
    driver.get(url)

    POM.init(driver)
    POM.email_field().send_keys("test@kodilla.com")
    POM.password_field().send_keys("kodilla123")
    POM.login_button().click()

    time.sleep(3)

if __name__ == '__main__':
    main()