import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class POM:
    @staticmethod
    def init(driver):
        POM.driver = driver

    search_field = lambda: POM.driver.find_element(By.XPATH, "//*[@id='searchField']")



def main():
    chrome_options = Options()
    chrome_options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Chrome(options=chrome_options)
    url = "https://kodilla.com/pl/test/store"
    driver.get(url)

    def test():
        POM.init(driver)
        POM.search_field().send_keys("NoteBook")
        POM.search_field().click()

    time.sleep(3)
	
if __name__ == '__main__':
    main()