import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def test_select(selenium):
    selenium.get("https://kodilla.com/pl/test/form/")
    year_combo = selenium.find_element(By.XPATH, "//select[1]")
    Select(year_combo).select_by_index(22)
    year_combo = selenium.find_element(By.XPATH, "//select[2]")
    Select(year_combo).select_by_index(11)
    year_combo = selenium.find_element(By.XPATH, "//select[3]")
    Select(year_combo).select_by_index(84)

    time.sleep(3)
    selenium.quit()