import time
from selenium.webdriver.common.by import By

def test_login(selenium):
    selenium.get("https://kodilla.com/pl/test/login")
    email_field = selenium.find_element(By.XPATH, "/html/body/section/form/div[1]/input")
    email_field.send_keys("testuser@gmail.com")

    time.sleep(3)
    selenium.quit()