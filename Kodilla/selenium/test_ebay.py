import time
from datetime import datetime, timezone
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_store_search(driver):
    driver.get("https://www.ebay.com/")
    search = driver.find_element(By.NAME, "_nkw")
    search.send_keys("Laptop")
    computers = driver.find_element(By.XPATH("/html/body/div[6]/div[3]/ul/li[1]/ul/li[1]/div[2]/ul/li/ul/li[1]/a/span"))
    #podałem full xpath, ale dalej nie działa
    computers.send_click()
    time.sleep(3)
    driver.quit()

'''def test_search(driver):
    driver.get("https://www.ebay.com/")
    computers = driver.find_element(By.CSS_SELECTOR('//*[@id="x-refine__group__0"]/ul/li/ul/li[1]/a/span'))
    #podpytać dlaczego mam ten błąd z timestamp i czy mogę kopiować z narzędzi dev chrome po copy ---> Xpath?
    computers.send_click()
    time.sleep(3)
    driver.quit()'''