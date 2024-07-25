from selenium import webdriver
from selenium.webdriver.common.by import By

def test_zadanie():
    driver = webdriver.Chrome()
    driver.get("https://kodilla.com/pl/test/store")

    def search_laptop(search_term):
        search_box = driver.find_element(By.XPATH, "//input[@id='searchField']")
        search_box.send_keys(search_term)
        results_container = driver.find_element(By.CSS_SELECTOR, "#elements-wrapper")
        div_elements = results_container.find_elements(By.CLASS_NAME, "elements-wrapper")
        return(div_elements)
        # nie wiem jak zrobić tak, żeby mi same divy zliczało??

    assert search_laptop("laptop") == 3
    assert search_laptop("NoteBook") == 2
    assert search_laptop("Gaming") == 1
