'''
Przykład logowania do przykładowej strony kodilli
'''

import time
from selenium.webdriver.common.by import By

def test_login(selenium):
    selenium.get("https://kodilla.com/pl/test/login")
    email_field = selenium.find_element(By.XPATH, "/html/body/section/form/div[1]/input")
    email_field.send_keys("test@kodilla.com")
    password_field = selenium.find_element(By.XPATH, "/html/body/section/form/div[2]/input")
    password_field.send_keys("kodilla123")
    login_button = selenium.find_element(By.XPATH, "/html/body/section/form/button")
    login_button.click()

    time.sleep(3)
    selenium.quit()