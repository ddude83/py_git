from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class W3SchoolPage:
   url = "https://www.w3schools.com/"

   def __init__(self, driver):
      self.driver = driver

   def open(self):
      self.driver.get(self.url)

   def close(self):
      self.driver.quit()

   def set_window_size(self, x, y):
      self.driver.set_window_size(x, y)

   def get_top_bar_elements(self):
      return self.driver.find_elements(By.CSS_SELECTOR, "#pagetop a")

def main():
   chrome_options = Options()
   chrome_options.add_argument("--remote-allow-origins=*")

   driver = webdriver.Chrome(options=chrome_options)
   page = W3SchoolPage(driver)
   page.open()

   page.set_window_size(1920, 1080) # Full HD
   elements = page.get_top_bar_elements()
   assert elements[1].text == "Tutorials"
   assert elements[1].is_displayed()
   assert elements[2].text == "Exercises"
   assert elements[2].is_displayed()
   assert elements[3].text == "Certificates"
   assert elements[3].is_displayed()
   assert elements[4].text == "Services"
   assert elements[4].is_displayed()
   assert elements[5].text == ""
   assert not elements[5].is_displayed()

   page.set_window_size(390, 844) # iPhone 14
   elements = page.get_top_bar_elements()
   assert elements[1].text == ""
   assert not elements[1].is_displayed()
   assert elements[2].text == ""
   assert not elements[2].is_displayed()
   assert elements[3].text == ""
   assert not elements[3].is_displayed()
   assert elements[4].text == ""
   assert not elements[4].is_displayed()
   assert elements[5].text == "Menu"
   assert elements[5].is_displayed()

   page.close()

if __name__ == '__main__':
   main()