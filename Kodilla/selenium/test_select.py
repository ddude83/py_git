import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def test_select(selenium):
    selenium.get("https://kodilla.com/pl/test/form/")
    year_combo = selenium.find_element(By.XPATH, "//*[@id='birthday_wrapper']/select[3]")
    Select(year_combo).select_by_index(5)

    time.sleep(3)
    selenium.quit()